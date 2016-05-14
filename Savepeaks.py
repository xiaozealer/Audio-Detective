# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:45:29 2016

@author: parallels
"""

import functions
from librosa.util import find_files
from librosa.core import load

audiofilelist = find_files("database/audios/",ext = "wav")
print "saving peaks...."
for audiofile in audiofilelist:
    y,sr = load(audiofile)
    filename = audiofile.split("/")[-1]+".npy" # -1 means the last name of the directory
    functions.save_maximum_array(y,filename)
    print "saved:" + filename