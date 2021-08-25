# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:36:02 2021

@author: admin
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.colors as colors
import matplotlib



didV=np.loadtxt(open("Fig5_Vimp4_ap5_addedcp.csv","rb"),delimiter=",",skiprows=0)
didV9=np.transpose(didV.reshape(501,101))

Bs=np.linspace(0,3,501)
mus=np.linspace(5.5,6,101)


figsize=10,7
figure, axs= plt.subplots(2,1,constrained_layout=True,
                           figsize=figsize,gridspec_kw={'height_ratios': [1,1]})

# line,=ax.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3)  

# ax.legend(handles=[line],loc='lower left',#bbox_to_anchor=(-0.04, -0.03),
#           handlelength=0,handletextpad=0,fontsize=20) #,facecolor='none'

pcm =axs[0].contourf(Bs,mus,didV9,[0,1.9,2.1,4],
                         colors = ["#E4EBF2","#0343DF","#FFFF14"],
                         vmin=0.0, vmax=4,extend='neither')




axs[0].set_xlim([0.,3.])        
axs[0].set_xticks((0, 1, 2, 3))
axs[0].set_xticklabels('')
axs[0].plot([1.5,2.1],[mus[15],mus[15]],color='cyan')
axs[0].plot([1.5,2.1],[mus[19],mus[19]],color='red')
axs[0].plot([1.5,2.1],[mus[22],mus[22]],color='green')
axs[0].set_ylabel(r'$\mu(meV)$')

didV9=np.round(didV9,2)
line1,=axs[1].plot(Bs,didV9[15,:], linewidth=3,color='cyan')
line2,=axs[1].plot(Bs,didV9[19,:], linewidth=3,color='red')
line3,=axs[1].plot(Bs,didV9[22,:], linewidth=3,color='green')
axs[1].plot([1.5,2.1],[2,2],'k--', linewidth=2)
axs[1].set_ylim([0., 2.4])


# axs[1].set_xlim([1.5,2.0])
axs[1].set_xlim([0.,3.])        
axs[1].set_xticks((0, 1, 2, 3))
axs[1].set_xticklabels(['0','1','2','3'])
axs[1].set_ylabel(r'$G(e^2/h)$')
axs[1].set_xlabel(r'$\Gamma(meV)$')

plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
plt.rcParams['axes.linewidth'] = 1.5

plt.show()

fig,ax=plt.subplots(figsize=(4,2.5))
line1,=ax.plot(Bs,didV9[15,:], linewidth=3,color='cyan')
line2,=ax.plot(Bs,didV9[19,:], linewidth=3,color='red')
line3,=ax.plot(Bs,didV9[22,:], linewidth=3,color='green')
ax.plot([1.5,2.1],[2,2],'k--', linewidth=2)
ax.set_ylim([1.65, 2.35])
ax.set_yticks((1.8,2.,2.2))
ax.set_xlim([1.65,1.95])