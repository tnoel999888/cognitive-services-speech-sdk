from utils import run_ffmpeg
import sys

params = { 'ar': 16000,
           'ac': 1,
           'ab': '16k',
           'f': 'wav'
         }

options = {'--verbose': 1}

# input_file = sys.argv[1]
# output_file = sys.argv[2]
# no_convert = sys.argv[3]

input_file = './test4.m4a'
output_file = './test4-conv.wav'

# if(no_convert):
#   return

run_ffmpeg(input_file, output_file, params, options)
