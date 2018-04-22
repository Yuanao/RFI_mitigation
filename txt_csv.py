import numpy as np
import pandas as pd
import pickle
import os

os.system('find /public/home/yuanmao/FAST_bandpass/201711/01 -name "*drifting*" -exec basename {} \; >/public/home/yuanmao/shell/bandpass_txt_20171101.list')

os.system('sort -d /public/home/yuanmao/shell/bandpass_20171101.list -o /public/home/yuanmao/shell/bandpass_20171101.list')
for name1 in open ('/public/home/yuanmao/bandpass_gather/1801_bandpass_0-1G.list','r'):
    print name1
    name_1 = name1.strip('\n')
    bandpass = np.loadtxt('/public/home/yuanmao/bandpass_gather/0-1G/201801/''%s'%name_1)
    print bandpass.shape
    data1=pd.DataFrame(bandpass)
    basename = name_1[:name_1.find(".txt")]
    data1.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/201801/''%s'%basename+".csv",index=False,na_rep='NaN',header=False)
