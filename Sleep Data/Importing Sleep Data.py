# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:13:12 2018
Week 8: Importing Sleep Data
@author: Vignesh
"""

import pandas as pd
import numpy as np
import csv

#Selecting over 1000 datapoints from the sleepdata. The data used had over ten million points to work with
if __name__ == '__main__':
    data = np.zeros((1000,15))
    data1 = []
    z = []
    z.append([])
    i = 0
    with open('nsrr01 - 1000_NoTitle.csv', 'rb') as csvfile:
        edf_reader = csv.reader(csvfile, delimiter = ' ')
        z=[]
        for row in edf_reader:
           print ','.join(row)
           data1 = ','.join(row)
           z += [data1.split(',')]
           i+=1
        
    for i in range(1001):
        for j in range(15):
            if(z[i][j] == ''):
                z[i][j] = None
    
    data = pd.DataFrame(data = z, index = None, columns = None)
    data.to_csv("Modified_nssr01 - 1000.csv",sep=',', columns = None, header = None, index = None)
