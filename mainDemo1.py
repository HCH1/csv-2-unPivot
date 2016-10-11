from __future__ import division
from numpy.random import randn
import numpy as np
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import csv

path = "C:/Users/hhung/2015-6 work/demo0928TTdiff/DTTn2orig.csv"
f = open(path)
csv_f = csv.reader(f)
data = pd.read_csv(path, low_memory=False) 
## data.head(9)
df = pd.DataFrame(data)
## df.head(9)
unpivot = pd.melt(df, id_vars=['SPICE Model Name'], value_vars=list(df.columns[1:]),
        var_name='Col', value_name='Val')
## unpivot.head(9)
path2 = "C:/Users/hhung/2015-6 work/demo0928TTdiff/ans.csv"
unpivot.to_csv('C:/Users/hhung/2015-6 work/demo0928TTdiff/ansn2orig.csv', sep=',', index=False)
###
path = "C:/Users/hhung/2015-6 work/demo0928TTdiff/DTTn2old.csv"
f = open(path)
csv_f = csv.reader(f)
data = pd.read_csv(path, low_memory=False) 
## data.head(9)
df = pd.DataFrame(data)
## df.head(9)
unpivot = pd.melt(df, id_vars=['SPICE Model Name'], value_vars=list(df.columns[1:]),
        var_name='Col', value_name='Val')
## unpivot.head(9)
path2 = "C:/Users/hhung/2015-6 work/demo0928TTdiff/ans.csv"
unpivot.to_csv('C:/Users/hhung/2015-6 work/demo0928TTdiff/ansn2old.csv', sep=',', index=False)
###
