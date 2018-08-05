
# coding: utf-8

# In[11]:

from TICC_solver import TICC
import numpy as np
import time
import pandas as pd
from matplotlib import pyplot
get_ipython().magic('matplotlib inline')


# In[3]:


"""
Created on Mon Jun 11 11:25:40 2018
#To generate cluster_assignment 
@author: Vignesh
"""

##########################
#Parameters to play with
window_size = i = 1
cluster_num = j = 3
lambda_p    = k = 0.01
beta_p      = l = 200

##########################

if __name__ == '__main__':
    fname = 'Week6_[n=3]_Amplitude_Wave3_New.csv'
    start_time = time.time()
    savelist = []
    
               
    ticc = TICC(window_size = i, number_of_clusters = j, lambda_parameter=k, beta=l, maxIters=100, threshold=2e-5,
                write_out_file=False, prefix_string="output_folder/", num_proc=1)
    (cluster_assignment, cluster_MRFs, bic_num) = ticc.fit(input_file=fname)
    tub = (i,j,k,l, bic_num)
    savelist.append(tub)
    #print(cluster_assignment)

    np.savetxt("ClusterAssign_Amplitude_Wave3.csv", cluster_assignment, delimiter= ',')
  


# In[12]:

import time


start_time = time.time()
df_read = pd.read_csv('Week6_[n=3]_Amplitude_Wave3_New.csv')
df_clust = pd.read_csv('ClusterAssign_Amplitude_Wave3.csv')
cluster_assignment = df_clust.iloc[:,0]
a = df_read.iloc[:,0]
b = df_read.iloc[:,1]
a = np.array(list(a))
b = np.array(list(b))

j = 0
s1 = np.size(a)
s3 = np.size(cluster_assignment)
k = 0
clus_assign = np.zeros(s1)
#If the window size varies a lot, this section assigns cluster number according to window size
ctr = 0
for i in range(0,s1):
    clus_assign[i] = cluster_assignment[k]
    ctr+=1
    if(ctr == window_size):
        k+=1
        ctr = 0
    
#Creating dataframe containing the series along with the cluster assignment for every datapoint and converting it into csv format.
data = np.column_stack((a,b, clus_assign))
df = pd.DataFrame(data)
    #print("Printing Dataframe! ")
print(df.iloc[:])
pyplot.plot(a)
pyplot.show()
df.to_csv('df_Test.csv', sep = ',', index = False, header = False)
e = time.time() - start_time
print("Process finished in: ",e," seconds - i.e. =", e/60," minutes")
    


# In[13]:

pyplot.plot(a)
pyplot.show()


# In[28]:

df_read = pd.read_csv('df_Test.csv')
i = 0
c = [ 'b','g','r','c','m','y']
t = 0 
x = df_read.iloc[:,0]
y = df_read.iloc[:,2]
z = np.unique(y)
s5 = np.size(z)
start_p =  end_p = 0
print(z)
x = np.array(list(x))
y = np.array(list(y))
'''
for i in range(1,s1):
    if(y[i-1] != y[i]):
        end_p +=1
        t = 0
    else:
        while(y[i-1] == y[i]):
            if((y[i-1] == z[t]) & (t<s5)):
                p = pyplot.axvspan(start_p, end_p, facecolor= c[int(z[t])], alpha=0.5)
               
            else:
                t+=1
                start_p+=1
                end_p+=2
 '''               
for i in range(1,s1-1):
    print(i)
    if(y[i-1] == y[i]):
        p = pyplot.axvspan(i-1, i, facecolor=c[int(y[i-1])], alpha=0.5)

pyplot.plot(x,c='k')
    #print(y[0])
pyplot.show()


# In[ ]:



