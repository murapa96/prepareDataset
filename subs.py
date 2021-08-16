import datetime
import time

import webvtt

def time2seconds(time_string):
    x = time.strptime(time_string,'%H:%M:%S.%f')
    return datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

def extract_captions(vtt_path):
    captions = webvtt.read(vtt_path)

    result = []
    for caption in captions:
        start = time2seconds(caption.start)
        end = time2seconds(caption.end)        
        result.append((caption.text.replace("\n",". "), start, end))
    return result