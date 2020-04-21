import openpyxl
from pathlib import Path
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


filename = 'datap2.txt'

pt = Path(__file__)
parent = pt.parent
filepath = Path.joinpath(parent,filename)
data = []

fl = open(filepath,'r')
data = fl.read().split('\n') 
fl.close()

#print(data)
n = []
x = []
y = []

for i in range(len(data)):
    k = data[i].split(' ')
    n.append(float(k[0]))
    x.append(float(k[1]))
    y.append(float(k[2]))
    #print(x[i],y[i])

num = 0
dem = 0
x_sqr = [xl**2 for xl in x]
ssx = sum(x_sqr)

x_mean = np.mean(x)
y_mean = np.mean(y)
#calcualting b0 and b1
for i in range(len(x)):
    num+= (x[i]-x_mean)*(y[i]-y_mean)
    dem+= (x[i]-x_mean)**2

b1 = num/dem
b0 = y_mean - b1*x_mean

y_pred = []
for xl in x:
    y_pred.append(b1*xl+b0)

print('y='+str(b0)+'+('+str(b1)+')x')
#calculating sigma^2
sqresid = []

sqrmean = []
for i in range(len(y)):
    dif = y_mean - y[i]
    sqrmean.append(dif**2)
sst = sum(sqrmean)

for i in range(len(y)):
    dif = y_pred[i] - y[i]
    sqresid.append(dif**2)
sse = sum(sqresid)
ssr = sst-sse

#n-2 because we using sample data
s_sqr = sse/(len(x)-2) 
print('sigma sqr = '+str(s_sqr))

#calculating Variances
s = s_sqr**0.5
sb1 = s/(dem**0.5) 
varb1 = sb1**2
print('Var(b1) = '+str(varb1))

varb0 = (s_sqr*ssx)/(len(x)*dem)
print('Var(b0) = '+str(varb0))
#calculating correlation
r_sqr = ssr/sst
print('r^2 = '+str(r_sqr))

plt.plot([min(x),max(x)],[min(y_pred),max(y_pred)])
plt.scatter(x,y)


plt.show()
