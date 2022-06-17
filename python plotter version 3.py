import numpy as np
import csv
import pandas as pd
import matplotlib.pylab as plt
#setting directory 

df = pd.read_excel('ground_truth.xlsx','sheet1')

#set plot
x = list(df['tx'])
y = list(df['ty'])
a = list(df['TX2'])
b = list(df['TY2'])

#set labels
plt.figure(figsize=(10,10))
plt.style.use('classic')
plt.scatter(x,y,marker=".",s=100,edgecolors="black",c="red")
plt.scatter(a,b,marker=".",s=100,edgecolors="black",c="green")
plt.title("Plot 1: Vicon Ground Truth Data")
plt.xlabel('X Coordinates', fontsize=15)
plt.ylabel('Y Coordinates', fontsize=15)
plt.show()