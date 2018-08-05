# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:07:22 2018
#Preprocessing: The inout given had a lot of NaN values which couldn't be recognized by TICC. Hence had to separately preprocess it before taking further action.
@author: Vignesh
"""

import numpy as np
import os

if __name__ == '__main__':
    #add input file!
    data = np.loadtxt('learn-nsrr01_data_[SR = 0.1,Data = 0.1%]-2.csv', delimiter = ',')
    s = len(data)
    c = data.shape
    cond = np.isnan(data)
    for i in range(s):
        for j in range(c[1]):
            if(cond[i][j]):
                data[i][j] = 0
    #Save the preprocessed data!
    np.savetxt("learn-nsrr01_data_[SR = 0.1,Sample = 40920(1%)]_np1.csv", data, delimiter = ',')
