import csv
import math

file = open('MEAN&Scatter105/data.csv', newline= '')
reader = csv.reader(file)
fileData = list(reader)
data = fileData[0]

def Mean () :
    n = len(data)
    sum = 0
    for i in data :
        sum = sum + int(i)
    mean = sum/n
    return mean

squaredList = []
for number in data :
    a = int(number)- Mean()
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList :
    sum = sum + i

result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)
