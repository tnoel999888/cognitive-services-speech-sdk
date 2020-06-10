from utils import run_ffmpeg
import sys
import os

# convert = sys.argv[2]

params = { 
'ar': 16000,
'ac': 1,
'ab': '16k',
'f': 'wav'
}

options = {'--verbose': 1}

input_file = sys.argv[1]

name = os.path.splitext(input_file)[0]
output_file = "{name}-conv.wav".format(name=name)

run_ffmpeg(input_file, output_file, params, options)
