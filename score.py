import os, sys, collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

### test data

ns = 'ABCDE'
n = [x for x in ns]
s = [10,20,40,30,20]

s_mean = np.mean(s)
s_std = np.std(s)

#s_pdf = norm.pdf(sorted(s),s_mean, s_std)
x = np.linspace(0,100,100)
y = norm.pdf(x,s_mean,s_std)


### graph 그리기

plt.plot(x,y, color="blue", label="score")
plt.axvline(x=30, linestyle='dashed', color = "red")
plt.legend()
plt.grid(True, alpha=0.3, linestyle="--", label ='30')
plt.text(30, -.003, "test", ha="center", va = "top")
plt.show()
