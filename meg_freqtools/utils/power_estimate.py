import os
import numpy as np

def

def auto_cycle(freq_bins,duration):
    """
    freq_bins : list or numpy array
    duration : means epoch time in second
    """
    cpoint = np.where(freq_bins < 8)[0][-1] ## find the last frequency that is smaller than 8 Hz
    cycle_slow_freq = duration * freq_bins[:cpoint]

    if cycle_slow_freq.min() 

    cycle_array = np.zeros_like(freq_bins)
    cycle_array[cpoint + 1:] = freq_bins[cpoint + 1:] // 2

def freq_window():
    