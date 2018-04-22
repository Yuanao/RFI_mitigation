from __future__ import division
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
import pywt
from scipy import interpolate
import pandas as pd

output_nos=[]
output_bandpass=[]
def smooth(sig,threshold = 3, level=6, wavelet='db8'):
        sigma = sig.std()
        dwtmatr = pywt.wavedec(data=sig, wavelet=wavelet, level=level)
        denoised = dwtmatr[:]
        denoised[1:] = [pywt.threshold(i, value=threshold*sigma, mode='soft') for i in dwtmatr[1:]]
        smoothed_sig = pywt.waverec(denoised, wavelet, mode='sp1')[:sig.size]
        noises = sig - smoothed_sig
        return smoothed_sig, noises

bandpass = np.loadtxt(open("/public/home/yuanmao/bandpass_gather/0-1G/4mon_bandpass_0-1G.csv","rb"),delimiter=",",skiprows=0)
bandpass_copy=bandpass
idxbad_chan=[]
inf=float('inf')
#bandpass = np.loadtxt('/ssd/yuanmao/data_test/5bandpass.txt')
print("bandpass.shape",bandpass.shape)
print("bandpass[:,0].shape",bandpass[:,0].shape)
idxgood_num_=[]
idxbad_chan_=[]
nos_pca=[]
for i in range(len(bandpass[:,0])):
    copy_=bandpass[i]
#    copy1=np.delete(copy_,np.s_[0:1000],axis=0)
#    copy=np.delete(copy1,np.s_[2500:3097],axis=0)
#    sig,nos = smooth(copy)
    sig,nos = smooth(copy_)
    output_nos.append(nos)
#    idxarr = np.arange(copy.size)
    idxarr = np.arange(copy_.size)
    tck = interpolate.splrep(idxarr,sig)
#    xnew=np.arange(1,2501,1)
    xnew=np.arange(1,4097,1)
    y = interpolate.splev(xnew, tck)
    y2 = abs((y-copy_)/y)
    y2[abs(y2)==inf]=0
    idxgood = idxarr[y2<0.3]
    idxbad = idxarr[y2>=0.3]
    a=idxgood.size
    idxgood_num_.append(a)
#    copy[idxgood]=0
#    copy[idxbad]=1
#    idxbad_chan_.append(copy)
    nos_pca_=copy_ - y
    nos_pca.append(nos_pca_)
#nos=pd.DataFrame(output_nos)
output_nos_pca=pd.DataFrame(nos_pca)
'''
nos.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/4mon_nos_0-1G.csv',index=False,na_rep='NaN',header=False)
'''
output_nos_pca.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/4mon_nos_pca_0-1G.csv',index=False,na_rep='NaN',header=False)

'''
nos_arr = np.loadtxt(open("/public/home/yuanmao/bandpass_gather/0-1G/4mon_nos_0-1G.csv","rb"),delimiter=",",skiprows=0)
print ('nos_arr',nos_arr.shape)
#

#
avg_nos0=nos_arr.sum(axis=0)/len(nos_arr[:,0])
avg_nos=pd.DataFrame(avg_nos0)
avg_nos.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/4mon_avg_nos_0-1G.csv',index=False,na_rep='NaN',header=False)
print ("avg_nos.shape",avg_nos.shape)
#

idxgood_num=pd.DataFrame(idxgood_num_)
idxgood_num.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/4mon_idxbad_num.csv',index=False,na_rep='NaN',header=False)
print('idxgood',idxgood.shape)
#
idxbad_chan=pd.DataFrame(idxbad_chan_)
print('idxbad_chan',idxbad_chan.shape)
idxbad_chan.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/4mon_idxbad_chan.csv',index=False,na_rep='NaN',header=False)
idxbad_chan_arr=np.loadtxt(open('/public/home/yuanmao/bandpass_gather/0-1G/4mon_idxbad_chan.csv','rb'),delimiter=",",skiprows=0)
idxbad_chan_stat_=idxbad_chan_arr.sum(axis=0)
idxbad_chan_stat=pd.DataFrame(idxbad_chan_stat_)
idxbad_chan_stat.to_csv('/public/home/yuanmao/bandpass_gather/0-1G/4mon_idxbad_chan_stat.csv',index=False,na_rep='NaN',header=False)
print(idxbad_chan_stat.shape)
#
'''
