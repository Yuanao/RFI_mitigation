import numpy as np 
#import pyfits
import astropy.io.fits as pyfits
import os
import datetime
import time
import sys

#filename = sys.argv[1]
for filename in open('/public/home/yuanmao/20171203fits.list', 'r'):
    print filename
    name = filename.strip()
    hdulist = pyfits.open('/public/home/data/psr/201712/03/'+ name)
    hdu0 = hdulist[0]
    hdu1 = hdulist[1]
    header1 = hdu1.header
    obsfreq = hdu0.header['OBSFREQ']
    obsnchan = hdu0.header['OBSNCHAN']
    obsbw = hdu0.header['OBSBW']
    minfreq = float(obsfreq - obsbw/2.)
    maxfreq = float(obsfreq + obsbw/2.)
    nf = obsnchan
    df = hdu1.header['CHAN_BW']
    tsamp = hdu1.header['TBIN']
    nsubint = hdu1.header['NAXIS2']
    samppersubint = int(hdu1.header['NSBLK'])
    nsamp = nsubint * samppersubint
    sourename = hdu0.header['SRC_NAME']
    ra = hdu0.header['RA']
    dec = hdu0.header['DEC']
    tstart = float("%d.%d" % (hdu0.header['STT_IMJD'], hdu0.header['STT_SMJD']))
    nbits = hdu0.header['BITPIX']
    header = hdu0.header + hdu1.header
    dtype = ''
    duration = tsamp * nsamp
    
    data = hdu1.data['data']
    data = data.mean(axis=2)
    data = data.squeeze()
    l,m,n = data.shape
    data = data.reshape(l*m,n)
    m,n = data.shape
    data = data.reshape(m/4096, 4096, n)
    data = data.mean(axis=1)
#    print data.shape
    sumdata=[]
    sumdata.append(data)


from pylab import *
imshow(data.T, aspect='auto', origin='low', extent=(0., float(duration), float(minfreq), float(maxfreq)))
xlabel('t (s)')
ylabel('frequency (MHz)')
show()


    
    
    
    
    
    
    
    
    
    
    


