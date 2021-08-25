# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:25:47 2021

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

didV=np.loadtxt(open("Fig4_ap1.csv","rb"),delimiter=",",skiprows=0)
didV1=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig4_ap2p5.csv","rb"),delimiter=",",skiprows=0)
didV2=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig4_ap5.csv","rb"),delimiter=",",skiprows=0)
didV3=np.transpose(didV.reshape(301,501))


didV=np.loadtxt(open("Fig5_Vimp3_ap1.csv","rb"),delimiter=",",skiprows=0)
didV4=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig5_Vimp3_ap2p5.csv","rb"),delimiter=",",skiprows=0)
didV5=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig5_Vimp3_ap5.csv","rb"),delimiter=",",skiprows=0)
didV6=np.transpose(didV.reshape(301,501))


didV=np.loadtxt(open("Fig5_Vimp4_ap1.csv","rb"),delimiter=",",skiprows=0)
didV7=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig5_Vimp4_ap2p5.csv","rb"),delimiter=",",skiprows=0)
didV8=np.transpose(didV.reshape(301,501))

didV=np.loadtxt(open("Fig5_Vimp4_ap5.csv","rb"),delimiter=",",skiprows=0)
didV9=np.transpose(didV.reshape(301,501))

Bs=np.linspace(0,3,301)
mus=np.linspace(-3,7,501)

Ds=[didV1,didV2,didV3,didV4,didV5,didV6,didV7,didV8,didV9]
labels=[[r'$1 \times V_{imp2}$',r'$2.5 \times V_{imp2}$',r'$5 \times V_{imp2}$'],
        [r'$1 \times V_{imp3}$',r'$2.5 \times V_{imp3}$',r'$5 \times V_{imp3}$'],
        [r'$1 \times V_{imp4}$',r'$2.5 \times V_{imp4}$',r'$5 \times V_{imp4}$']]

figsize=10,18
figure, axs = plt.subplots(3,3,constrained_layout=True,figsize=figsize)

for i in range(3):
    for j in range(3):
        ax=axs[i,j]
        
 
        pcm =ax.contourf(Bs,mus,Ds[3*i+j],[0,1.9,2.1,4],
                         colors = ["#E4EBF2","#0343DF","#FFFF14"],
                         vmin=0.0, vmax=4,extend='neither')
        
        ax.set_xticks((0, 1, 2, 3))
        ax.set_xticklabels(['','','',''])

        # ax.annotate(labels[i][j], (0.2, -2.5), backgroundcolor='w',fontsize=20,family='Times New Roman')

        if i==2:
            ax.set_xticklabels(['0','1','2','3'])
            ax.set_xlabel('$\Gamma (meV)$',family='Times New Roman') # ,**csfont
        ax.set_yticks((-2,0,2,4,6))
        if j==0:
            ax.set_yticklabels(['-2','0','2','4','6'])
            ax.set_ylabel('$\mu (meV)$',family="Times New Roman" ) #,**csfont
        else:    
            ax.set_yticklabels(['','','','',''])
            ax.set_ylabel('',family="Times New Roman" ) #,**csfont
            
        line,=ax.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000', linewidth=3,label=labels[i][j])  
        
        ax.legend(handles=[line],loc='lower left',#bbox_to_anchor=(-0.04, -0.03),
                  handlelength=0,handletextpad=0,fontsize=20) #,facecolor='none'
        # ax.text('Vimp1')
        ax.set_xlim([-0.,3.])
        ax.set_ylim([-3.,7.])



cbar=figure.colorbar(pcm, ax=axs[0, :], location='top',extend='max', spacing='proportional',
                     ticks=[0,2,4],pad=0.2*10**(-2),aspect=75,shrink=0.9)
cbar.ax.set_xticklabels(['0', '2', '4'])
cbar.set_label(r'$G(e^2/h)$',verticalalignment='center', labelpad=-5, x=0.75,rotation=0,fontsize=22)

axs[1,2].plot([0,0.2],[2.4,2.4],'-',linewidth=5,color='slategrey')
axs[1,2].plot([0,0.2],[4.3,4.3],'-',linewidth=5,color='magenta')

axs[0,2].plot([0,0.2],[2.44,2.44],'-',linewidth=5,color='slategrey')
axs[0,2].plot([0,0.2],[5.7,5.7],'-',linewidth=5,color='magenta')

axs[2,2].plot([0,0.2],[4.4,4.4],'-',linewidth=5,color='slategrey')
axs[2,2].plot([0,0.2],[5.98,5.98],'-',linewidth=5,color='magenta')


plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
plt.rcParams['axes.linewidth'] = 1.5

# figure.tight_layout()
# plt.legend()
plt.show()


# figure.savefig('Fig5_md.png', format='png', dpi=400)