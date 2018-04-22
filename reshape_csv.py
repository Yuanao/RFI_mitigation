import numpy as np
import os
import pandas as pd
for name in open('/public/home/yuanmao/test/csv.list','r'):
    print name
    filename = name.replace("\n","")
    data=np.loadtxt(open('/public/home/yuanmao/test/''%s'%filename,'rb'),delimiter=',',skiprows=0)
    data_reshape = data.reshape(data.size/4096,4096)
    print data_reshape.shape
    data_reshape_csv=pd.DataFrame(data_reshape)
    data_reshape_csv.to_csv('/public/home/yuanmao/test/''%s'%filename,index=False,na_rep='NaN',header=False)
