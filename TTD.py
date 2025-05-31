import os
import requests
from TikTokApi import TikTokApi

def download_video(video_url, save_path):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print(f"Failed to download video: {video_url}")

def download_all_videos(username):
    # Initialize the TikTokApi instance
    with TikTokApi() as api:
        user_videos = api.user(username=username).videos(count=1000)

        # Create a directory to save the videos
        if not os.path.exists(username):
            os.makedirs(username)

        for idx, video in enumerate(user_videos):
            video_url = video.as_dict['video']['downloadAddr']
            save_path = os.path.join(username, f"{username}_video_{idx}.mp4")
            print(f"Downloading {video_url} to {save_path}")
            download_video(video_url, save_path)

if __name__ == "__main__":
    username = "longmanin"  # Replace with the TikTok username
    download_all_videos(username)
