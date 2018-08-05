
# coding: utf-8

# In[2]:

import pandas as pd
from pandas import Series
from matplotlib import pyplot
import random
import numpy as np
get_ipython().magic('matplotlib inline')
import time
import csv


# In[8]:

#For Visualization


"""
Created on Thu May 24 12:06:53 2018

@author: Vignesh
Program to extract the data from the dataframe - namely cluster assignments, Sensor Value (a) and (b).
x -> indicates the data point
y -> indicates the cluster assignment for that point.
Visualize them in a plot and also draw plots indicating cluster assignments.
"""


#numpy.savetxt("Opt_Para_Repeat_Amplitude2_1.csv", savelist, delimiter= ',')
start_time = time.time()

df = pd.read_csv('Heartbeat+Sine_Waveform_ClustAssign.csv', sep=',')
x = df.iloc[:,0]
y = df.iloc[:,2]
s1 = np.size(y)
print(s1)
'''
#Syntax to use for horizontal plots!
plt.axvspan(0, 360, facecolor='g', alpha=0.5)
'''      
x = [int(i) for i in x]

start_p = s2 = 0
end_p = 0
ctr = 0
t = 0
z = y.unique()
print(s2)
s2 = np.size(z)
print('z =',z)
k = l = 0



# In[4]:

'''x#For some reason, it keeps running without any display of graphs, no idea why! 
start_p = end_p = 0
c = [ 'b','g','r','c','m','y']
df = pd.read_csv('Heartbeat_Waveform_ClustAssign.csv', sep=',')
x = df.iloc[:,0]
y = df.iloc[:,2]
s1 = np.size(y)

for i in range(1,s1):
    if(y[i-1] != y[i]):
        end_p +=1
        t = 0
    else:
        while(y[i-1] == y[i]):
            if(y[i-1]==z[t]):
                p = pyplot.axvspan(start_p, end_p, facecolor=c[int(z[t])], alpha=0.5)
                start_p +=1
                end_p +=2
            else:
                t+=1
    #print(y[0])    
x = np.array(list(x))
#y = np.array(list(y))
pyplot.plot(x)
# = [int(i) for i in y]

pyplot.show()
'''


# In[13]:

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


c = [ 'b','g','r','c','m','y']
df = pd.read_csv('Heartbeat+Sine_Waveform_ClustAssign_Cluster = 4,Beta = 100.csv', sep=',')
x = df.iloc[:,0]
y = df.iloc[:,1]
z = df.iloc[:,2]
s1 = np.size(y)

ax1.plot(x, c = 'k')
ax2.plot(y, c = 'k')

z = z.astype(int)
#df.a = df.a.astype(float)

for i in range(1,808):
    p = ax1.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
    q = ax2.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
pyplot.show()

fig.savefig("Heart Beat + Varying Freq Sine Wave[Cluster = 4,Beta = 100]")


# In[55]:




# In[11]:

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,15))
c = [ 'b','g','r','c','m','y']
df = pd.read_csv('Heartbeat+Sine_Waveform_ClustAssign_Cluster = 4,Beta = 105.csv', sep=',')
x = df.iloc[:,0]
y = df.iloc[:,1]
z = df.iloc[:,2]
s1 = np.size(y)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(x, c = 'k')
ax2.plot(y, c = 'k')

z = z.astype(int)
#df.a = df.a.astype(float)

for i in range(1,808):
    p = ax1.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
    q = ax2.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
pyplot.show()

fig.savefig("Heart Beat + Varying Freq Sine Wave[Cluster = 4,Beta = 105]")


# In[12]:

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

c = [ 'b','g','r','c','m','y']
df = pd.read_csv('Heartbeat+Sine_Waveform_ClustAssign_Cluster = 4,Beta = 50, BIC = 157.csv', sep=',')
x = df.iloc[:,0]
y = df.iloc[:,1]
z = df.iloc[:,2]
s1 = np.size(y)

ax1.plot(x, c = 'k')
ax2.plot(y, c = 'k')

z = z.astype(int)
#df.a = df.a.astype(float)

for i in range(1,808):
    p = ax1.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
    q = ax2.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
pyplot.show()

fig.savefig("Heart Beat + Varying Freq Sine Wave [Cluster = 4,Beta = 50, BIC = 157]")


# In[ ]:




# In[8]:

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

c = [ 'b','g','r','c','m','y']
df = pd.read_csv('Heartbeat+Sine_Waveform_ClustAssign_Cluster = 4,Beta = 75,bic = 157.csv', sep=',')
x = df.iloc[:,0]
y = df.iloc[:,1]
z = df.iloc[:,2]
s1 = np.size(y)

ax1.plot(x, c = 'k')
ax2.plot(y, c = 'k')

z = z.astype(int)
#df.a = df.a.astype(float)

for i in range(1,808):
    p = ax1.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
    q = ax2.axvspan(i-1, i, facecolor=c[z[i]], alpha=0.5)
pyplot.show()
fig.savefig("Heart Beat + Varying Freq Sine Wave [Cluster = 4,Beta = 75,bic = 157]")


# In[ ]:



