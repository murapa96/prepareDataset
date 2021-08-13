import sys

from tqdm import tqdm
from pydub import AudioSegment

from dl import download_from_youtube
from split import vocals
from subs import extract_captions
from audio import normalize_audio

audios_directory = "audios"

def dict_to_list(dict):
  lines_list=[]
  for key, value in dict.items():
    text_line=key + "||" + value
    lines_list.append(text_line)
  return lines_list


def extract_id(file):
    file = file.split("/")[-1]
    return int(file.split(".")[0])

def run(urls, output_csv="transcript.csv"):

    print("Downloading songs from YouTube...")
    audios_paths = []
    subs_paths = []
    for i, val in enumerate(tqdm(urls)):
        new_audios_paths, new_subs_paths = download_from_youtube(val, i)
        audios_paths.extend(new_audios_paths)
        subs_paths.extend(new_subs_paths)
    print("Done ✔️")

    print("Extracting vocals...")
    vocals_paths = vocals(audios_paths)
    print("Done ✔️")

    print("Creating the dataset...")
    id2audio = {int(file.split("/")[-2]): file for file in vocals_paths}
    id2sub = {extract_id(sub_file): sub_file for sub_file in subs_paths if "es" in sub_file}
    print(id2sub)

    audios_transcript={}

    for i, audio in id2audio.items():
        start_offset = 300
        end_offset = 500
        captions = extract_captions(id2sub[i])        
        audio = AudioSegment.from_file(audio, format="wav")
        for (text, start, end) in captions:
            chunk = audio[start+start_offset:end+end_offset]
            chunk = normalize_audio(chunk)
            audio_path = f"audios/{text}.wav"
            audios_transcript[audio_path]=text
            chunk.export(audio_path, format = "wav")

    lines_list = dict_to_list(audios_transcript)
    audios_transcript_file="\n".join(lines_list)

    with open(output_csv, 'w', encoding="utf-8") as file:
        file.write(audios_transcript_file)

    print("Done ✔️")


if __name__ == "__main__":
    try:
        urls_file = sys.argv[1]
    except:
        print("Try something like: 'python main.py urls.txt'")
    with open(urls_file,'r') as f:
        urls = [line.strip() for line in f.readlines()]
    run(urls)
