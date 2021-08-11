from spleeter.separator import Separator

# Using embedded configuration.
separator = Separator('spleeter:2stems')


def separate(inputs):
    # List of input to process.
    audio_descriptors = inputs

    # Batch separation export.
    for i in audio_descriptors:
        separator.separate_to_file(i, 'output/', synchronous=False)


    # Wait for batch to finish.
