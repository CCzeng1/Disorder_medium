# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:18:34 2021

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:42:36 2021

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:35:46 2021

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
from textwrap import fill


xs=np.loadtxt(open("position.csv","rb"),delimiter=",",skiprows=0)


m1=np.loadtxt(open("added_Vimp1_mode1_r.csv","rb"),delimiter=",",skiprows=0)
m1cp=np.loadtxt(open("Vimp1_mode1_r.csv","rb"),delimiter=",",skiprows=0)
m2=np.loadtxt(open("added_Vimp1_mode2_r.csv","rb"),delimiter=",",skiprows=0)
m2cp=np.loadtxt(open("Vimp1_mode2_r.csv","rb"),delimiter=",",skiprows=0)

m3=np.loadtxt(open("added_Vimp1_mode2_b.csv","rb"),delimiter=",",skiprows=0)
m4=np.loadtxt(open("added_Vimp1_mode1_b.csv","rb"),delimiter=",",skiprows=0)


m5=np.loadtxt(open("added_Vimp2_mode1_r.csv","rb"),delimiter=",",skiprows=0)
m6=np.loadtxt(open("added_Vimp2_mode2_r.csv","rb"),delimiter=",",skiprows=0)
m7=np.loadtxt(open("Vimp2_mode1_b.csv","rb"),delimiter=",",skiprows=0)
m8=np.loadtxt(open("Vimp2_mode2_b.csv","rb"),delimiter=",",skiprows=0)

m9=np.loadtxt(open("added_Vimp3_mode1_r.csv","rb"),delimiter=",",skiprows=0)
m10=np.loadtxt(open("added_Vimp3_mode2_r.csv","rb"),delimiter=",",skiprows=0)
m11=np.loadtxt(open("Vimp3_mode1_b.csv","rb"),delimiter=",",skiprows=0)
m12=np.loadtxt(open("Vimp3_mode2_b.csv","rb"),delimiter=",",skiprows=0)

m13=np.loadtxt(open("added_Vimp4_mode1_r.csv","rb"),delimiter=",",skiprows=0)
m14=np.loadtxt(open("added_Vimp4_mode2_r.csv","rb"),delimiter=",",skiprows=0)
m15=np.loadtxt(open("Vimp4_mode1_b.csv","rb"),delimiter=",",skiprows=0)
m16=np.loadtxt(open("Vimp4_mode2_b.csv","rb"),delimiter=",",skiprows=0)


modes=[[[m1cp,m2cp],[m4,m3]],
       [[m5,m6],[m7,m8]],
       [[m9,m10],[m11,m12]],
       [[m13,m14],[m15,m16]]]


# Ds=[[Gs1,Gs2],[Gs3,Gs4],[Gs5,Gs6],[Gs7,Gs8]]



labels=[[r'$5 \times V_{imp1}: \mu=1.60,\Gamma=0.57$',
         r'$5 \times V_{imp1}: \mu=4.30,\Gamma=2.15$'],
        [r'$5 \times V_{imp2}: \mu=2.44,\Gamma=1.86$',
         r'$5 \times V_{imp2}: \mu=5.70,\Gamma=2.80$'],
        [r'$5 \times V_{imp3}: \mu=2.40,\Gamma=1.16$',
         r'$5 \times V_{imp3}: \mu=4.30,\Gamma=2.00$'],
        [r'$5 \times V_{imp4}: \mu=4.40,\Gamma=0.96$',
         r'$5 \times V_{imp4}: \mu=5.98,\Gamma=2.55$']]


labelss=[[r'$\mu=1.60,\Gamma=0.57$',r'$\mu=4.30,\Gamma=2.00$'],
        [r'$\mu=2.44,\Gamma=1.75$',r'$\mu=5.70,\Gamma=2.80$'],
        [r'$\mu=2.40,\Gamma=1.08$',r'$\mu=4.30,\Gamma=2.00$'],
        [r'$\mu=4.40,\Gamma=1.10$',r'$\mu=5.96,\Gamma=2.55$']]


label0=[r'$5 \times V_{imp1}$',r'$5 \times V_{imp2}$',
        r'$5 \times V_{imp3}$',r'$5 \times V_{imp4}$']

pos=['upper center','upper center','upper center','upper center',
     'upper left','upper left','upper right','upper right']
shifts=[[0.45,1.05],[-0.02,-0.1],[1.02,1.05],[0.8,1.05]]


# indexs=[[231,366],[272,435],[270,365],[371,448]]
# Gs=[[0.57,2.00],[1.75,2.80],[1.08,2.0],[1.1,2.55]]
# Gsindexs=[[58,200],[175,280],[108,200],[110,253]]
# pos=['upper center','lower left','upper right','upper right']
# shifts=[[0.45,1.05],[-0.02,-0.1],[1.02,1.05],[0.8,1.05]]

# Bs=np.linspace(0,3,301)
# mus=np.linspace(-3,7,501)

figsize=10,10
figure, axs = plt.subplots(4,2,constrained_layout=True,
                           figsize=figsize,gridspec_kw={'width_ratios': [1,1]})
# plt.subplots_adjust(wspace=0.15,hspace=0.15)

for i in range(4):
    for j in range(2):
        ax=axs[i,j]
        d=modes[i][j]
        ax.set_yticks(())
        ax.set_xticks((0,100,200))
        ax.set_yticklabels('')
        ax.set_xticklabels('')


        line0,=ax.plot([0,200],[0,0],'--',color='silver',linewidth=0.5,
                       label=labels[i][j])#fill(labels[j][0],20))
        # line1,=ax.plot(Us,d[0],color="red",linewidth=1.5,marker='^',markersize=8,label=labels[j][0])
        # line2,=ax.plot(Us,d[1],color="blue",linewidth=1.5,marker='^',markersize=8,label=labels[j][1])
        temp1=d[0]
        temp2=d[1]
        ax.fill_between(xs,temp1,facecolor='#FF0000',alpha=0.75,edgecolor='k',linewidth=1) 
        ax.fill_between(xs,temp2,facecolor='#FFFF00',alpha=0.6,edgecolor='k',linewidth=1)
    
        ax.legend(handles=[line0],loc='upper center',
              handlelength=1.2,handletextpad=0.5,fontsize=18,facecolor='none',edgecolor='none') 
        # ax.annotate(label0[i],xy=(100,.25),xytext=(100,.25),fontsize=20)
        # pos[i*2+j],
            
        ax.set_xlim([0,200])

            
        if j==0 :
            # ax.set_yticklabels(['0','2','4'])
            ax.set_ylabel('$\Psi(a.u.)$',family='Times New Roman')
        if i==3:
            # ax.set_xticks((0,10,20,30,40))
            ax.set_xticklabels(['0','1','2'])
            ax.set_xlabel('$Position(\mu m)$',family='Times New Roman')
        
m5cp=np.loadtxt(open("added_Vimp2_mode5_r.csv","rb"),delimiter=",",skiprows=0)
m6cp=np.loadtxt(open("added_Vimp2_mode6_r.csv","rb"),delimiter=",",skiprows=0)
        
m13cp=np.loadtxt(open("added_Vimp4_mode5_r.csv","rb"),delimiter=",",skiprows=0)
m14cp=np.loadtxt(open("added_Vimp4_mode6_r.csv","rb"),delimiter=",",skiprows=0)

# axs[1,0].fill_between(xs,m5cp,facecolor='mediumseagreen',alpha=0.75,
#                       edgecolor='k',linewidth=1,linestyle='--') 
axs[1,0].fill_between(xs,m6cp,facecolor='#00FFFF',alpha=0.6,
                      edgecolor='k',linewidth=1,linestyle='--')

# axs[3,0].fill_between(xs,m13cp,facecolor='mediumseagreen',alpha=0.75,
#                       edgecolor='k',linewidth=1,linestyle='--') 
axs[3,0].fill_between(xs,m14cp,facecolor='#00FFFF',alpha=0.6,
                      edgecolor='k',linewidth=1,linestyle='--')

# m13cp=np.loadtxt(open("Vimp4_mode1_rcp2.csv","rb"),delimiter=",",skiprows=0)
# m14cp=np.loadtxt(open("Vimp4_mode2_rcp2.csv","rb"),delimiter=",",skiprows=0)

# # axs[3,0].fill_between(xs,m14cp,facecolor='#FF0000',alpha=0.75,
# #                       edgecolor='k',linewidth=1,linestyle='--') 
# # axs[3,0].fill_between(xs,m13cp,facecolor='#FFFF00',alpha=0.6,
# #                       edgecolor='k',linewidth=1,linestyle='--')

plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
# plt.rcParams['axes.linewidth'] = 1.5

plt.show()
# figure.savefig('Fig8_md1.png', format='png', dpi=300)


