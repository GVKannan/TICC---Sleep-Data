
# coding: utf-8
#Program to extract the data from Sleep Data
# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


data = pd.read_csv("learn-nsrr01_data.txt", sep=',')


# In[9]:


a = data.iloc[:,0]
print(a)


# In[26]:


n = len(a) # 10,230,000 points
index = []
for i in range(0,20000):
    if(i%25 == 0):
        index.append(i)
        data_skim = data.loc[i,:]
        i+=25
#print(index)
#n1 = len(index)
data_skim = data.ix[(data.index%25 ==0)]


# In[30]:


data_skim.to_csv("learn-nsrr01_data_[SR = 0.1].csv", sep=',', header=False, index= False)


# In[69]:


n2 = len(data_skim)
print(n2)
print(n2*0.1)
n4 = int(n2*0.1)
data_p = data.ix[(data.index<n4)]
n3 = len(data_p)
print(n3)
data_p.to_csv("learn-nsrr01_data_[SR = 0.1,Data = 0.1%]-2.csv", sep=',', header=False,index = False)


# In[65]:


print(len(data_skim))
print(len(data_p))
print(int(n4))


# In[ ]:


#Changing NaNs to zero
#idx.isna() idx = pd.index

n = len(data_p)
cond = data_p.isnull()
print(cond)
print(cond.shape)
#for i in range(0,1): #For the row index
#    for j in range(0,1): #For Column index
#        if()


n = len(data_p)
#print(n) #40920

cond = data_p.isnull()
#print(cond) #40919 x 15
for i in range(0,n): #For the row index
    for j in range(0,15): #For Column index
        if(cond.iloc[i,j]):
            data_p.iloc[i,j] = 0

