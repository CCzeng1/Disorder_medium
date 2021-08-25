# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:06:44 2021

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:24:58 2021

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:28:54 2021

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

font1 = {'family': 'serif',
        'serif': 'Times New Roman',
        'weight': 'normal',
        'size': 10}


# 用 Times New Roman 字体
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'


didV=np.loadtxt(open("Fig5_Vimp2_ap1.csv","rb"),delimiter=",",skiprows=0)
didV1=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig5_Vimp2_ap2p5.csv","rb"),delimiter=",",skiprows=0)
didV2=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig5_Vimp2_ap5.csv","rb"),delimiter=",",skiprows=0)
didV3=np.transpose(didV.reshape(301,501))

Bs=np.linspace(0,3,301)
mus=np.linspace(-3,7,501)

figsize=10,12
figure, [[ax1,ax2,ax3],[ax4,ax5,ax6]] = plt.subplots(2,3,constrained_layout=True,figsize=figsize)
# plt.subplots_adjust(wspace=0.1,hspace=0.1)
# cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["#E4EBF2","#0444BF","#F4ED71"])
cbaxes = figure.add_axes([0.14, 1.005, 0.8, 0.015])
cbaxes1 = figure.add_axes([0.14, 1.03, 0.8, 0.015])

# cbaxes = figure.add_axes([0.14, .905, 0.8, 0.015])
# cbaxes1 = figure.add_axes([0.14, 0.93, 0.8, 0.015])

# figure.subplots_adjust(hspace=0.1,top=0.9)

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["purple","white","green"])

im1=ax1.pcolor(Bs,mus,didV1,cmap='PRGn',vmin=0.0, vmax=4,edgeColors='none')  # BuPu seismic  PRGn
im2=ax2.pcolor(Bs,mus,didV2,cmap='PRGn',vmin=0.0, vmax=4,edgeColors='none')  # seismic  PRGn
im3=ax3.pcolor(Bs,mus,didV3,cmap='PRGn',vmin=0.0, vmax=4,edgeColors='none')  # seismic  PRGn

im4=ax4.contourf(Bs,mus,didV1,[0,1.9,2.1,4],colors = ["#E4EBF2","#0343DF","#FFFF14"],vmin=0.0, vmax=4,extend='neither')
im5=ax5.contourf(Bs,mus,didV2,[0,1.9,2.1,4],colors = ["#E4EBF2","#0343DF","#FFFF14"],vmin=0.0, vmax=4,extend='neither')
im6=ax6.contourf(Bs,mus,didV3,[0,1.9,2.1,4],colors = ["#E4EBF2","#0343DF","#FFFF14"],vmin=0.0, vmax=4,extend='neither')
#["#E4EBF2","#0343DF","#FFFF14"]

# cbar1=figure.colorbar(im1,ax=ax1,location='top',extend='max', spacing='proportional',
#                      ticks=[0.01,0.25],pad=-2.5*10**(-2),aspect=15,shrink=0.9,) 
# cbar1.ax.set_xticklabels([ '0.01', '0.25'])
# cbar1.set_label('$E_0(meV)$', labelpad=0, rotation=0,fontsize=22) # labelpad=-40, y=-0.02,
line,=ax1.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3,label=r'$1 \times V_{imp1}$')
ax1.legend(handles=[line],loc='lower left',bbox_to_anchor=(0,.0),
                  handlelength=0,handletextpad=0,fontsize=20)

ax1.set_xticks((0, 1, 2, 3))
ax1.set_xticklabels(['','','',''])
ax1.set_yticks((-2,0,2,4,6))
# ax1.set_yticklabels(['','','','',''])

ax1.set_xlabel('',family='Times New Roman') # ,**csfont
ax1.set_ylabel('$\mu (meV)$',family="Times New Roman" ) #,**csfont
ax1.set_xlim([-0.0,3.0])
ax1.set_ylim([-3.0,7.0])

line,=ax2.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3,label=r'$2.5 \times V_{imp1}$')
ax2.legend(handles=[line],loc='lower left',bbox_to_anchor=(0,.0),
                  handlelength=0,handletextpad=0,fontsize=20)
# cbar2=figure.colorbar(im2,ax=ax2,location='top',extend='max', spacing='proportional',
#                      ticks=[0,2,4],pad=-0*10**(-2),aspect=15,shrink=0.9,) 
# cbar2.ax.set_xticklabels(['0', '2', '4'])
# cbar2.set_label(r'$G(\frac{e^2}{h})$', labelpad=0, x=0.72,rotation=0,fontsize=22)
ax2.set_xticks((0, 1, 2, 3))
ax2.set_xticklabels(['','','',''])
ax2.set_yticks((-2,0,2,4, 6))
ax2.set_yticklabels(['','','','',''])
ax2.set_xlabel('',family='Times New Roman') # ,**csfont
ax2.set_ylabel('',family="Times New Roman" ) #,**csfont
ax2.set_xlim([-0.,3.])
ax2.set_ylim([-3.,7.])


line,=ax3.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3,label=r'$5 \times V_{imp1}$')
ax3.legend(handles=[line],loc='lower left',bbox_to_anchor=(0,.0),
                  handlelength=0,handletextpad=0,fontsize=20)
ax3.set_xticks((0, 1, 2, 3))
ax3.set_xticklabels(['','','',''])
ax3.set_yticks((-2,0,2,4, 6))
ax3.set_yticklabels(['','','','',''])

ax3.set_xlabel('',family='Times New Roman') # ,**csfont
ax3.set_ylabel('',family="Times New Roman" ) #,**csfont
ax3.set_xlim([-0.,3.])
ax3.set_ylim([-3.,7.])


ax4.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3)
ax4.set_xticks((0, 1, 2, 3))
ax4.set_yticks((-2,0,2,4, 6))
# ax4.set_yticklabels(['','','','',''])
ax4.set_ylabel('$\mu (meV)$',family="Times New Roman" ) #,**csfont
ax4.set_xlim([-0.,3.])
ax4.set_ylim([-3.,7.])
ax4.set_xlabel('$\Gamma (meV)$',family='Times New Roman') # ,**csfont

ax5.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3)
ax5.set_yticks((-2,0,2,4, 6))
ax5.set_xticks((0, 1, 2, 3))
ax5.set_yticklabels(['','','','',''])
ax5.set_xlim([-0.,3.])
ax5.set_ylim([-3.,7.])
ax5.set_xlabel('$\Gamma (meV)$',family='Times New Roman') # ,**csfont



    
cbar3=plt.colorbar(im3,cax=cbaxes, orientation = 'horizontal',ticks=[0,2,4], spacing='proportional',)
cbar3.ax.set_xticklabels(['', '', '']) #'0', '2', '4'
cbar3.ax.xaxis.set_ticks_position("top")

cbar6=plt.colorbar(im6,cax=cbaxes1, orientation = 'horizontal',ticks=[0,2,4], spacing='proportional',)
cbar6.ax.set_xticklabels(['0', '2', '4']) #'0', '2', '4'

cbar6.ax.xaxis.set_ticks_position("top")

cbar6.set_label(r'$G(e^2/h)$',verticalalignment='center', 
                labelpad=-3.5*10,x=.75,rotation=0,fontsize=22)

# cbar3=figure.colorbar(im3,ax=[ax1,ax2,ax3],location='top',extend='max', spacing='proportional',
#                       ticks=[0,2,4],pad=0*10**(-2),aspect=50,shrink=0.9,) 
# cbar3.ax.set_xticklabels(['', '', '']) #'0', '2', '4'
# # cbar3.set_label(r'$G(e^2/h)$',verticalalignment='center', labelpad=2.5*10**(-2), x=0.75,rotation=0,fontsize=22)

# cbar6=figure.colorbar(im6,ax=[ax1,ax2,ax3],location='top',extend='neither', spacing='proportional',
#                       ticks=[0,2,4],pad=2*10**(-2),aspect=50,shrink=0.9,) 
# cbar6.ax.set_xticklabels(['', '', ''])
# cbar6.set_label(r'$G(e^2/h)$',verticalalignment='center', labelpad=2*10**(-2), x=.75,rotation=0,fontsize=22)
# # line,=ax6.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3)



line,=ax6.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3,label=r'$5 \times V_{imp1}$')  
ax6.plot([0,0.2],[1.6,1.6],'-',linewidth=5,color='slategrey')
ax6.plot([0,0.2],[4.3,4.3],'-',linewidth=5,color='magenta')

 
ax6.set_yticks((-2,0,2,4, 6))
ax6.set_yticklabels(['','','','',''])
ax6.set_xticks((0, 1, 2, 3))
ax6.set_xlim([-0.,3.])
ax6.set_ylim([-3.,7.])
ax6.set_xlabel('$\Gamma (meV)$',family='Times New Roman') # ,**csfont

plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
plt.rcParams['axes.linewidth'] = 1.5

plt.show()
figure.savefig('Fig4.png', format='png', dpi=400,bbox_inches = 'tight')