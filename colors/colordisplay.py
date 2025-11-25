import matplotlib.pyplot as plt 
import matplotlib as mpl

with open("colors.txt", encoding='utf-8') as file:
    color_r = file.read()
    color = color_r.split("\n")

with open("colors2.txt", encoding='utf-8') as file:
    color_r2 = file.read()
    color2 = color_r2.split("\n")

with open("colors3.txt", encoding='utf-8') as file:
    color_r3 = file.read()
    color3 = color_r3.split("\n")

fig = plt.figure(figsize=[8,3])
ax1 = fig.add_axes([0.05,0.8,0.9,0.2])
ax2 = fig.add_axes([0.05,0.475,0.9,0.2])
ax3 = fig.add_axes([0.05,0.15,0.9,0.2])

cmap = mpl.colors.ListedColormap(color)
cmap2 = mpl.colors.ListedColormap(color2)
cmap3 = mpl.colors.ListedColormap(color3)

bounds = [0] * len(color)
for idx, value in enumerate(bounds) : 
    bounds[idx] = idx + 1 

bounds2 = [0] * len(color2)
for idx, value in enumerate(bounds2) : 
    bounds2[idx] = idx + 1 

bounds3 = [0] * len(color3)
for idx, value in enumerate(bounds3) : 
    bounds3[idx] = idx + 1 

cb = mpl.colorbar.ColorbarBase(ax1,cmap=cmap,spacing='proportional',orientation='horizontal')
cb2 = mpl.colorbar.ColorbarBase(ax2,cmap=cmap2,spacing='proportional',orientation='horizontal')
cb3 = mpl.colorbar.ColorbarBase(ax3,cmap=cmap3,spacing='proportional',orientation='horizontal')

plt.show()
