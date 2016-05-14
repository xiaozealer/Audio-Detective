# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:30:17 2016

@author: parallels
"""

import numpy as np
from scipy.ndimage.filters import maximum_filter
from librosa.core import stft

def find_peaks(M,size):
    maximum = maximum_filter(M,size)
    threshold = np.max(M)* 0.01
    maximum[maximum<threshold] = -1.0
    return M == maximum

def matching_score(maximum_spec,maximum_query):
    spec_size = maximum_spec.shape[1]
    query_size = maximum_query.shape[1]

    overlap = np.zeros(spec_size-query_size)

    for t in range(spec_size - query_size):
        spec_snip = maximum_spec[:,t:t+query_size]
        overlap[t] = np.sum(spec_snip & maximum_query)
    return np.max(overlap)
    
def save_maximum_array(y,filename):
    D = np.abs(stft(y,n_fft = 4096,hop_length = 512))
    maximum = find_peaks(D,50)
    np.save("database/peaks/%s" % filename,maximum)