# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:25:40 2018
#To generate cluster_assignment 
@author: Vignesh
"""

from TICC_solver import TICC
import numpy as np
import time
import pandas as pd
import os

##########################
#Parameters to play with
window_size = i = 1
cluster_num = j = 2
lambda_p    = k = 0.01
beta_p      = l = 350
Iters       = z = 10
##########################

if __name__ == '__main__':
    fname = 'Series1_30_Repv1.csv'
    start_time = time.time()
    savelist = []

    ticc = TICC(window_size = i, number_of_clusters = j, lambda_parameter=k, beta=l, maxIters=z, threshold=2e-5,
                write_out_file=False, prefix_string="output_folder/", num_proc=5)
    (cluster_assignment, cluster_MRFs, bic_num) = ticc.fit(input_file=fname)
    tub = (i,j,k,l, bic_num)
    savelist.append(tub)
    #print(cluster_assignment)
    print("Done with TICC")
    #numpy.savetxt("Opt_Para_Repeat_Amplitude2_1.csv", savelist, delimiter= ',')
    #Manual Entry of the number of columns. Need to find an efficient way.
    print(bic_num)
     
    #If the window size varies a lot, this section assigns cluster number according to window size
        #To save the cluster assignments using pandas
    data = pd.read_csv("Series1_30_Repv1.csv", sep=',', header = None)
    a = data.iloc[:,0]
    j = ctr = 0
    s1 = a.shape[0]
    s3 = np.size(cluster_assignment)
    k = 0
    clus_assign = np.zeros(s1)    
    for i in range(0,s1):
            clus_assign[i] = cluster_assignment[k]
            ctr+=1
            if(ctr == window_size):
                k+=1
                ctr = 0    
    #Creating dataframe containing the series along with the cluster assignment for every datapoint and converting it into csv format.
    data = np.column_stack((data,cluster_assignment))
    data_save = pd.DataFrame(data)
    data_save.to_csv("Series1_30_Repv1-Cluster-5200.csv", sep = ',', header = False, index = False)
    e = time.time() - start_time
    print("Process finished in: ",e," seconds - i.e. =", e/60," minutes")    

   
