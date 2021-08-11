import youtube_dl


def download_from_youtube(yt_url, i):

    ydl_opts = {
        'format': 'bestaudio/best',
        "download_archive": "cache.txt",

        'outtmpl': f'downloads/{i}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        ],

    }
    playlist_opts = {
        'format': 'bestaudio/best',
        "download_archive": "cache.txt",

        'outtmpl': f'downloads/%(playlist_index)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        ],
    }
    if("list" in yt_url):
        with youtube_dl.YoutubeDL(playlist_opts) as ydl:
            ydl.download([yt_url])
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
