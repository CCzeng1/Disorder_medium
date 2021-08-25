# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:57:05 2021

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



Gs1=np.loadtxt(open("added_Fig7a_Us_mu1p6.csv","rb"),delimiter=",",skiprows=0)
Gs1cp=np.loadtxt(open("Fig7_Us_mu1p6.csv","rb"),delimiter=",",skiprows=0)
Gs2=np.loadtxt(open("added_Fig7a_Us_mu4p3.csv","rb"),delimiter=",",skiprows=0)
#Gs3=np.loadtxt(open("Fig7_Us_mu5p0.csv","rb"),delimiter=",",skiprows=0)

#Gs1=np.loadtxt(open("Fig7b_Us_mu3p78.csv","rb"),delimiter=",",skiprows=0)
Gs3=np.loadtxt(open("added_Fig7b_Us_mu2p44.csv","rb"),delimiter=",",skiprows=0)
Gs4=np.loadtxt(open("Fig7b_Us_mu5p7.csv","rb"),delimiter=",",skiprows=0)

#Gs1=np.loadtxt(open("Fig7c_Us_mu5p4.csv","rb"),delimiter=",",skiprows=0)
Gs5=np.loadtxt(open("added_Fig7c_Us_mu2p4.csv","rb"),delimiter=",",skiprows=0)
Gs6=np.loadtxt(open("Fig7c_Us_mu4p3.csv","rb"),delimiter=",",skiprows=0)


#Gs1=np.loadtxt(open("Fig7d_Us_mu4p4.csv","rb"),delimiter=",",skiprows=0)
Gs7=np.loadtxt(open("added_Fig7d_Us_mu4p4.csv","rb"),delimiter=",",skiprows=0)
Gs8=np.loadtxt(open("Fig7d_Us_mu5p98.csv","rb"),delimiter=",",skiprows=0)

Us=np.linspace(0,40,81)


Ds=[[Gs1cp,Gs2],[Gs3,Gs4],[Gs5,Gs6],[Gs7,Gs8]]



labels=[[r'$\mu=1.60,\Gamma=0.57$',r'$\mu=4.30,\Gamma=2.15$'],
        [r'$\mu=2.44,\Gamma=1.86$',r'$\mu=5.70,\Gamma=2.80$'],
        [r'$\mu=2.40,\Gamma=1.16$',r'$\mu=4.30,\Gamma=2.00$'],
        [r'$\mu=4.40,\Gamma=0.96$',r'$\mu=5.98,\Gamma=2.55$']]

label0=[r'$5 \times V_{imp1}$',r'$5 \times V_{imp2}$',
        r'$5 \times V_{imp3}$',r'$5 \times V_{imp4}$']

# indexs=[[231,366],[272,435],[270,365],[371,448]]
# Gs=[[0.57,2.00],[1.75,2.80],[1.08,2.0],[1.1,2.55]]
# Gsindexs=[[58,200],[175,280],[108,200],[110,253]]
# pos=['upper center','lower left','upper right','upper right']
# shifts=[[0.45,1.05],[-0.02,-0.1],[1.02,1.05],[0.8,1.05]]

# Bs=np.linspace(0,3,301)
# mus=np.linspace(-3,7,501)

figsize=10,7
figure, axs = plt.subplots(2,2,constrained_layout=True,
                           figsize=figsize,gridspec_kw={'width_ratios': [1,1]})
# plt.subplots_adjust(wspace=0.15,hspace=0.15)

for i in range(2):
    for j in range(2):
        ax=axs[j,i]
        d=Ds[2*i+j]
        ax.set_yticks((0,2,4))
        ax.set_xticks((0,10,20,30,40))
        ax.set_yticklabels('')
        ax.set_xticklabels('')


        line0,=ax.plot([0,40],[2,2],'--',color='silver',linewidth=4,label=label0[2*i+j])
        line2,=ax.plot(Us,d[1],color="blue",linewidth=1.5,marker='^',markersize=8,label=labels[j+2*i][1])
        line1,=ax.plot(Us,d[0],color="red",linewidth=1.5,marker='^',markersize=8,label=labels[j+2*i][0])
        
        # ax.plot(Bs[Gsindexs[j][0]],d[indexs[j][0]][Gsindexs[j][0]],marker='^',color='r',markersize=10)
        # ax.plot(Bs[Gsindexs[j][1]],d[indexs[j][1]][Gsindexs[j][1]],marker='^',color='b',markersize=10)
        # ax.legend(handles=[line0],loc='lower left',edgecolor='none',
        #       handlelength=0,handletextpad=0.5,fontsize=18,facecolor='none') 
        
        ax.annotate(label0[2*i+j],xy=(20,2.25),xytext=(20,2.25),fontsize=20)
        ax.legend(handles=[line1,line2],loc='best',
              handlelength=1.2,handletextpad=0.5,fontsize=18,facecolor='none',edgecolor='none') 
        #,bbox_to_anchor=(0, 0)
        # bbox_to_anchor=0*(shifts[j][0],shifts[j][1]),    
            
        ax.set_xlim([-0.1,40.1])
        ax.set_ylim([-0.1,4.1])
            # ax.set_ylabel('$G(e^2/h)$',family='Times New Roman')
            # ax.set_yticks((0,2,4))
            # ax.set_yticklabels(['0','2','4'])
        
            
        if i==0 :
            ax.set_yticklabels(['0','2','4'])
            ax.set_ylabel('$G(e^2/h)$',family='Times New Roman')
        if j==1 :
            ax.set_xticks((0,10,20,30,40))
            ax.set_xticklabels(['0','10','20','30','40'])
            ax.set_xlabel('$U_{barrier}(meV)$',family='Times New Roman')
        


plt.rcParams["font.family"] = "Times New Roman" #Times New Roman
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.size"] =25
plt.tick_params(labelsize=25)
# plt.rcParams['axes.linewidth'] = 1.5

plt.show()
figure.savefig('Fig9_md1.png', format='png', dpi=400)


