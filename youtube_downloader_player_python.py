# -*- coding: utf-8 -*-
"""Youtube downloader player python project(6-jan-2024).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ir3aFfOtV69JH0Yb_hJx0V_ezQEoTlsM
"""

!pip install yt-dlp  # Install yt-dlp for downloading YouTube videos

import yt_dlp
from IPython.display import Video, display
import glob
import os

def fix_url(url):
    """Convert YouTube Shorts URL to regular watch URL."""
    if "/shorts/" in url:
        return url.replace("/shorts/", "/watch?v=")
    return url

def download_and_play_video(url):
    # Fix Shorts URL if needed
    url = fix_url(url)

    # Remove previously downloaded files
    for file in glob.glob("downloaded_video.*"):
        os.remove(file)  # Delete old video file

    ydl_opts = {
        'format': 'mp4',  # Force MP4 format for better compatibility
        'outtmpl': 'downloaded_video.mp4',  # Save as downloaded_video.mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n Video downloaded successfully!")

    # Ensure the file exists
    video_file = "downloaded_video.mp4"
    if not os.path.exists(video_file):
        print(" Error: No video file found.")
        return

    # Display the new video inside Colab
    print("\n Now Playing Video Below ")
    display(Video(video_file, embed=True, width=600))

# Enter YouTube Video URL and download/play
url = input(" Enter YouTube Video or Shorts URL: ")
download_and_play_video(url)