# -*- coding: utf-8 -*-
"""
Created on Thu May 20 05:40:33 2021
https://www.journaldev.com/40720/python-script-to-download-youtube-videos
@author: Ovindu Wijethunge
"""

from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=ElFM9Z48riA'
 
yt_obj = YouTube(youtube_video_url)

for stream in yt_obj.streams:
    print(stream)
    
filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
filters.get_highest_resolution()
filters.get_lowest_resolution()   

filters.get_highest_resolution().download()