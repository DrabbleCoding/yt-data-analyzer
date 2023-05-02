import requests
import json

# Set up the API request parameters
API_KEY = "AIzaSyCt6zi-h0r4VxKth9R5v9aVTdNX4c_y8yQ"
video_id = "SUgJdsTCs0E"
url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={API_KEY}"
sponsors_list = ['Aki Bento', 'Audible', 'Blue Apron', 'BetterHelp', 'Bokksu', 'Brilliant', 'Candid', 'Casetify', 'Casper', 'Core', 'Crunchyroll', 'Curiosity Stream', 'Current', 'Dark Nemesis', 'Dashlane', 'DBrand', 'Demon Turf', 'Displate', 'Dollar Shave Club', 'DraftKings Sportsbook', 'DressX', 'DoorDash',
                 'Established Titles (Scam)[1]', 'ExpressVPN', 'Filmora', 'Fortnite', 'GFuel', 'Girl Cafe Gun', 'Glossier', 'Google Search', 'Garena Free Fire', 'Genshin Impact', 'Grammarly', 'Hello Fresh', 'Honey', 'Honkai Impact 3rd', 'Indochino', 'Keeps', 'LootBoy', 'Lootcrate (scam)[2]', 'Manscaped', 'Mech Arena', 'MPL - Mobile Premier League', 'Nebula', 'NordVPN', 'Policy Genius', 'Raid: Shadow Legends', 'Raycon', 'Ridge Wallet', 'Rouge Company', 'SakuraCo', 'Scentbird', 'SeatGeek', 'Shaker & Spoon', 'Shopify', 'Skillshare', 'Stamps.com', 'State of Survival', 'Squarespace', 'Surfshark', 'Swagbucks', 'Tunnelbear', 'Tokyo Treat', 'Vessi Footwear', 'Vincero', 'War Thunder', 'Wix']
youtube_channel_urls = [
    "https://www.youtube.com/user/tseries",
    "https://www.youtube.com/user/PewDiePie",
    "https://www.youtube.com/user/Checkgate",
    "https://www.youtube.com/user/setindia",
    "https://www.youtube.com/channel/UCk8GzjMOrta8yxDcKfylJYw",
    "https://www.youtube.com/user/WWEFanNation",
    "https://www.youtube.com/channel/UC295-Dw_tDNtZXFeAPAW6Aw",
    "https://www.youtube.com/user/zeemusiccompany",
    "https://www.youtube.com/channel/UCJplp5SjeGSdVdwsfb9Q7lQ",
    "https://www.youtube.com/user/CanalKondZilla",
]

def get_channel_id_or_username(channel_url):
    channel_type, identifier = channel_url.split('/')[-2:]
    return channel_type, identifier


def get_channel_id(api_key, channel_type, identifier):
    base_url = 'https://www.googleapis.com/youtube/v3'

    if channel_type == 'channel':
        return identifier

    if channel_type == 'user':
        search_url = f'{base_url}/search?part=snippet&type=channel&q={identifier}&key={api_key}'
        search_response = requests.get(search_url)
        search_data = json.loads(search_response.text)

        if 'items' not in search_data:
            print(f"Error: {search_data.get('error', 'Unknown error')}")
            return None

        return search_data['items'][0]['snippet']['channelId']

    return None


def get_video_descriptions(api_key, channel_id, max_results=5):
    base_url = 'https://www.googleapis.com/youtube/v3'

    # Get the channel's uploads playlist ID
    channel_url = f'{base_url}/channels?part=contentDetails&id={channel_id}&key={api_key}'
    channel_response = requests.get(channel_url)
    channel_data = json.loads(channel_response.text)

    if 'items' not in channel_data:
        print(f"Error: {channel_data.get('error', 'Unknown error')}")
        return None

    uploads_playlist_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Get the last n videos
    video_url = f'{base_url}/playlistItems?part=snippet&playlistId={uploads_playlist_id}&maxResults={max_results}&key={api_key}'
    video_response = requests.get(video_url)
    video_data = json.loads(video_response.text)

    # Retrieve the video descriptions
    video_descriptions = []
    for item in video_data['items']:
        video_descriptions.append(item['snippet']['description'])

    return video_descriptions


if __name__ == '__main__':
    # Replace this with the YouTube channel URL
    channel_url = 'https://www.youtube.com/user/tseries'
    channel_type, identifier = get_channel_id_or_username(channel_url)
    channel_id = get_channel_id(API_KEY, channel_type, identifier)

    if channel_id:
        descriptions = get_video_descriptions(API_KEY, channel_id)
        if descriptions:
            descriptions_list = [
                f'Description {i+1}:\n{desc.encode("utf-8", errors="ignore").decode("utf-8")}\n' for i, desc in enumerate(descriptions)]
            print(descriptions_list)
        else:
            print('No descriptions found.')
    else:
        print("Couldn't find the channel ID.")


def get_channel_descriptions(channel_url):
    # Replace this with the YouTube channel URL
    # channel_url = 'https://www.youtube.com/user/tseries'
    channel_type, identifier = get_channel_id_or_username(channel_url)
    channel_id = get_channel_id(API_KEY, channel_type, identifier)

    if channel_id:
        descriptions = get_video_descriptions(API_KEY, channel_id)
        if descriptions:
            descriptions_list = [
                f'Description {i+1}:\n{desc.encode("utf-8", errors="ignore").decode("utf-8")}\n' for i, desc in enumerate(descriptions)]

            print(descriptions_list)
            return descriptions_list
        else:
            print('No descriptions found.')
    else:
        print("Couldn't find the channel ID.")


for url in youtube_channel_urls:
    get_channel_descriptions(url)

# Send the API request and retrieve the response
response = requests.get(url)


def get_video_stats(response):
    response_dict = response.json()
    # Extract the desired information from the API response
    if response_dict["items"]:
        items = response_dict["items"][0]
        likes = items["statistics"]["likeCount"]
        dislikes = items["statistics"].get("dislikeCount", 0)
        channel_name = items["snippet"]["channelTitle"]
        upload_date = items["snippet"]["publishedAt"]
        description = items["snippet"]["description"]
        comment_count = items["statistics"]["commentCount"]
    else:
        print("Video not found")
    return

def get_channel_id_or_username(channel_url):
    channel_type, identifier = channel_url.split('/')[-2:]
    return channel_type, identifier


def get_channel_id(api_key, channel_type, identifier):
    base_url = 'https://www.googleapis.com/youtube/v3'

    if channel_type == 'channel':
        return identifier

    if channel_type == 'user':
        search_url = f'{base_url}/search?part=snippet&type=channel&q={identifier}&key={api_key}'
        search_response = requests.get(search_url)
        search_data = json.loads(search_response.text)

        if 'items' not in search_data:
            print(f"Error: {search_data.get('error', 'Unknown error')}")
            return None

        return search_data['items'][0]['snippet']['channelId']

    return None


def get_video_descriptions(api_key, channel_id, max_results=5):
    base_url = 'https://www.googleapis.com/youtube/v3'

    # Get the channel's uploads playlist ID
    channel_url = f'{base_url}/channels?part=contentDetails&id={channel_id}&key={api_key}'
    channel_response = requests.get(channel_url)
    channel_data = json.loads(channel_response.text)

    if 'items' not in channel_data:
        print(f"Error: {channel_data.get('error', 'Unknown error')}")
        return None

    uploads_playlist_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Get the last n videos
    video_url = f'{base_url}/playlistItems?part=snippet&playlistId={uploads_playlist_id}&maxResults={max_results}&key={api_key}'
    video_response = requests.get(video_url)
    video_data = json.loads(video_response.text)

    # Retrieve the video descriptions
    video_descriptions = []
    for item in video_data['items']:
        video_descriptions.append(item['snippet']['description'])

    return video_descriptions


if __name__ == '__main__':
    # Replace this with the YouTube channel URL
    channel_url = 'https://www.youtube.com/user/tseries'
    channel_type, identifier = get_channel_id_or_username(channel_url)
    channel_id = get_channel_id(API_KEY, channel_type, identifier)

    if channel_id:
        descriptions = get_video_descriptions(API_KEY, channel_id)
        if descriptions:
            descriptions_list = [
                f'Description {i+1}:\n{desc.encode("utf-8", errors="ignore").decode("utf-8")}\n' for i, desc in enumerate(descriptions)]
            print(descriptions_list)
        else:
            print('No descriptions found.')
    else:
        print("Couldn't find the channel ID.")


def get_channel_descriptions(channel_url):
    # Replace this with the YouTube channel URL
    # channel_url = 'https://www.youtube.com/user/tseries'
    channel_type, identifier = get_channel_id_or_username(channel_url)
    channel_id = get_channel_id(API_KEY, channel_type, identifier)

    if channel_id:
        descriptions = get_video_descriptions(API_KEY, channel_id)
        if descriptions:
            descriptions_list = [
                f'Description {i+1}:\n{desc.encode("utf-8", errors="ignore").decode("utf-8")}\n' for i, desc in enumerate(descriptions)]

            print(descriptions_list)
            return descriptions_list
        else:
            print('No descriptions found.')
    else:
        print("Couldn't find the channel ID.")

# def print_video_info(url):



#     return None'

# def video_info_to_file(url):
    

# for url in youtube_channel_urls:
#     get_channel_descriptions(url)

    

# # Print the extracted information
# print(f"Likes: {likes}")
# print(f"Dislikes: {dislikes}")
# print(f"Channel Name: {channel_name}")
# print(f"Upload Date: {upload_date}")
# print(f"Description: {description}")
# print(f"Comment Count: {comment_count}")
