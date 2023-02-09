import re
from pytube import YouTube

urls = []
while True:
    url = input("Enter the URL of the YouTube video (or 'q' to quit): ")
    if url == 'q':
        break
    urls.append(url)

for url in urls:
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    file_name = re.sub(r'[^\w\-_\. ]', '_', yt.title) + ".mp3"
    stream.download(filename=file_name)
