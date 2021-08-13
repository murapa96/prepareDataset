from glob import glob

from spleeter.separator import Separator

def vocals(inputs):
    # Using embedded configuration.
    separator = Separator('spleeter:2stems')

    # List of input to process.
    audio_descriptors = inputs

    # Batch separation export.
    for i in audio_descriptors:
        separator.separate_to_file(i, 'output/', synchronous=False)
    # Wait for batch to finish.
    separator.join()

    return glob("output/*/vocals.wav")