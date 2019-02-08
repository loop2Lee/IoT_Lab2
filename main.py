import pandas as pd
import sys
import csv
import functions

inputfile     = 'country_list.csv'
inputlist     = []
processlist   = []
firstlist     = []
endlist       = []
Birth_list    = []
netBirth_list = []

input_dict = {}
row_dict   = {}

with open (inputfile,newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t',quotechar = ' ')
    for row in reader:
       row_dict = {}
       n = 0
       inputlist.append(row)
    #print(inputlist)

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
    endlist.append(row)
    #print(row)
#print(endlist)

#Problems solution
for i in endlist:
    netBirth = 0
    netRate = 0
    if ('Birth Rate' in i):
        if i['Birth Rate'] > 0.045:
            Birth_list.append(i["Name"])
        netBirth = i['Birth Rate'] - i['Death Rate']
    netRate = [netBirth, i['Name']]
    netBirth_list.append(netRate)


#Solution 1
print(sorted(Birth_list, reverse = True))

#Solution 2
netBirth_list.sort(reverse = True)
print(netBirth_list[:5])

