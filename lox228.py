import torch
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def func(x):
    return 2*np.exp(-np.abs(x+1)/2)+2*np.exp(-np.abs(x-1)/2)
x_val=np.linspace(-10,10,100)
y_val=func(x_val)
sns.set(style='whitegrid')
sns.lineplot(x=x_val,y=y_val)
plt.show()