import os
from tqdm import tqdm
import audio
import dl
import split
import transcriber

urls = [
   "https://www.youtube.com/watch?v=BZNtxpO9DoA&list=PLzB6GWA5mO6VPA7YDMqosoVbM-RTsEMr1"
]


def run():
    for i,val in enumerate(tqdm(urls)):
        dl.download_from_youtube(val, i)
    filenames = os.listdir("downloads/")
    split.separate(map(lambda x: "downloads/" + x,filenames))
    split.separator.join()
    filenames = os.listdir("output/")

    for i,val in enumerate(tqdm(filenames)):
        audio.split(f"output/{i}/vocals.wav")

    transcriber.transcribe_audios()


run()
