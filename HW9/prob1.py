import openpyxl
from pathlib import Path
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 28
y = 19
a = 0.05
prb = binom.pmf(y,n,0.5)
if(prb>=a):
    print('significant')
else:
    print('insignificant')
#p is less than a, that means that difference is insignificant