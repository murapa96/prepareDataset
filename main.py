import audio
import dl
import split
import transcriber

urls = [
    "https://www.youtube.com/watch?v=hJ7EymoaYDY",
    "https://www.youtube.com/watch?v=C45yKO8MOi8"
]

completeFiles = [

]

def run():
    for i,val in enumerate(urls):
        global completeFiles
        dl.download_from_youtube(val, i)
        completeFiles.append("downloads/" + str(i) +".mp3")
    print(completeFiles)
    split.separate(completeFiles)
    split.separator.join()
    for i,val in enumerate(completeFiles):
        audio.split(f"output/{i}/vocals.wav")

    transcriber.transcribe_audios()


run()
