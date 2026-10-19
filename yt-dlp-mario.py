import yt_dlp
from spotify_to_ytmusic import search_track, transfer_playlist, update_playlist

def main():
    end = 0
    while (end != '1'):
        url = input("Video or playlist: ")
        if (url.__contains__("spotify")):
            if (url.__contains__("open.spotify.com/playlist")):
                playlistId = transfer_playlist(url, privacy="UNLISTED")
                url = f"https://music.youtube.com/playlist?list={playlistId}"
            else:
                url = search_track(url)
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