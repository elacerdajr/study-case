#################
# This script will:
# - load plot libs
# - define settings
# - set paletes
# - load some userful functions
#################


#################
## libs
#################

import matplotlib
from matplotlib import pyplot as plt


# import plotly.express as px
# import plotly.graph_objects as go

#################
## settings
#################

# output image quality
# %config InlineBackend.figure_format = 'retina'

# set pyplot stype
# plt.style.use('dark_background') # see more with plt.style.available


# defaut figsize
matplotlib.rcParams['figure.figsize'] = [8,6]

# defaut font style
font = {'size':14,
        'family':'monospace'}
matplotlib.rc('font', **font)

# color pallete
global pal
pal = ['#2F58EB', '#773BEB', '#12B8EB', '#EB9846', '#8b8b8b', '#810f7c','#6D8AF1','#808080']

# Color maps
global cmap_neon
cmap_neon = matplotlib.colors.LinearSegmentedColormap.from_list("", [pal[2],pal[0]])

# setting defaut colors
from cycler import cycler
plt.rc('axes', prop_cycle=(cycler('color', pal) ))

#################
## some useful functions
#################

# remove unnecessary lines
def clean_ax(ax,n=2,minimalist=False):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    if n==3:
        ax.spines["left"].set_visible(False)

    
    if n==4:
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        
    if minimalist:
        ax.set_yticks([])
        ax.set_yticks([], minor=True)
        ax.set_xticks([])
        ax.set_xticks([], minor=True)

    return ax

# create prettier histogram
def grad_hist(ax, data, bins='auto', alpha=1, cmap='winter'): 
    
    if isinstance(cmap, str):
        cmap = matplotlib.cm.get_cmap(cmap)
    else:
        cmap = cmap


    N, bins, patches = ax.hist(data, bins=bins, density=False,rwidth=0.95,alpha=alpha)
    bmax = bins.max()
    bmin = bins.min()
    
    bins_norm = (bins - bmin) / (bmax - bmin)

    for bin_norm, patch in zip(bins_norm, patches):

        color = cmap(bin_norm)
        patch.set_facecolor(color)


    return ax