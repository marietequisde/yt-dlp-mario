import yt_dlp

URLS = ['https://www.youtube.com/watch?v=YE7VzlLtp-4']

dw = yt_dlp.YoutubeDL()
dw.download(URLS)