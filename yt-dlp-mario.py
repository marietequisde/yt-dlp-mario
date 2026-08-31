import yt_dlp

def main():
    end = 0
    while (end != '1'):
        url = input("Video or playlist: ")
        format = input("Audio(1), Video(2): ")
        if (format == '1'):
            download_audio(url)
        elif (format == '2'):
            download_video(url)

        end = input("(1) to end: ")    

def download_audio(urls):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    dw = yt_dlp.YoutubeDL(ydl_opts)
    dw.download(urls)

def download_video(urls):
    ydl_opts = {
        'format': 'bv+ba/b',
        'merge_output_format': 'mp4'
    }

    dw = yt_dlp.YoutubeDL(ydl_opts)
    dw.download(urls)

if __name__ == "__main__":
    main()