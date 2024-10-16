# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:50:45 2024

@author: Zirui Zhang
"""

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from pandas import *
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

data = read_csv('./ddeep.csv')
label = [1,2,3,4,5,6]
# Assuming you want to plot a heatmap of the first 3x3 portion of the dataset
# If your data is already in a 3x3 form, you can use it directly.
# Otherwise, you can slice the first 3x3 portion as follows:
heatmap_data = data.iloc[:6, :6]
colors = ['#14958D','#5ab4af',
'#89cac6','#a1d4d1',
'#d0e9e8','#e7f4f3','#ffffff']  # Example colors #

#14958d
#2b9f98
#42aaa3
#5ab4af
#72bfba
#89cac6
#a1d4d1
#b8dfdc
#d0e9e8
#e7f4f3
#ffffff

colors.reverse()
# Create a custom diverging palette
cmap = sns.color_palette(colors, as_cmap=True)


vmin_value = 0.1    # minimum value for the colorbar
vmax_value = 0.22  # maximum value for the colorbar
# Plot the heatmap
fig, ax = plt.subplots()
ax = sns.heatmap(heatmap_data,vmin=vmin_value, vmax=vmax_value, annot=False, cmap = cmap)
for text in ax.texts:
    text.set_fontname('Arial')
    text.set_color('black')
colorbar = ax.collections[0].colorbar

# Customize the colorbar label
colorbar.ax.yaxis.label.set_fontname('Arial')
colorbar.ax.yaxis.label.set_fontsize(12)  # Adjust label font size
colorbar.ax.yaxis.label.set_color('black')  # Set label color
colorbar.ax.tick_params(labelsize=10, labelcolor='black')  # Adjust tick label size and color

# Customize colorbar tick labels
colorbar.ax.set_yticklabels(colorbar.ax.get_yticklabels(), fontname='Arial')


ax.set_xlabel('Perdicted location', fontsize = 14, fontname='Arial')
ax.set_ylabel('Actual location',fontsize = 14, fontname='Arial')
ax.set_xticklabels(ax.get_xticklabels(), fontname='Arial')
ax.set_yticklabels(ax.get_xticklabels(), fontname='Arial')
#ax.set_title('Deeper (Delay)',fontsize = 20,fontname='Arial')
ax.set_title('Deeper layers (Delay)',fontsize = 20,fontname='Arial')
# Display the plot
fig.set_size_inches(8, 6, forward=True)
fig.savefig('ddeep.jpg', dpi=300)
fig.savefig('ddeep.pdf', dpi=300, transparent=True)
plt.show()


data = read_csv('./dmiddle.csv')

# Assuming you want to plot a heatmap of the first 3x3 portion of the dataset
# If your data is already in a 3x3 form, you can use it directly.
# Otherwise, you can slice the first 3x3 portion as follows:
heatmap_data = data.iloc[:6, :6]
colors = ['#14958D','#5ab4af',
'#89cac6','#a1d4d1',
'#d0e9e8','#e7f4f3','#ffffff']  # Example colors #

#14958d
#2b9f98
#42aaa3
#5ab4af
#72bfba
#89cac6
#a1d4d1
#b8dfdc
#d0e9e8
#e7f4f3
#ffffff

colors.reverse()
# Create a custom diverging palette
cmap = sns.color_palette(colors, as_cmap=True)
# Plot the heatmap
fig, ax = plt.subplots()
ax = sns.heatmap(heatmap_data, vmin=vmin_value, vmax=vmax_value,annot=False, cmap = cmap)
for text in ax.texts:
    text.set_fontname('Arial')
    text.set_color('black')

colorbar = ax.collections[0].colorbar

# Customize the colorbar label
colorbar.ax.yaxis.label.set_fontname('Arial')
colorbar.ax.yaxis.label.set_fontsize(12)  # Adjust label font size
colorbar.ax.yaxis.label.set_color('black')  # Set label color
colorbar.ax.tick_params(labelsize=10, labelcolor='black')  # Adjust tick label size and color

# Customize colorbar tick labels
colorbar.ax.set_yticklabels(colorbar.ax.get_yticklabels(), fontname='Arial')

ax.set_xlabel('Perdicted location', fontsize = 14, fontname='Arial')
ax.set_ylabel('Actual location',fontsize = 14, fontname='Arial')
ax.set_xticklabels(ax.get_xticklabels(), fontname='Arial')
ax.set_yticklabels(ax.get_xticklabels(), fontname='Arial')
#ax.set_title('Middle (Delay)',fontsize = 20, fontname='Arial')
ax.set_title('Middle layers (Delay)',fontsize = 20, fontname='Arial')
# Display the plot
fig.set_size_inches(8, 6, forward=True)
fig.savefig('dmiddle.jpg', dpi=300)
fig.savefig('dmiddle.pdf',transparent=True, dpi=300)


data = read_csv('./dsuper.csv')
# Assuming you want to plot a heatmap of the first 3x3 portion of the dataset
# If your data is already in a 3x3 form, you can use it directly.
# Otherwise, you can slice the first 3x3 portion as follows:
heatmap_data = data.iloc[:6, :6]
colors = ['#14958D','#5ab4af',
'#89cac6','#a1d4d1',
'#d0e9e8','#e7f4f3','#ffffff']  # Example colors #

#14958d
#2b9f98
#42aaa3
#5ab4af
#72bfba
#89cac6
#a1d4d1
#b8dfdc
#d0e9e8
#e7f4f3
#ffffff

colors.reverse()
# Create a custom diverging palette
cmap = sns.color_palette(colors, as_cmap=True)
# Plot the heatmap
fig, ax = plt.subplots()
ax = sns.heatmap(heatmap_data, vmin=vmin_value, vmax=vmax_value,annot=False, cmap = cmap)
for text in ax.texts:
    text.set_fontname('Arial')
    text.set_color('black')
    
colorbar = ax.collections[0].colorbar

# Customize the colorbar label
colorbar.ax.yaxis.label.set_fontname('Arial')
colorbar.ax.yaxis.label.set_fontsize(12)  # Adjust label font size
colorbar.ax.yaxis.label.set_color('black')  # Set label color
colorbar.ax.tick_params(labelsize=10, labelcolor='black')  # Adjust tick label size and color

# Customize colorbar tick labels
colorbar.ax.set_yticklabels(colorbar.ax.get_yticklabels(), fontname='Arial')

ax.set_xlabel('Perdicted location', fontsize = 14, fontname='Arial')
ax.set_ylabel('Actual location',fontsize = 14, fontname='Arial')
ax.set_xticklabels(ax.get_xticklabels(), fontname='Arial')
ax.set_yticklabels(ax.get_xticklabels(), fontname='Arial')
ax.set_title('Superficial layers (Delay)',fontsize = 20, fontname='Arial')
#ax.set_title('Superficial layers (Delay)',fontsize = 20, fontname='Arial')
# Display the plot
fig.set_size_inches(8, 6, forward=True)
fig.savefig('dsuper.jpg', dpi=300)
fig.savefig('dsuper.pdf', dpi=300, transparent=True)
plt.show()







