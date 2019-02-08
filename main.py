#IoT lab2 Lziheng Liu 2/7/2019
import pandas as pd
import csv
import functions
import seaborn as sns
import matplotlib.pyplot as plt

inputfile     = 'country_list.csv'
inputlist     = []
processlist   = []
firstlist     = []
endlist       = []
Birth_list    = []
netBirth_list = []
futurePop_list    = []
aGDP_netRate  = []

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
    futurePop = 0
    aGDP = 0
    aGDP_netRate1 = {}
    future_pop = []
    if ('Birth Rate' in i):
        if i['Birth Rate'] > 0.045:
            Birth_list.append(i["Name"])
        netBirth = i['Birth Rate'] - i['Death Rate']
        futurePop = i['Population'] * (1 + netBirth ** 31)
        aGDP = i['GDP'] / i['Population']
    netRate = [netBirth, i['Name']]
    future_pop = [futurePop, i['Name']]
    futurePop_list.append(future_pop)
    netBirth_list.append(netRate)
    aGDP_netRate1 = {'aGDP': aGDP, 'netBirth': netBirth}
    aGDP_netRate.append(aGDP_netRate1)

#Solution 1
print(sorted(Birth_list, reverse = True))

#Solution 2
netBirth_list.sort(reverse = True)
print(netBirth_list[:5])

#Solution 3
futurePop_list.sort(reverse = True)
print(futurePop_list[:5])

#Solution 4
#print(aGDP_netRate)
aGDP_nB_df = pd.DataFrame(aGDP_netRate)
im = sns.catplot(x = 'netBirth', y = 'aGDP', data = aGDP_nB_df, kind = 'strip')
plt.show()
