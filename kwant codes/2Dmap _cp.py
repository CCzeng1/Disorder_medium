import time
start = time.time()

## necessary modules
import kwant
import numpy as np
import tinyarray as ty
import matplotlib.pyplot as plt
import scipy.sparse.linalg as sla
import scipy.linalg as la

## for parallel running
from concurrent import futures
from functools import partial

## define the pauli matrices
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.array([[1,0],[0,-1]])
s0=np.array([[1,0],[0,1]])


# the main body defining Hamiltonian
def make_sys(mu, Zeeman):
    #print(Zeeman)
    
    ### in mev or in delta (SC pairing potential)
    t=12.7*4     ## hopping amplitute
    alpha=2.5*2  ## SOC strength
    delta=0.3    ## SC gap
    W=1          ## length in y-direction
    mu=mu        ## chemical potential
                 ## mu =2,3, 4, 5 2.5
    U=6+mu       ## tunneling barrier 
    El=0         ## gate voltage, sometimes make chaneges to the transport
    a=0.5        ## lattice constant in nm, sometimes a=1 nm, 10 angstrom
    B=Zeeman     ## Magnetic field
    N=400        ## total site number, equal to length /a
    
    width=4      ## width for applying the tunnel barrier
    Disp=eta     ## dissipation
    Vimp=amps*Vimp0   ## impurity, amps indicates the amplitude
   
    
   
    lat_e=kwant.lattice.square(a,name='e')
    lat_h=kwant.lattice.square(a,name='h')
    
    sys=kwant.Builder()
     
    ## function to introduce the disorders on chemical potential
    def potential(site):
        xs=[i/2 for i in range(N)]
        data=[]
        for i in range(len(Vimp)):
            data.append(Vimp[i]) 
        index=xs.index(site.pos[0])   
        return data[index]
        
    ### onsite energy for nanowire 
    def onsite_e(site):
        return B*sx-(mu+potential(site))*s0+2*t*s0-1j*Disp
    def onsite_h(site):
        return B*sx+(mu+potential(site))*s0-2*t*s0-1j*Disp
    
    ###  onsite enery for tunneling part by adding U (tunneling)
    def onsite_el(site):
        return B*sx-(mu+potential(site))*s0+2*t*s0+U*s0-1j*Disp
    def onsite_hl(site):
        return B*sx-(-(mu+potential(site))*s0+2*t*s0+U*s0)-1j*Disp
    
        
    ### onsite
    sys[(lat_e(x,y)for x in range(N) for y in range(W))]=onsite_e
    sys[(lat_h(x,y)for x in range(N) for y in range(W))]=onsite_h
    
    sys[(lat_e(i,j)for i in range(width) for j in range(W))]=onsite_el
    sys[(lat_h(i,j)for i in range(width) for j in range(W))]=onsite_hl
    
    ### hopping, one can also define the terms on rhs as a function
    sys[kwant.builder.HoppingKind((1,0),lat_e,lat_e)]=-t*s0-1j*alpha*sy
    sys[kwant.builder.HoppingKind((0,1),lat_e,lat_e)]=-t*s0+1j*alpha*sx
    
    sys[kwant.builder.HoppingKind((1,0),lat_h,lat_h)]=t*s0+1j*alpha*sy
    sys[kwant.builder.HoppingKind((0,1),lat_h,lat_h)]=t*s0-1j*alpha*sx
    
    ### SC pairing potential
    sys[((lat_e(x,y),lat_h(x,y))for x in range(N) for y in range(W))]=delta*s0
    
    sym=kwant.TranslationalSymmetry((-a,0))
    lead0=kwant.Builder(sym)
    lead1=kwant.Builder(sym)
    
    ### define lead,  onsite and hoppings 
    lead0[(lat_e(0,y)for y in range(W))]=1*B*sx-mu*s0+2*t*s0+El*s0
    lead1[(lat_h(0,y)for y in range(W))]=1*B*sx-(-mu*s0+2*t*s0+El*s0)
    
    lead0[((lat_e(1,j),lat_e(0,j))for j in range(W))]=-t*s0-1j*alpha*sy
    lead1[((lat_h(1,j),lat_h(0,j))for j in range(W))]=t*s0+1j*alpha*sy
    
    ### first consider a single lead tunneling experiment
    sys.attach_lead(lead0)
    sys.attach_lead(lead1)
    
    ### multi-lead cases, can also be defined, 
    ### attahced to any position of the nanowire
    #sys.attach_lead(lead0.reversed())
    #sys.attach_lead(lead1.reversed())

    return sys


###############################################################################
  
def Bands(Zeeman0):     ## function to calculate the band structure
    #Energy=[]
    sys=make_sys(Zeeman=Zeeman0)
    sys=sys.finalized()
    #Zeemans=np.linspace(0,6,51)
    N=sys.graph.num_nodes
    
    ham=sys.hamiltonian_submatrix(args=[Zeeman0],sparse=False)
        #eval=sla.eigsh(ham,k=15,which='SM',return_eigenvectors=False)
    eval,evec=la.eigh(ham)
        #eval,evec=np.linalg.eigh(ham)
    #Energy.append(eval)
        
    return eval    ## eigen vectors can also been given by this func.

def Spectrum():  ## func for band structure
    
    Zeemans=np.linspace(0,6,301)
    data=[]
    with futures.ProcessPoolExecutor(max_workers=24) as executor:
      for result in executor.map(Bands,Zeemans):
          data.append(result)
    
    return data
###############################################################################
    
###################################============================================  
## different ways to deal with the conductance 

# def plot_conductance_old(sys,T0):
#     sys=sys.finalized()
#     data=[]
#     #print(len(Vbias))
#     for i in range(len(Vbias)):
#         energy=Vbias[i]
#         smatrix=kwant.smatrix(sys,energy,check_hermiticity=False)
#         data.append(smatrix.submatrix(0,0).shape[0]+smatrix.transmission(1,0)-smatrix.transmission(0,0))    
#     #data_t=Tem_G(data,T0=T0)   
#     data_t=dIdV_eff(G0=data,Rs0=Rs,T0=T0)
#     return data_t


# def plot_conductance(sys,T0):
#     sys=sys.finalized()
#     data=[]
#     Vbiascp=np.asarray(Vbias)
    
#     nmid=int(len(Vbias)/2)
#     idx=np.abs(Vbiascp-Rs/2).argmin()    ## here, Rs needs a definition before being called
#     Vidx=np.arange(nmid+2,idx)
    
#     for i in Vidx:
#         energy=Vbias[i]
#         smatrix=kwant.smatrix(sys,energy,check_hermiticity=False)
#         data.append(smatrix.submatrix(0,0).shape[0]+smatrix.transmission(1,0)-smatrix.transmission(0,0))    

#     return np.sum(data)/len(data)    
      
 
# def dIdV_eff(G0,Rs0,T0):
#     if T0 !=0:
#         G0=Tem_G(G0,T0=T0)
        
#     Vbiascp=np.asarray(Vbias)
#     #Vbiascp1=[i for i in Vbias]
#     nmid=int(len(Vbias)/2)
#     G0=np.array(G0) 
#     idx=np.abs(Vbiascp-Rs0/2).argmin()
#     nmid=int(len(Vbias)/2)
#     Vidx=np.arange(nmid+2,idx)
#     #Vs=Vbiascp[Vidx]
#     Gs=G0[Vidx]
#     return np.sum(Gs)/len(Gs)
######################################=========================================


def plot_conductance_updd(sys,T0):  ## here we count several sample points and take the max

    sys=sys.finalized()
    data=[]
    for i in range(len(Vbias)):
        energy=Vbias[i];
        smatrix=kwant.smatrix(sys,energy,check_hermiticity=False)  ## in the presence of dissipation
        data.append(smatrix.submatrix(0,0).shape[0]+smatrix.transmission(1,0)-smatrix.transmission(0,0))    
    return np.max(data)     
    #return np.sum(data)/len(data)   ## one can also try the average, but not solid

def Tem_G(G0,T0):  ## temperature integral 
    if T0==0: 
        return G0
    ### for a given V we need get a factor G(e) as a function of epsilon
    G_T=[]
    factor=[]
    Vbias0=np.linspace(0,1,1)  ## we focus on the zero-bias peak, Vbias=0
    for v in Vbias0:
        factor_v=[]
        for i in range(len(energies)):  
            x0=G0[i]
            e=energies[i]     ## represent for the incident energy
            x1=Dif_ferm(v,e,T0)
            factor_v.append(x1*x0)
        temp=np.trapz(factor_v,energies)
        G_T.append(temp)
    return G_T
    
def Dif_ferm(Vbias,energy,T0):   ## temperature factor 
    
    T=1.72*10**(-3)*T0/20## this value is for Temperature at 20mK
    bias=np.abs((Vbias-energy)/T)
    if bias>20:
        return 0
    else:
        return 1/(4*T*(np.cosh((Vbias-energy)/(2*T)))**2)


def calc(mus0, Zeeman0):  
    sys=make_sys(mu=mus0, Zeeman=Zeeman0)
    cond_z0=plot_conductance_updd(sys,T0=0)
    #cond_z0=plot_conductance(sys,Vbias,T0=0)
    return cond_z0  


def conductances():   ## func for conductance
 
    data_total=[]
    
    for Zeeman in Zeemans:
      with futures.ProcessPoolExecutor(max_workers=28) as executor:
        for result in executor.map(partial(calc,Zeeman0=Zeeman),mus):
          data_total.append(result)
        
    return data_total
   

###############################################################################    
import random as rd
def Vimpfun(N, nd, lambda0):    ## ways to define a random function
    Nd=np.int(nd*2) 

    Vimps=np.zeros(x.size)
    for i in range(Nd):
        x0=rd.randrange(10,N)
        #xs.append(x0)
        A0=rd.normalvariate(0,1)
        if np.abs(A0)>1:
            A0=0
        #As.append(A0)
        Vimps=Vimps+A0*np.exp(-np.abs(x-x0)/(lambda0/5))
    
    return Vimps*V0
###############################################################################


## paras for disorder function, as given in the paper    
N=400  ## total site number
V0=5   ## ampltitude
nd=40  ## number density, or the number of disorders
lambda0=30  ## decay length for disorders

x=np.linspace(0,399,400)

###############======== To generate the disorder function
#Vimp0=Vimpfun(N,nd,lambda0)
#np.savetxt('Vimp_t4030.csv',Vimp0,delimiter=',')

###############========= To apply a given disorder function
Vimp0=np.loadtxt(open("Vimp2.csv","rb"),delimiter=",",skiprows=0)



## paras for the phase maps, namely, vbias, zeemans, etc.
energies=np.linspace(-0.25,0.25,1501)
Vbias=np.linspace(0,16,9)*10**(-3)

Zeemans=np.linspace(15,25.0,501)
mus=np.linspace(-3,6.0,201)

eta=0.4*10**(-3)  ## dissipation 
amps=5            ## amplitute of disorder

data=conductances()  ## similarly, use Spectrum and Bands can calculate the band strcuture and wavefunction


data=np.array(data)
np.savetxt('test_RjV3_3_cp1.csv',data,delimiter=',') # expect to see some islands. 
end = time.time()
print('The elapsed time is ...\n')
print(end - start)


