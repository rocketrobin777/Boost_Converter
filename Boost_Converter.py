"""@author: robin leuering"""

import numpy as np
import matplotlib.pyplot as plt

"""Differential equations"""

def current_calc(U0, UC, I, D, L, RL, RDS, dt):
    dI = (U0-(D*RDS+RL)*I-(1-D)*UC)/L   # Calc current slope
    return I+dI*dt                      # Calc current                            

def voltage_calc(UC, I, C, R, dt):  
    dUC = (I-UC/R)/C                    # Calc voltage slope   
    return UC+dUC*dt                    # Calc voltage

"""Time conditions"""
tsim =       5e-3           # Simulation duration
n    =        200           # Number of time steps
dt   = tsim/n               # Simulation step time
t    = np.arange(0,tsim,dt) # Time vector

"""System parameters"""      
L   =       50e-6       # Inductivity
RL  =      750e-3       # Internal inductor resistance
RDS =       50e-3       # Drain-Source resistance
R   =       500.0       # Load resistance
C   =      330e-6       # Capacity
D   =       50e-2       # Duty cycle

"""Source voltage"""
U0  =       100.0                       # Source DC voltage
U0  = U0*np.ones(n, dtype=float)        # Source voltage array
UN  = 0*U0;                          # Noise scale factor
U0  = U0+UN*np.random.random_sample(n)  # Add noise

"""System values"""
I   = np.zeros(n)                       # Initialize current vector
UC  = U0*np.ones(n)                     # Initialize voltage vector

"""Solve System"""
for i in range(1,n):
    I[i]  = current_calc(U0[i], UC[i-1], I[i-1], D, L, RL, RDS, dt)
    UC[i] = voltage_calc(UC[i-1], I[i], C, R, dt)

"""Visualization"""   
plt.figure()
plt.rcParams['figure.figsize'] = [16, 12]
plt.plot(t,U0,c='#000000',label='U0 [V]',linewidth=3.0)
plt.plot(t,UC,c='#284b64',label='Uc [V]',linewidth=3.0)
plt.plot(t,I,c='#ff0000',label='I [A]',linewidth=3.0)
plt.title('Boost Converter Math Model, D = '+str(100*D)+'%',fontsize=20)
plt.legend(loc='best',fontsize=16)
plt.grid(True)
plt.show()
