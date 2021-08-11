from pydub import AudioSegment
import pydub
from pydub.silence import split_on_silence
import time

min_seconds = 2
max_seconds = 60
audios_directory = "audios" # Directorio de los archivos wav

def mp3_to_wav(audio_path):
	audio = AudioSegment.from_mp3(audio_path)
	audio = audio.set_channels(1)
	audio = audio.set_frame_rate(22050)
	audio.export("converted_audio.wav", format = "wav")


# Normalizar audios a un volumen especifico
def match_target_amplitude(aChunk, target_dBFS):
	change_in_dBFS = target_dBFS - aChunk.dBFS
	return aChunk.apply_gain(change_in_dBFS)


def split(audio_path):
	audio = AudioSegment.from_wav(audio_path)
	min_silence_len = 150 # Cortar el audio si hay 500 milisegundos de silencio
	silence_thresh = -40 # Defino silencio como cualquier sonido por debajo de -40 dBFS
	audio = pydub.effects.normalize(audio)

	chunks = split_on_silence (
		audio,
		min_silence_len = min_silence_len,
		silence_thresh = silence_thresh,
	)
	timestr = time.strftime("%Y%m%d_%H%M%S") # Fecha de hoy que vamos a utilizar para ponerle nombre unico a los archivos
	for i, chunk in enumerate(chunks):
		# Descartamos archivos muy largos o muy cortos
		if min_seconds*1000 < len(chunk) < max_seconds*1000:
			chunk = match_target_amplitude(chunk, -22.0)
			chunk.export(f"{audios_directory}/audio_{timestr}_{str(i)}.wav", format = "wav")

