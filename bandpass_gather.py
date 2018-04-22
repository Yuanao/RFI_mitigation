from __future__ import division
import numpy as np
import os
bp_gather=[]
#str1 = '201801/04'
#str1.replace ('201801/04', '201801/05')
#str2 = '180104_bandpass_'
#str2.replace('180104_bandpass_','180105_bandpass_')


os.system('find /public/home/yuanmao/FAST_bandpass/201801/02 -name "*0-1G*" -exec basename {} \; >/public/home/yuanmao/bandpass_gather/list/180102_bandpass_0-1G.list')

os.system('find /public/home/yuanmao/FAST_bandpass/201801/02 -name "*1-2G*" -exec basename {} \; >/public/home/yuanmao/bandpass_gather/list/180102_bandpass_1-2G.list')

os.system('sort -d /public/home/yuanmao/bandpass_gather/list/180102_bandpass_0-1G.list -o /public/home/yuanmao/bandpass_gather/list/180102_bandpass_0-1G.list')

os.system('sort -d /public/home/yuanmao/bandpass_gather/list/180102_bandpass_1-2G.list -o /public/home/yuanmao/bandpass_gather/list/180102_bandpass_1-2G.list')

#0-1G
for name1 in open ('/public/home/yuanmao/bandpass_gather/list/180102_bandpass_0-1G.list','r'):
    print name1
    name_1 = name1.strip('\n')
    bandpass = np.loadtxt('/public/home/yuanmao/FAST_bandpass/201801/02/''%s'%name_1)
    bp_gather.append(bandpass)

np.savetxt('/public/home/yuanmao/bandpass_gather/0-1G/201801/'"bandpass0-1G_201802.txt",bp_gather,fmt='%f')

#1-2G
for name2 in open ('/public/home/yuanmao/bandpass_gather/list/180102_bandpass_1-2G.list','r'):
    print name2
    name_2 = name2.strip('\n')
    bandpass = np.loadtxt('/public/home/yuanmao/FAST_bandpass/201801/02/''%s'%name_2) 
    bp_gather.append(bandpass)

np.savetxt('/public/home/yuanmao/bandpass_gather/1-2G/201801/'"bandpass1-2G_20180102.txt",bp_gather,fmt='%f')

