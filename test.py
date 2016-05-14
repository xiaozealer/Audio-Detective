# -*- coding: utf-8 -*-
"""
Created on Sat May  7 13:51:42 2016

@author: parallels
"""
import numpy as np
from librosa.core import load,stft
import matplotlib.pyplot as plt
from librosa.display import specshow
import functions
 #from scipy.spatial.distance import euclidean

y,sr = load("wiwym.wav")
rec,sr = load("recording.wav")
y = y[:sr*30]

 spec = np.abs(stft(y,n_fft = 4960,hop_length = 512))
    query = np.abs(stft(rec,n_fft = 4960,hop_length = 512))
    maximum_spec = find_peak(spec,30)
    maximum_query = find_peak(query,30)

plt.plot(overlap)