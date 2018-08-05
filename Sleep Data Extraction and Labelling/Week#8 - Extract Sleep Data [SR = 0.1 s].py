# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:17:20 2018
#Week8: To extract sleep data points for every 0.1 interval.
@author: Vignesh
"""
import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('learn-nsrr01_data.txt', sep = ',', header = None)
    a = df.loc[:,0]