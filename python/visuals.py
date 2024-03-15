import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

#connecting to the csv
df = pd.read_csv('data/data.csv')

#defining the colours for the categories
colours = {
  'Relationships': '#c92f16', 
  'Body, mind and spirituality': '#3374c1', 
  'Community and society': '#f5bf32',
  'Job, learning and finances': '#469c34',
  'Interests and entertainment': '#8e22c9',
  'Personal care': '#434c4f'
}

colour_list = [colours[group] for group in df['Strategic Life Areas']]

#building the plot
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111)

#Setting up the text on the plot
plt.title('Strategise Your Life')
plt.xlabel('Satisfaction')
plt.ylabel('Importance')

#x and y limits
plt.xlim((0,10))
plt.ylim((0,10))

#adding the 4 quadrant lines
plt.plot([5,5],[0,11], linewidth=1, color='grey' )
plt.plot([0,11],[5,5], linewidth=1, color='grey' )



#Plots the data points
plt.scatter(df['Satisfaction'], df['Importance'], df['Time Invested']*10000, c=colour_list)

#adds the labels to the points
for i, txt in enumerate(df['Strategic Life Units']):
  ax.annotate(txt, (df['Satisfaction'][i], df['Importance'][i]), xytext=(df['Satisfaction'][i]+0.3, df['Importance'][i]+0.3), arrowprops=dict(arrowstyle='-'))

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

plt.savefig('img/visual.png')

