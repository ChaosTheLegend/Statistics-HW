import openpyxl
from pathlib import Path
import os
import numpy as np
import matplotlib.pyplot as plt

wbname = Path(os.getcwd())
wbname= os.path.join(wbname,Path("Stat//HW7//data.xlsx"))
print(wbname)
wb = openpyxl.load_workbook(wbname)
ws = wb.worksheets[1]

x = []
y = []

for i in range(1,9):
    c = ws['A'+str(i)]
    l = str(c.value).split(' ')
    x.append(float(l[1]))
    y.append(float(l[2]))


x_mean = np.mean(x)
y_mean = np.mean(y)

num = 0
dem = 0

y_pred = []
for i in range(len(x)):
    num+= (x[i]-x_mean)*(y[i]-y_mean)
    dem+= (x[i]-x_mean)**2

b0 = num/dem
b1 = y_mean - b0*x_mean
for xl in x:
    y_pred.append(b0*xl+b1)

plt.plot([min(x),max(x)],[min(y_pred),max(y_pred)])
plt.scatter(x,y)

a = np.polyfit(x,y,2)
b = np.poly1d(a)



plt.plot(x,b(x))
plt.show()

