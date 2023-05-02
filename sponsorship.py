class video:
    def __init__(self, video_name, date, channel_name, view_count, sponsor, sponsor_link):
        self.video_name = video_name
        self.date = date
        self.channel_name = channel_name
        self.view_count = view_count
        self.sponsor = [sponsor, sponsor_link]
    

    def __str__(self):
        """
        -------------------------------------------------------
        returns a string version of a video in the format
        Video name: video-name
        Date posted: date
        Channel: channel-name
        View count: view-count
        Sponsor of this video: sponsor
        Use: boolean = comp_link(string)
        -------------------------------------------------------
        
        Returns:
            A formatted version of the video data (str)
        -------------------------------------------------------
        """
        string = f"""Video Name:{self.video_name}\nDate Posted:{self.date}\nChannel:{self.channel_name}\nView Count:{self.view_count}\nSponsor of This Video:{self.sponsor[0]}\nLink to the sponsor:{self.sponsor[1]}"""
        return string
    
# v = video("hi", "2023-02-28", "sarahdoesstuff" , 100000, "NordVPN", "https://nordvpn.com/sarah")

# print(v)
        
    