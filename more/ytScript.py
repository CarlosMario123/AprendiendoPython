from pytube import Search
from yt_dlp import YoutubeDL
import time

def download_audio(video_url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'retries': 3,
        'sleep_interval_requests': 10,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def search_and_download(song_name, output_path='.'):
    search = Search(song_name)
    video = search.results[0]  # Get the first result
    video_url = video.watch_url
    print(f"Downloading: {video.title}")
    download_audio(video_url, output_path)

def download_songs(song_list, output_path='.'):
    for song in song_list:
        try:
            search_and_download(song, output_path)
        except Exception as e:
            print(f"Failed to download {song}: {e}")
            continue

if __name__ == "__main__":
    songs = [
        "mirame jenni rivera",
        "cuando abras los ojos jenni rivera",
        "por un amor jenni rivera",
        "ahora que estuviste lejos jenni rivera",
        "como tu decidas jenni rivera",
        "ahora vengo a verte jenni rivera",
        "jure que nunca volver jenni rivera",
        "no me hagas menos vicente fernadez",
        "con la misma tijera vicente fernandez",
        "si alcazo vulves vicente fernandez",
        "le pese quien le pese vicente fernandez",
        "adorado tormento vicente fernandez",
        "le pese quien le pese vicente fernandez",
        "volver volver vicente fernandez",
        "la derrota vicente fernandez",
       
        # Add more songs as needed
    ]
    output_path = 'utils'
    download_songs(songs, output_path)
