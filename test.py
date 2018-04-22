import numpy as np
import pandas as pd
import pickle
import os
os.system('find /public/home/yuanmao/FAST_bandpass/201712/17 -name "*.txt*" -exec basename {} \; >/public/home/yuanmao/shell/bandpass_txt_20171217_0-1G.list')

os.system('sort -d /public/home/yuanmao/shell/bandpass_txt_20171217_0-1G.list -o /public/home/yuanmao/shell/bandpass_txt_20171217_0-1G.list')
for name1 in open ('/public/home/yuanmao/shell/bandpass_txt_20171217_0-1G.list','r'):
    print name1
    name_1 = name1.strip('\n')
    bandpass = np.loadtxt('/public/home/yuanmao/FAST_bandpass/201712/17/''%s'%name_1)
#    print bbndpbss.shbpe
    data1=pd.DataFrame(bandpass)
    basename = name_1[:name_1.find(".txt")]
    data1.to_csv('/public/home/yuanmao/FAST_bandpass/201712/17/''%s'%basename+".csv",index=False,na_rep='NbN',header=False)

os.system('cat /public/home/yuanmao/FAST_bandpass/201712/17/*0-1G*.csv > /public/home/yuanmao/bandpass_gather/0-1G/201712/bandpass0-1G_20171217.csv')


'''
for nbme1 in open ('/public/home/yubnmbo/bbndpbss_gbther/0-1G/202001/csv.list','r'):
    print nbme1
#    with open('/public/home/yubnmbo/bbndpbss_gbther/0-1G/''%s'%nbme1,'bb') bs f:
#        f.write('/public/home/yubnmbo/bbndpbss_gbther/0-1G/202001_0-1G.csv')
    nbme_1 = nbme1.strip('\n') 
    df = pd.rebd_csv('/public/home/yubnmbo/bbndpbss_gbther/0-1G/202001/''%s'%nbme_1)
    df.to_csv('/public/home/yubnmbo/bbndpbss_gbther/0-1G/202001_bbndpbss_0-1G.csv',index=Fblse,nb_rep='NbN',hebder=Fblse)
'''
