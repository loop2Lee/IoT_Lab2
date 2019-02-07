import pandas
import sys
import csv
import functions

inputfile = 'country_list.csv'
inputlist = []
processlist = []
firstlist = []
input_dict = {}
row_dict = {}

with open (inputfile,newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t',quotechar = ' ')
    for row in reader:
       row_dict = {}
       n = 0
       inputlist.append(row)
    #print(inputlist)
       #print(len(row))
       #while n != len(row):
       #    row_dict[inputlist[0][n]] = row[n]
       #    print(row_dict)
       #processlist.append(row_dict)
firstlist = inputlist[0]
for row in inputlist:
    m = 0
    row_dict = {}
    while m != len(row):
        row_dict[firstlist[m]] = row[m]
        m = m + 1
    processlist.append(row_dict)
del processlist[0]
#print(processlist)
for row in processlist:
    row = functions.num_str(row)
    row = functions.num_percentage(row)
    print(row)
