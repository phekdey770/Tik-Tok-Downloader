import asyncio
from tiktokdl.download_post import get_post

async def download_video(video_url, save_path):
    try:
        await get_post(video_url, savepath=save_path)
        print(f"Downloaded {video_url} successfully.")
    except Exception as e:
        print(f"Failed to download {video_url}. Error: {str(e)}")

async def main():
    # List of TikTok video URLs
    video_urls = [
        "https://www.tiktok.com/@longmanin/video/7319063274476047617",
        "https://www.tiktok.com/@longmanin/video/7167261701400792346",
        "https://www.tiktok.com/@longmanin/video/7146516057858018586",
        "https://www.tiktok.com/@longmanin/video/7388822110220602632",
        "https://www.tiktok.com/@longmanin/video/7385164696434920711",
        "https://www.tiktok.com/@longmanin/video/7385163889828285714"
    ]
    
    # Path to save the downloaded videos
    save_path = r"D:/TEST 2/Data/Tik Tok"

    # Download each video asynchronously
    tasks = []
    for url in video_urls:
        tasks.append(download_video(url, save_path))
    
    # Run tasks asynchronously
    await asyncio.gather(*tasks)

# Run the asyncio event loop to start downloading
if __name__ == "__main__":
    asyncio.run(main())
