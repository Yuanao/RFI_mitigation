import numpy as np  
#import pyfits
from pylab import *
import astropy.io.fits as pyfits
import os
import datetime
import time
import sys 
from decimal import Decimal
from pylab import *
import pandas as pd

secperday = 3600 * 17

os.system('find /public/home/data/psr/201710/20 -name "*drifting*" -exec basename {} \; >/public/home/yuanmao/shell/bandpass_20171020.list')

os.system('sort -d /public/home/yuanmao/shell/bandpass_20171020.list -o /public/home/yuanmao/shell/bandpass_20171020.list')
for name in open('/public/home/yuanmao/shell/bandpass_20171020.list', 'r'):
    print name
    filename = '/public/home/data/psr/201710/20/' + name
    filename=filename.replace("\n","")
    try:
        hdulist = pyfits.open(filename)
        hdu0 = hdulist[0]
        hdu1 = hdulist[1]
        data1 = hdu1.data['data']
        header1 = hdu1.header
        fchannel = hdulist['SUBINT'].data[0]['DAT_FREQ']
        fch1 = fchannel[0]
        obsfreq = hdu0.header['OBSFREQ']
        obsnchan = hdu0.header['OBSNCHAN']
        obsbw = hdu0.header['OBSBW']
        fmin = obsfreq - obsbw/2.
        fmax = obsfreq + obsbw/2.
        nf = obsnchan
        df = hdu1.header['CHAN_BW']
        tsamp = hdu1.header['TBIN']
        nsubint = hdu1.header['NAXIS2']
        samppersubint = int(hdu1.header['NSBLK'])
        nsamp = nsubint * samppersubint
        sourename = hdu0.header['SRC_NAME']
        ra = hdu0.header['RA']
        dec = hdu0.header['DEC']
        subintoffset = hdu1.header['NSUBOFFS']
        tstart = "%.17f" % (Decimal(hdu0.header['STT_IMJD']) + Decimal(hdu0.header['STT_SMJD'] + tsamp * samppersubint * subintoffset )/secperday )
        nbits = hdu0.header['BITPIX']
        header = hdu0.header + hdu1.header
        dtype = ''
        a,b,c,d,e = data1.shape
        if c > 1:
                 data = data1[:,:,0,:,:].squeeze().reshape((-1,d))
        else:
        
                 data = data1.squeeze().reshape((-1,d))
        l, m = data.shape
        data = data.reshape(l/64, 64, d).sum(axis=1)
        data1 = np.sum(data,axis=0)
#    plot(data1)
#    show()
    except:
            print ('Error')
    else:
         basename = name[:name.find(".fits")]
#         np.savetxt('/public/home/yuanmao/FAST_bandpass/201710/17/''%s' %basename + ".txt", data1, fmt='%d')
#         data17=np.loadtxt('/public/home/yuanmao/FAST_bandpass/201717/17/''%s' %basename + ".txt")
         data_reshape=data1.reshape(data1.size/4096,4096)
         data17=pd.DataFrame(data_reshape)
         data17.to_csv('/public/home/yuanmao/FAST_bandpass/201710/20/''%s' %basename + ".csv",index=False,na_rep='NaN',header=False)
