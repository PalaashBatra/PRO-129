import csv
import pandas as pd

d1 = []
d2 = []

with open("C:/Users/palaa/OneDrive/Desktop/whitehat/python/c129/pro/unit_converted_stars.csv","r") as o:
    csvread1=csv.reader(o)
    for row in csvread1:
        d1.append(row)

with open("C:/Users/palaa/OneDrive/Desktop/whitehat/python/c129/pro/bright_stars.csv","r") as f:
    csvread2=csv.reader(f)
    for row in csvread2:
        d2.append(row)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)