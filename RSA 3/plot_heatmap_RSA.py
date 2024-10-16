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
path = 'C:/Users/Zirui Zhang/Desktop/For Yuan/box and violin plots for Yuan/heatmap/RSA/'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

for i in range(3):
    if i == 0:
        data = read_csv(path + 'RSA_delay.csv')
        data = data[data.columns[::-1]]
    if i == 1:
        data = read_csv(path + 'RSA_sample.csv') 
        data = data[data.columns[::-1]]
    if i == 2:
        data = read_csv(path + 'RSA_iti.csv') 
        data = data[data.columns[::-1]]
        
    label = [1,2,3,4,5,6]
        # Assuming you want to plot a heatmap of the first 3x3 portion of the dataset
        # If your data is already in a 3x3 form, you can use it directly.
        # Otherwise, you can slice the first 3x3 portion as follows:
    heatmap_data = data.iloc[:6, :6]
    #diagonal = np.diag(np.diag(heatmap_data))
    colors = ['#14958D','#5ab4af',
        '#89cac6','#a1d4d1',
        '#d0e9e8','#e7f4f3','#ffffff']  # Example colors #
        
        #14958d
        #2b9f98
        #42aaa3
        #5ab4af
        #72bfbaxinl
        #89cac6
        #a1d4d1
        #b8dfdc
        #d0e9e8
        #e7f4f3
        #ffffff
        
    colors.reverse()
        # Create a custom diverging palette
    cmap = sns.color_palette(colors, as_cmap=True)
        
        
    vmin_value = 3.9    # minimum value for the colorbar
    vmax_value = 4  # maximum value for the colorbar
        # Plot the heatmap
    fig, ax = plt.subplots()
    
    flip_hdata = np.fliplr(heatmap_data)
    diagonal = np.diag(np.diag(flip_hdata))
    diagonal = np.fliplr(diagonal)
    fflip_hdata = np.triu(flip_hdata)
    matrix = np.fliplr(fflip_hdata) - diagonal
   # h_diag = np.diag(np.diag(heatmap_data))
    #heatmap_data = heatmap_data + diagonal
    ax = sns.heatmap(heatmap_data,vmin=vmin_value, vmax=vmax_value, annot=False, cmap = cmap, mask=matrix)
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
    ax.set_xlabel('locations', fontsize = 14, fontname='Arial')
    ax.set_ylabel('locations',fontsize = 14, fontname='Arial')
    ax.set_xticklabels(ax.get_xticklabels(), fontname='Arial')
    ax.set_yticklabels(ax.get_xticklabels(), fontname='Arial')
        #ax.set_title('Deeper (Delay)',fontsize = 20,fontname='Arial')
        
    if i == 0:    
        
        ax.set_title('RSA (Delay)',fontsize = 20,fontname='Arial')
        # Display the plot
        fig.set_size_inches(7, 6, forward=True)
        fig.savefig('RSA_delay.png', dpi=300)
        fig.savefig('RSA_delay.pdf', dpi=300, transparent=True)
        
    if i == 1:    
        
        ax.set_title('RSA (Sample)',fontsize = 20,fontname='Arial')
        # Display the plot
        fig.set_size_inches(7, 6, forward=True)
        fig.savefig('RSA_sample.png', dpi=300)
        fig.savefig('RSA_sample.pdf', dpi=300, transparent=True)
        
    if i == 2:    
        
        ax.set_title('RSA (ITI)',fontsize = 20,fontname='Arial')
        # Display the plot
        fig.set_size_inches(7, 6, forward=True)
        fig.savefig('RSA_iti.png', dpi=300)
        fig.savefig('RSA_iti.pdf', dpi=300, transparent=True)
    
    plt.show()









