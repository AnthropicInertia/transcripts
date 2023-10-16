import sys
import pytube

video_url = sys.argv[1]

video = pytube.YouTube(video_url)

print(video.title)

streams = video.streams.get_audio_only()

print("Downloading audio streams")
streams.download()