# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 10:18:58 2018

@author: Vignesh
"""


#####Visualization of the clustering done by TICC! This is for four different custom generated waveforms.

import numpy as np
from matplotlib import pyplot
import csv 
import pandas as pd
import sys
import time

if __name__ == '__main__':
    #Importing the file with cluster arrangement.
    df = pd.read_csv('Week4_Mixed[4]_Freq_Wave_Final_Multivariate_WithoutLabel_csv.csv', sep=',')
    #print(df)
    start_p = 0
    end_p = 0
    ctr = 0

    #For four different waveforms and the last column representing the cluster assignment.
    a = df.iloc[:,0]
    b = df.iloc[:,1]
    c = df.iloc[:,2]
    d = df.iloc[:,3]
    e = df.iloc[:,4]
    print(b)
    '''
    a = np.array(list(a))
    b = np.array(list(b))
    c = np.array(list(c))
    d = np.array(list(d))
    e = np.array(list(e))
    '''
    s = np.size(e)
    
    fig,(ax1,ax2,ax3,ax4) = pyplot.subplots(4,1)
    ax1.plot(a,c='black')
    #ax1.show()
    ax2.plot(b, c='black')
    ax3.plot(c,c='black')
    ax4.plot(d,c='black')
    j= e.unique()
    s1 = np.size(j)
    
    a = np.array(list(a))
    b = np.array(list(b))
    c = np.array(list(c))
    d = np.array(list(d))
    e = np.array(list(e))
    
    c = ['b','g','r','g']
    #print(y[0])
    #pyplot.plot(x,c='w')

    # This is an inefficient way of plotting but works. Efficient way would be to find all the indices belonging to the same column and then plotting individual clusters separately.
    for i in range(1,1440):
        if(e[i-1] == e[i]):
             end_p=i+1
        else:
             for k in range(0,s1):
                if(j[k]==e[i]):
                    p = ax1.axvspan(start_p,end_p, facecolor=c[k], alpha=0.6)      
                    q = ax2.axvspan(start_p,end_p, facecolor=c[k], alpha=0.6)
                    r = ax3.axvspan(start_p,end_p, facecolor=c[k], alpha=0.6)
                    s = ax4.axvspan(start_p,end_p, facecolor=c[k], alpha=0.6)
                    
                    #print(c[k])
                    start_p=i+1              
                    end_p=i+2
        
