import yt_dlp

def download_audio(url, path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False