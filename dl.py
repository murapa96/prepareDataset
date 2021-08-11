import youtube_dl


def download_from_youtube(yt_url, i):
    ydl_opts = {
        'format': 'bestaudio/best',
        "download_archive": "cache.txt",

        'outtmpl': 'downloads/' + str(i) + '.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        ],

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])
