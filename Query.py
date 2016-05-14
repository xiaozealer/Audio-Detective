# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:05:52 2016

@author: parallels
"""

import numpy as np
import functions
from librosa.core import stft,load
from librosa.util import find_files

peak_filelist = find_files("database/peaks",ext="npy")
file_count = len(peak_filelist)
queryfile = "recording2.wav"
rec,sr = load(queryfile)
QUERY = np.abs(stft(rec,n_fft = 4096, hop_length = 512))
maximum_query = functions.find_peaks(QUERY,30)

query_size = QUERY.shape[1]
scores = np.zeros(file_count)
for i in range(file_count):
    filename = peak_filelist[i].split("/")[-1]
    print "comparing with " + filename
    maximum_spec = np.load(peak_filelist[i])
    spec_size = maximum_spec.shape[1]
    
    scores[i] = functions.matching_score(maximum_spec,maximum_query)
if np.max(scores)<20:
    print "nothing matched"
else:    
    matched_filename = find_files("database/audios", ext = "wav")[np.argmax(scores)]
    print "matched with:" + matched_filename.split("/")[-1]