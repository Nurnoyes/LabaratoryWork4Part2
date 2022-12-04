import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

'CustomerID', 'Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'
counter = 0
xlabel = []
ylabel = []
df = pd.read_csv('Mall_Customers.csv')
'''
    Hypothesis: Female in general spend more than Male.
    The hypothesis is true if half or more than a half values of
    mean, min, 25%, 50%, 75% and max value of Female column is more than such of Man column.
    Grouping the dataset to see:
'''
print(df.groupby('Genre')['Spending Score (1-100)'].describe())
'''
        We have:
                count       mean       std       min  25%   50%   75%   max
Genre                                                          
Female          112.0       51.526786  24.11495  5.0  35.0  50.0  73.0  99.0
Male            88.0        48.511364  27.89677  1.0  24.5  50.0  70.0  97.0

So, mean, min, 25%, 75% and max values of Female column is MORE than such of men column.


                The conclusion:
                    Female in general spend more than Male
'''
#print(df.describe())




with open('Mall_Customers.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if (counter == 0):
            counter += 1
            continue
        xlabel.append(int(row[0]))
        ylabel.append(int(row[4]))
        #print(row)

fig, ax = plt.subplots(figsize=(18,8))  # Create a figure containing a single axes.
ax.plot(xlabel,ylabel,color='#f55d42',linewidth='0',marker=".")
#plt.plot(xlabel, ylabel)#bins=100)#, ylabel, bins=100) #align='edge', linewidth=4000);  # Plot some data on the axes.
plt.title('ID & Annual Income/Spending score')
ax.set_xlabel('ID', fontsize='21')
#ax.set_xticks([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200])
#ax.set_xticklabels(["0","10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140", "150", "160", "170", "180", "190", "200"],fontsize='8')
ax.set_ylabel('Annual Income',fontsize='21')#plt.ylabel('Spending score')
#ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
#ax.set_yticklabels(["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"], fontsize="8")
plt.show()

