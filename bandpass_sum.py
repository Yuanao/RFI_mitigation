from __future__ import division
import numpy as np
import os
bp_gather=[]
for root,dirs,files in os.walk('/public/home/yuanmao/FAST_bandpass/201801/02/'):
    for name in files:
        bandpass = np.loadtxt('/public/home/yuanmao/FAST_bandpass/201801/02/%s'%name)
        bp_gather.append(bandpass)

np.savetxt('/public/home/yuanmao/bandpass_sum/0-1G''%s'%bandpass_20180102.txt,bp_gather,fmt='%f')
