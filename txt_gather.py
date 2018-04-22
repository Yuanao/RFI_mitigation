from __future__ import division
import numpy as np
import os
bp_gather=[]

#os.system('find /home/ym/FAST_rfi/FP201801/0-1G -name "*0-1G*" -exec basename {} \; >/public/home/yuanmao/bandpass_gather/list/171107_bandpass_0-1G.list')
#
#os.system('find /public/home/yuanmao/FAST_bandpass/201711/07 -name "*1-2G*" -exec basename {} \; >/public/home/yuanmao/bandpass_gather/list/171107_bandpass_1-2G.list')
#0-1G
for name1 in open ('/public/home/yuanmao/bandpass_gather/1801_bandpass_0-1G.list','r'):
    print name1
    name_1 = name1.strip('\n')
    bandpass = np.loadtxt('/public/home/yuanmao/bandpass_gather/0-1G/201801/''%s'%name_1)
    
    bp_gather.append(bandpass)
    np.set_printoptions(threshold=np.NaN)
#np.savetxt('/public/home/yuanmao/bandpass_gather/'"1801_bandpass_0-1G.txt",bp_gather,fmt='%s')

'''
with open('/public/home/yuanmao/bandpass_gather/1801_bandpass_0-1G.txt','r') as modifiled_txt:
    new_txt=modifiled_txt.read()
new_txt=new_txt.replace('[','')
new_txt=new_txt.replace(']','')
with open('/public/home/yuanmao/bandpass_gather/1801_bandpass_0-1G.txt','w') as modifiled_txt0:
    modifiled_txt0.write(new_txt)
'''
print bp_gather.shape

#print bp_gather
