# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:18:47 2021

@author: admin
"""
## import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.colors as colors
import matplotlib

# del matplotlib.font_manager.weight_dict['roman']
# matplotlib.font_manager._rebuild()

# 用 Times New Roman 字体
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'

didV1=np.loadtxt(open("Vimp2.csv","rb"),delimiter=",",skiprows=0)

didV2=np.loadtxt(open("Vimp1.csv","rb"),delimiter=",",skiprows=0)

didV3=np.loadtxt(open("Vimp3.csv","rb"),delimiter=",",skiprows=0)

didV4=np.loadtxt(open("Vimp4.csv","rb"),delimiter=",",skiprows=0)

Vs=[didV1,didV2,didV3,didV4]
xs=np.linspace(0,399,400)
labels=[[r'$V_{imp1}: n_d=30/\mu m, \lambda=10nm$',
         r'$V_{imp2}:n_d=30/\mu m, \lambda=10nm$'],
        [r'$V_{imp3}:n_d=40/\mu m, \lambda=30nm$',
         r'$V_{imp4}:n_d=40/\mu m, \lambda=30nm$']]

figsize=10,7
figure, axs = plt.subplots(2,2,constrained_layout=True,figsize=figsize)

for i in range(2):
    for j in range(2):
        ax=axs[i,j]
        line,=ax.plot(xs,Vs[2*i+j],'-',color="peru",linewidth=3,label=labels[i][j])
        
        ax.legend(handles=[line],loc='lower left',bbox_to_anchor=(0, 0),
                  handlelength=0,handletextpad=0,fontsize=18) #,facecolor='none'
        
        ax.set_xticks((0,200,399))
        ax.set_xticklabels(['0','1','2'])
        ax.set_xlim([0,399])
        ax.set_ylim([-6,6])
        ax.set_ylabel(r'$V_{imp}(meV)$')
        ax.set_xlabel(r'$Position (\mu m)$')
        
        if i==0:
            ax.set_xticklabels('')
            ax.set_xlabel('')
        if j==1:
            ax.set_yticklabels('')
            ax.set_ylabel('')
            
plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
plt.rcParams['axes.linewidth'] = 1.5

plt.show()
figure.savefig('Fig2.png', format='png', dpi=400)