import csv
import math

with open("data2.csv", newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

total = 0
for i in data:
    total += float(i)

n = len(data)
mean = total/n

sqList = []
for i in data:
    x = int(i) - mean
    x = x**2
    sqList.append(x)

sum = 0
for i in sqList:
    sum += i

result = sum/(n-1)

stdv = math.sqrt(result)

print("The Standard Deviation is: ", stdv)