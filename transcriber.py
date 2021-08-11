import speech_recognition as sr
import json
import os
from tqdm import tqdm
audios_directory = "audios"
def transcribe_audios():
    # Incializar speech recognizer
    r = sr.Recognizer()

    # Crear un diccionario vacio, donde la clave va a ser
    # El nombre del archivo wav, y el valor es su transcripcion
    audios_transcript={}
    filenames = os.listdir(audios_directory)
    for filename in tqdm(filenames):
      try:
        audio=os.path.join(audios_directory, filename)
        with sr.AudioFile(audio) as source:
            audio_text = r.listen(source)
            text = r.recognize_google(audio_text, language = "es-ES")
            audios_transcript["audios/" + filename]=text #agregar la transcripcion al diccionario
      except:
        pass

    # Transformar el diccionario en una lista de transcripciones
    def dict_to_list(dict):
      lines_list=[]
      for key, value in dict.items():
        text_line=key + "||" + value
        lines_list.append(text_line)
      return lines_list

    lines_list = dict_to_list(audios_transcript)

    # Transformar esa lista en lineas de texto
    audios_transcript_file="\n".join(lines_list)

    # Imprimir ese texto en un archivo de texto
    # (Para eso yo primero cree a mano un archivo vacio llamado "transcript.csv")
    with open('transcript.csv', 'w', encoding="utf-8") as file:
         file.write(audios_transcript_file)