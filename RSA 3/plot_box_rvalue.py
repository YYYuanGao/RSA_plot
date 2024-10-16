import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches


data = pd.read_csv('./data_rvalue.csv') 

# Display the first few rows of the dataset to verify the columns

fig, ax = plt.subplots(figsize=(10, 6))
# Set up the figure
plt.figure(figsize=(6, 6))
line_colours = ['#a566a1', '#609dc5', '#ecbd4a']
fillcolours = ['#c395be', '#99c7da', '#f3d886']
# Create a violin plot for the 'day' vs. 'total_bill'
# =============================================================================
box = sns.boxplot(x = 'time', y = 'rvalue_z', data=data, width = 0.2, ax = ax,palette = fillcolours,
                   linewidth=4, boxprops=dict(edgecolor='none'))

# Apply custom edge colors

for i, line in enumerate(box.lines):
    if i % 6 == 0 or i % 6 == 1:  # Whiskers
        line.set_color(line_colours[i // 6 % len(line_colours)])
    elif i % 6 == 2 or i % 6 == 3:  # Caps
        line.set_color(line_colours[i // 6 % len(line_colours)])
    elif i % 6 == 4:  # Median line
        line.set_color(line_colours[i // 6 % len(line_colours)])

sns.swarmplot(x = 'time', y = 'rvalue_z',data=data, ax=ax,palette=line_colours,size=12, alpha = 0.9) 
# Clip the violin plot to create the half violin effect

    
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

ax.set_xticklabels(ax.get_xticklabels(), fontname = 'Arial', fontsize = 16)
ax.set_yticklabels(ax.get_yticklabels(), fontname='Arial', fontsize = 16)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(2)  # Set border width for left spine
ax.spines['bottom'].set_linewidth(2)  # Set border width for bottom spine
ax.spines['left'].set_linestyle('-')
ax.set_ylabel('r-value', fontsize=20,fontname='Arial')
ax.set_xlabel('')
sns.set_style("white")


ax.set_title('Correlation', fontsize=22, pad=20,fontname='Arial')

fig.savefig('rvalue_z.pdf', dpi=300, transparent=True)
fig.savefig('rvalue_z.png', dpi=300)
plt.show()