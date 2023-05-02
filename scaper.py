import os
import re
import googleapiclient.discovery
import pandas as pd

SOCIAL_MEDIA = ["twitter","facebook","twitch","linkedin", "instagram", "fanlink", "tiktok", "discord", "reddit"]

def get_channel_id(channel_url):
    """
    -------------------------------------------------------
    Returns the channel ID from URL
    Use: channel_id = get_channel_id(URL)
    -------------------------------------------------------
    Parameters:
        channel_url - contains the url to the channel
    -------------------------------------------------------
    """
    return channel_url.split("/")[-1]

def get_video_id(video_url):
    """
    -------------------------------------------------------
    Returns the video ID from URL
    Use: video_id = get_video_id(URL)
    -------------------------------------------------------
    Parameters:
        video_url - contains the url to the video
    -------------------------------------------------------
    """
    return video_url.split("watch?v=")[-1]

def get_popular_channels(api_key, max_results = 5000):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    request = youtube.videoCategories().list(
        part="snippet",
        regionCode="US"
    )
    response = request.execute()

    channels = []
    for category in response['items']:
        category_id = category['id']

        request = youtube.channels().list(
            part="snippet,statistics",
            categoryId=category_id,
            maxResults=50,
            order="viewCount"
        )
        response = request.execute()

        for item in response['items']:
            channel = {
                'id': item['id'],
                'title': item['snippet']['title'],
                'subscriberCount': int(item['statistics']['subscriberCount']),
                'viewCount': int(item['statistics']['viewCount'])
            }
            channels.append(channel)

    channels = sorted(channels, key=lambda x: x['subscriberCount'], reverse=True)[:max_results]
    return channels

def get_recent_videos(channel_id, api_key, max_results=5):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        order="date",
        type="video"
    )
    response = request.execute()

    video_ids = [item['id']['videoId'] for item in response['items']]
    return video_ids

def get_urls_from_descriptions(video_ids, api_key):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    request = youtube.videos().list(
        part="snippet",
        id=",".join(video_ids)
    )
    response = request.execute()

    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    urls = []
    for item in response['items']:
        description = item['snippet']['description']
        found_urls = re.findall(url_pattern, description)
        urls.extend(found_urls)

    return urls


def get_sponsorship_links(urls):
    sponsor = []
    for i in urls:
        if SOCIAL_MEDIA not in i:
            sponsor.append(i)
    return sponsor




if __name__ == "__main__":
    api_key = "AIzaSyCt6zi-h0r4VxKth9R5v9aVTdNX4c_y8yQ"
    popular_channels = get_popular_channels(api_key, max_results=10000)

    all_urls = []
    for channel in popular_channels:
        recent_video_ids = get_recent_videos(channel['id'], api_key)
        urls_from_descriptions = get_urls_from_descriptions(recent_video_ids)

