from glob import glob

from spleeter.separator import Separator

def vocals(audios, vocals_path):
    # Using embedded configuration.
    separator = Separator('spleeter:2stems')

    # Batch separation export.
    for audio_path in set(audios):
        separator.separate_to_file(audio_path, vocals_path)
        #separator.separate_to_file(audio_path, vocals_path, synchronous=False)
    # Wait for batch to finish.
    #separator.join()