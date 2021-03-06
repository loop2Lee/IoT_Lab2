#IoT lab2 Lziheng Liu 2/7/2019
import math
import pandas
import sys
import seaborn as sns
import matplotlib.pyplot as plt

def num_str(row):
    #turn numbers from sring with ',' to pure nunmber
    #this function block comes from the lab manual 
    if isinstance(row['Population'], str):
        row['Population'] = int(row['Population'].replace(",", ""))
        if ('GDP' in row):
            row['GDP'] = int(row['GDP'].replace(",", ""))
        #print('population', row['Population'])
        return row

#df = df.apply(num_str, axis = 1)

def num_percentage(row):
    #this function turns thousandth of hundredth into hundredth
    if ('Birth Rate' in row):
        row['Birth Rate'] = float(row['Birth Rate']) / 1000
        row['Death Rate'] = float(row['Death Rate']) / 1000
        #print(row['Birth Rate'])
        #print(row['Death Rate'])
    return row