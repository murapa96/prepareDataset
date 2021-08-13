from glob import glob

import youtube_dl

dst_folder = "downloads"

def download_from_youtube(yt_url, i):

    ydl_opts = {
        'format': 'bestaudio/best',
        "download_archive": "cache.txt",
        "writesubtitles": True,
        "allsubtitles": True,
        "subtitlesformat": "vtt", # ('best', 'srv1', 'srv2', 'srv3', 'ttml', 'vtt')
        #"subtitleslang": null, #https://github.com/ytdl-org/youtube-dl/blob/5208ae92fc3e2916cdccae45c6b9a516be3d5796/test/parameters.json
        'outtmpl': f'{dst_folder}/{i}.%(ext)s',
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

    audios_paths = glob(f"{dst_folder}/*.mp3")
    subs_paths = glob(f"{dst_folder}/*.vtt")

    return audios_paths, subs_paths