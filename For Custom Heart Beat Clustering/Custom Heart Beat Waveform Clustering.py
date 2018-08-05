# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 08:23:09 2018
To check the optimal beta value for Amplitude waveform using TICC
@author: Vignesh
"""

## Clustering using TICC for custom heartbeat waveform.

from TICC_solver import TICC
import numpy as np
import time
import pandas as pd

##########################
#Parameters to play with
window_size = i = 1
cluster_num = j = 3
lambda_p    = k = 0.01
beta_p      = l = 100

##########################

if __name__ == '__main__':
    fname = 'Heartbeat_Waveform.csv'
    start_time = time.time()
    savelist = []
    
    #For Iterations!
    for l in range(0,100, 10):            
       ticc = TICC(window_size=i, number_of_clusters = j, lambda_parameter=k, beta=l, maxIters=100, threshold=2e-5,
                   write_out_file=False, prefix_string="output_folder/", num_proc=1)
       (cluster_assignment, cluster_MRFs, bic_num) = ticc.fit(input_file=fname)
       tub = (i,j,k,l, bic_num)
       savelist.append(tub)
    #print(cluster_assignment)
    
    np.savetxt("HeartBeat_OptPara2.csv", savelist, delimiter= ',')

    e = time.time() - start_time
    print("Process finished in: ",e," seconds - i.e. =", e/60," minutes")
    #np.savetxt("Week#6:Savelist_Amplitude_3",np.transpose([x,x]),delimiter = ',')
