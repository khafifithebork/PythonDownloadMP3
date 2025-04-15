import os
import yt_dlp

def download_audio(youtube_url, temp_dir):
    """
    Downloads audio from a YouTube video.
    Args:
        youtube_url (str): The URL of the YouTube video.
        temp_dir (str): Directory where the file should be saved.
    Returns:
        str: The file path of the downloaded audio file.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        file_path = ydl.prepare_filename(info_dict).replace(".webm", ".mp3")
        return file_path

