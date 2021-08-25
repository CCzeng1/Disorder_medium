# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:35:59 2021

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:26:20 2021

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:12:13 2021

@author: admin
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.colors as colors
import matplotlib


didV=Vimp0=np.loadtxt(open("Fig4_ap5.csv","rb"),delimiter=",",skiprows=0)
d2=np.transpose(didV.reshape(301,501))


didV=Vimp0=np.loadtxt(open("Fig5_Vimp2_ap5.csv","rb"),delimiter=",",skiprows=0)
d1=np.transpose(didV.reshape(301,501))


didV=Vimp0=np.loadtxt(open("Fig5_Vimp3_ap5.csv","rb"),delimiter=",",skiprows=0)
d3=np.transpose(didV.reshape(301,501))


didV=Vimp0=np.loadtxt(open("Fig5_Vimp4_ap5.csv","rb"),delimiter=",",skiprows=0)
d4=np.transpose(didV.reshape(301,501))


didV=np.loadtxt(open("Fig5_Vimp2_ap5.csv","rb"),delimiter=",",skiprows=0)
didV1=np.transpose(didV.reshape(301,501))
didV=np.loadtxt(open("Fig4_ap5.csv","rb"),delimiter=",",skiprows=0)
didV2=np.transpose(didV.reshape(301,501))
didV=np.loadtxt(open("Fig5_Vimp3_ap5.csv","rb"),delimiter=",",skiprows=0)
didV3=np.transpose(didV.reshape(301,501))
didV=np.loadtxt(open("Fig5_Vimp4_ap5.csv","rb"),delimiter=",",skiprows=0)
didV4=np.transpose(didV.reshape(301,501))


Ds=[d1,d2,d3,d4]
indexs=[[231,366],[272,435],[270,365],[370,449]]
didVs=[didV1,didV2,didV3,didV4]
labels=[[r'$\mu=1.60$',r'$\mu=4.30$'],[r'$\mu=2.44$',r'$\mu=5.70$'],
        [r'$\mu=2.40$',r'$\mu=4.30$'],[r'$\mu=4.40$',r'$\mu=5.98$']]

Gs=[[0.57,2.00],[1.75,2.80],[1.08,2.0],[1.1,2.55]]
Gsindexs=[[58,215],[186,280],[116,200],[96,253]]
pos=['upper center','lower left','upper right','upper right']
shifts=[[0.45,1.05],[-0.02,-0.1],[1.02,1.05],[0.8,1.05]]

Bs=np.linspace(0,3,301)
mus=np.linspace(-3,7,501)

figsize=10,12
figure, axs = plt.subplots(4,3,constrained_layout=True,
                           figsize=figsize,gridspec_kw={'width_ratios': [2.5, 1,1]})
# plt.subplots_adjust(wspace=0.15,hspace=0.15)

for i in range(3):
    for j in range(4):
        ax=axs[j,i]
        d=Ds[j]
        ax.set_xticks((0,1,2,3))
        ax.set_yticklabels('')
        ax.set_xticklabels('')

        if i==0:
            ax.plot([0,3],[2,2],'--',color='silver',linewidth=4)
            line1,=ax.plot(Bs,d[indexs[j][0]],color="slategrey",linewidth=3,label=labels[j][0])
            line2,=ax.plot(Bs,d[indexs[j][1]],color="magenta",linewidth=3,label=labels[j][1])
            
            ax.plot(Bs[Gsindexs[j][0]],d[indexs[j][0]][Gsindexs[j][0]],marker='^',color='r',markersize=10)
            ax.plot(Bs[Gsindexs[j][1]],d[indexs[j][1]][Gsindexs[j][1]],marker='^',color='b',markersize=10)
            
            ax.legend(handles=[line1,line2],loc=pos[j],bbox_to_anchor=(shifts[j][0],shifts[j][1]),
                  handlelength=0.8,handletextpad=0.2,fontsize=18,facecolor='none') #,bbox_to_anchor=(0, 0)
            
            
            ax.set_xlim([0,3])
            ax.set_ylim([0,4])
            ax.set_ylabel('$G(e^2/h)$',family='Times New Roman')
            ax.set_yticks((0,2,4))
            ax.set_yticklabels(['0','2','4'])
            
        if i==1:
            ax.contourf(Bs,mus,didVs[j],[0,1.9,2.1,4],
                        colors = ["#E4EBF2","#0343DF","#FFFF14"],vmin=0.0, vmax=4,extend='neither')
        
            line,=ax.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000',
                          linewidth=3,label=r'$5 \times V_{imp1}$')  
            ax.plot([0,3],[mus[indexs[j][0]],mus[indexs[j][0]]],'--',linewidth=3,color='slategrey')
            ax.plot([0,3],[mus[indexs[j][1]],mus[indexs[j][1]]],'--',linewidth=3,color='magenta')
            ax.set_xlim([0,3])
            ax.set_ylim([-0.3+mus[indexs[j][0]],0.3+mus[indexs[j][0]]])
            ax.set_ylabel('$\mu(meV)$',family='Times New Roman')
            
        if i==2:
            ax.contourf(Bs,mus,didVs[j],[0,1.9,2.1,4],
                        colors = ["#E4EBF2","#0343DF","#FFFF14"],vmin=0.0, vmax=4,extend='neither')
        
            line,=ax.plot(np.sqrt(mus**2+0.3**2),mus,color='#FF0000',
                          linewidth=3,label=r'$5 \times V_{imp1}$')  
            ax.plot([0,3],[mus[indexs[j][0]],mus[indexs[j][0]]],'--',linewidth=3,color='slategrey')
            ax.plot([0,3],[mus[indexs[j][1]],mus[indexs[j][1]]],'--',linewidth=3,color='magenta')
            ax.set_xlim([0,3])
            ax.set_ylim([-0.3+mus[indexs[j][1]],0.3+mus[indexs[j][1]]])
            
        if i!=0 and j==3:
            ax.set_xticklabels(['0','','2',''])
            ax.set_xlabel('$\Gamma (meV)$',family='Times New Roman')
        if i==0 and j==3:
            ax.set_xticks((0,1,2,3))
            ax.set_xticklabels(['0','1','2','3'])
            ax.set_xlabel('$\Gamma (meV)$',family='Times New Roman')
        


plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
# plt.rcParams['axes.linewidth'] = 1.5

plt.show()
figure.savefig('Fig6_md1.png', format='png', dpi=400)


