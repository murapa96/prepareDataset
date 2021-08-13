import datetime
import time

import webvtt

def time2miliseconds(time_string):
    x = time.strptime(time_string,'%H:%M:%S.%f')
    return datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()*1000

def extract_captions(vtt_path):
    captions = webvtt.read(vtt_path)

    result = []
    for caption in captions:
        start = time2miliseconds(caption.start)
        end = time2miliseconds(caption.end)        
        result.append((caption.text, start, end))
    return result