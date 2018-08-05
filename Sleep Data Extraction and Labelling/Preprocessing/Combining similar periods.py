# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:01:40 2018
Week8: Combining different variables with similar periodicity 
### The main objective of this program is to select those sensors of similar periodicity and apply TICC to identify different clusters within those time series for each periodicity.
@author: Vignesh
"""
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    '''
    direct_data = "D:\Summer Internship - QCRI\New_TICC\TICC-master\Datasets"
    fpath = os.path.join(direct_data, "Modified_nssr01 - 1000.csv")
    df = pd.read_csv("Series1_2000_zero_np2.csv", header=None,  sep = ',')
    #Manually finding out different periodical variables
    df_p = pd.DataFrame(df.iloc[:,0])
    df_p.loc[:,1] =df.loc[:,3]
    df_p.loc[:,2] =df.loc[:,5]
    df_p.loc[:,3] =df.loc[:,8]
    
    c = len(df.columns)
    
    ind = pd.isnull(df_p).any(1).nonzero()
    s = np.size(ind)
    #Since the tuple has multiple elements and it's size is (500,1)
    ind1 = np.column_stack(ind)
    
    for i in range(0,s):
        for j in range(c):
            z = ind1[i]
            df_p.loc[z,j] = 0
    '''
    #Taking Input in numpy format.
# 0,3,5,8
# 0,6,7
# 0,4
    
    data = np.loadtxt("nsrr01_1000_zero_np.csv", delimiter = ",")
    t = data[:,0]
    x = data[:,6]
    y = data[:,7]
    fig,(ax1, ax2) = plt.subplots(2,1,figsize=(15,15))
    ax1.plot(x)
    ax1.plot(y)
    '''
    data_null = np.loadtxt("Series1_2000_zero_np2_1.csv", delimiter = ',')
    ind = np.isnan(data_null)
    for i in range(1001):
        for j in range(4):
            if(ind[i][j]):
                data_null[i][j] = 0
''' 
    #df_p.to_csv("Series1_2000_zero.csv", sep = ',', header=False, index=False)
   # np.savetxt("Series1_2000_zero_series1.csv",data_null, delimiter = ',')

# 0,3,5,8
# 0,6,7
# 0,4
