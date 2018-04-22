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
secperday = 3600 * 24

for name in open('/public/home/yuanmao/shell/bandpass_20180110.list', 'r'):
    print name
    filename = '/public/home/data/psr/201801/10/' + name
    filename=filename.replace("\n","")
    hdulist = pyfits.open(filename)
    hdu0 = hdulist[0]
    hdu1 = hdulist[1]
    data1 = hdu1.data['data']
    header1 = hdu1.header
#    print hdu0.header
#    print hdu1.header
#    print data1.shape
#    
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
    tstart = "%.13f" % (Decimal(hdu0.header['STT_IMJD']) + Decimal(hdu0.header['STT_SMJD'] + tsamp * samppersubint * subintoffset )/secperday )
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

    basename = name[:name.find(".fits")]
    np.savetxt('/public/home/yuanmao/FAST_bandpass/201801/10/''%s' %basename + ".txt", data1, fmt='%d')
