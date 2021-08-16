import sys
import os
from glob import glob

from tqdm import tqdm
from pydub import AudioSegment

from dl import download_from_youtube
from subs import extract_captions
from audio import normalize_audio

def dict_to_list(dict):
    lines_list = []
    for key, value in dict.items():
        text_line=key + "||" + value
        lines_list.append(text_line)
    return lines_list

def extract_id(file):
    file = file.split("/")[-1]
    return int(file.split(".")[0])

def download_vocals(urls, vocals_path="output", labels_path="labels"):
    from split import vocals

    print("Downloading songs from YouTube...")
    audios_paths = []
    subs_paths = []
    for i, val in enumerate(tqdm(urls)):
        new_audios_paths, new_subs_paths = download_from_youtube(val, i)
        audios_paths.extend(new_audios_paths)
        subs_paths.extend(new_subs_paths)
    print("Done ✔️")

    print("Extracting vocals...")
    vocals(audios_paths, vocals_path)
    print("Done ✔️")

    print("Creating subs labels...")
    id2sub = {extract_id(sub_file): sub_file for sub_file in subs_paths if "es" in sub_file}

    offset = 300/1000

    for i, captions in id2sub.items():
        labels = ""
        captions = extract_captions(captions)
        for (text, start, end) in captions:
            text = text.replace("\t"," ")
            labels += "\t".join([str(start+offset), str(end+offset), text]) + "\n"
        labels_file = os.path.join(labels_path,f"{i}.txt")
        with open(labels_file, 'w', encoding="utf-8") as file:
            file.write(labels)

    print("Done ✔️")

def parse_labels(filepath):
    with open(filepath,'r') as f:
        labels = [tuple(line.strip().split("\t")) for line in f.readlines()]
    return labels

def cut_audios(vocals_path, labels_path):
    vocals_paths = glob(os.path.join(vocals_path,"*/vocals.wav"))

    id2audio = {int(file.split("/")[-2]): file for file in vocals_paths}

    audios_transcript_content = ""
    for i, audio in id2audio.items():
        audios_transcript = {}
        audio = AudioSegment.from_file(audio, format="wav")
        label_path = os.path.join(labels_path,f"{i}.txt")

        for j, (start, end, text) in enumerate(parse_labels(label_path)):
            audio_path = f"audios/{i:04d}_{j:04d}.wav"
            start = int(float(start)*1000)
            end = int(float(end)*1000)
            chunk = audio[start:end]
            chunk = normalize_audio(chunk)
            chunk.export(audio_path, format = "wav")
            audios_transcript[audio_path] = text

        lines_list = dict_to_list(audios_transcript)
        audios_transcript_content+="\n".join(lines_list) + "\n"

    with open("transcript.csv", 'w', encoding="utf-8") as file:
        file.write(audios_transcript_content)

if __name__ == "__main__":
        command = sys.argv[1]
        if command == "download":
            urls_file = sys.argv[2]
            with open(urls_file,'r') as f:
                urls = [line.strip() for line in f.readlines()]
            download_vocals(urls)
        elif command == "cut":
            vocals_paths = sys.argv[2]
            labels_path = sys.argv[3]
            cut_audios(vocals_paths, labels_path)
