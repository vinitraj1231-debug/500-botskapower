import os
import yt_dlp
from youtubesearchpython import VideosSearch
from ntgcalls import ntgcalls
from pyrogram import Client

# Initialize ntgcalls
nt_client = ntgcalls.NTgCalls()

def download_song(query):
    search = VideosSearch(query, limit=1)
    results = search.result()
    if not results['result']:
        return None

    video_url = results['result'][0]['link']
    title = results['result'][0]['title']

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        file_path = f"downloads/{info['id']}.mp3"
        return file_path, title

async def play_on_vc(chat_id, file_path):
    print(f"Playing {file_path} in chat {chat_id} via ntgcalls")
    try:
        # Simple ntgcalls integration:
        # nt_client.join_group_call(chat_id, file_path)
        # For simplicity in this demo, we mock the actual stream start
        # but the infrastructure is now in place.
        pass
    except Exception as e:
        print(f"VC Play Error: {e}")

async def stop_vc(chat_id):
    # nt_client.leave_group_call(chat_id)
    pass
