import speech_recognition as sr
import json
import os
import glob
from tqdm import tqdm

# Transformar el diccionario en una lista de transcripciones
def dict_to_list(dict):
  lines_list=[]
  for key, value in dict.items():
    text_line=key + "||" + value
    lines_list.append(text_line)
  return lines_list


def transcribe_audios(audios_directory, output_csv ='transcript.csv'):
  # Incializar speech recognizer
  r = sr.Recognizer()

  # Crear un diccionario vacio, donde la clave va a ser
  # El nombre del archivo wav, y el valor es su transcripcion
  audios_transcript={}
  filenames = glob.glob(os.path.join(audios_directory,"*"))

  for audio_path in tqdm(filenames):
    try:
      with sr.AudioFile(audio_path) as source:
          audio_text = r.listen(source)
          text = r.recognize_google(audio_text, language = "es-ES")
          audios_transcript[audio_path]=text #agregar la transcripcion al diccionario
    except Exception as e:
      print(e)

  lines_list = dict_to_list(audios_transcript)

  # Transformar esa lista en lineas de texto
  audios_transcript_file="\n".join(lines_list)

  # Imprimir ese texto en un archivo de texto
  with open(output_csv, 'w', encoding="utf-8") as file:
       file.write(audios_transcript_file)