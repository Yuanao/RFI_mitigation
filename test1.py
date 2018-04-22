import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#for name1 in open ('/home/ym/FAST_rfi/FP201801/0-1G/1801_bandpass_0-1G.list','r'):
#    print name1
#    name_1 = name1.strip('\n')
#    bandpass = np.loadtxt('/home/ym/FAST_rfi/FP201801/0-1G/''%s'%name_1)
#    data1=pd.DataFrame(bandpass)
#    basename = name_1[:name_1.find(".txt")]
#    data1.to_csv('/home/ym/FAST_rfi/FP201801/0-1G/''%s'%basename+".csv")
#    
#b = np.loadtxt(open("/home/ym/FAST_rfi/FP201801/0-1G/bandpass0-1G_20180102.csv","rb"),delimiter=",",skiprows=1,usecols=np.arange(1,4097))   
#b1 = np.loadtxt(open("/home/ym/FAST_rfi/FP201801/0-1G/bandpass0-1G_20180103.csv","rb"),delimiter=",",skiprows=1,usecols=np.arange(1,4097))     
#b2 = np.loadtxt(open("/home/ym/FAST_rfi/FP201801/0-1G/bandpass0-1G_20180131.csv","rb"),delimiter=",",skiprows=1,usecols=np.arange(1,4097))    
#print b.shape ,b1.shape,b2.shape

#for name1 in open ('/home/ym/FAST_rfi/FP201801/0-1G/csv.list','r'):
#    print name1
#    with open('/home/ym/FAST_rfi/FP201801/0-1G/bandpass0-1G_20180102.csv','ab') as f:
#        f.write(open('/home/ym/FAST_rfi/FP201801/0-1G/''%s'%name1,'rb').read())
    
#b = np.loadtxt('/public/home/yuanmao/bandpass_gather/1801_bandpass_0-1G.txt')    
data = np.loadtxt(open('/public/home/yuanmao/bandpass_gather/0-1G/201801_bandpass_0-1G.csv','rb'),delimiter=",",skiprows=0)
print data.shape   

fig = plt.figure()
ax2 = fig.add_subplot(1, 1,1)
norm = matplotlib.colors.Normalize(vmin=0, vmax=30e6)
cmap = matplotlib.cm.jet
ticks = ax2.set_xticks([0,6870,13740,20610,27480,34350])
labels = ax2.set_xticklabels([0,100,200,300,400,500])
ticks = ax2.set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000])
labels = ax2.set_yticklabels([0,125, 250, 375, 500,625,750,875,1000])
plt.ylabel('frequency(MHz)')
plt.xlabel('time(h)')
im1 = plt.imshow(data.T,aspect='auto',origin='lower',cmap = cmap,norm=norm)
cbar = fig.colorbar(im1, ticks=[0, 15e6, 30e6])

plt.savefig("/public/home/yuanmao/1.png",dpi=800)
