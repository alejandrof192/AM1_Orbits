"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                         test             MUSE                                                                                                                                                                    #
"""

from re import A, U
from numpy import array, zeros
import matplotlib.pyplot as plt
from numba import njit
from scipy.linalg.blas import dtbmv
from scipy.optimize import fsolve, newton
from numpy import matmul, array, zeros, float64, dot, empty
from numpy.linalg import norm 
from time_domain import equispaced_time_domain
from Kepler_Problem import F_Kepler
from temporal_schemes import Euler, Crank_Nicolson, RK4


"""
                   Cauchy_Problem
            -----------------------------
    Inputs:  
           F(U,t) : Function dU/dt = F(U,t) 
           time_domain : time partition t (vector of length N+1)
           U0 : initial condition at t=0
           temporal_scheme
           

    Return: 
           U: matrix[N+1, Nv], Nv state values at N+1 time steps     
 """



def Cauchy_Problem(time_domain, temporal_scheme, F, U0):

    U = array(zeros([len(time_domain), 4]))
    U[0,:] = U0    

    for i in range(0, len(time_domain)-1):
        U[i+1, :] = temporal_scheme(U = U[i, :], t1 = time_domain[i] , t2 = time_domain[i+1] , F = F )
    return U



################################### Temporal scheme and initial condition setup ###################################

time_domain = array(zeros(10000))
time_domain = equispaced_time_domain(N=10000, dt=0.01)

U0 = ([1, 0, 0, 1])

temporal_scheme = RK4

###################################################################################################################


U = Cauchy_Problem(time_domain, temporal_scheme=temporal_scheme, F=F_Kepler, U0=U0)

# Force of the Kepler Movement

F = array(zeros([len(time_domain), 4]))

for i in range(0,len(time_domain)):
    F[i,:] = F_Kepler(U[i,:], time_domain)

    



#####################################################  PLOTS  #####################################################

# Plotting orbit with 'i' scheme

plt.plot(U[:,0], U[:,1], color='blue')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
if temporal_scheme == Euler:
    plt.legend(['Euler'])
elif temporal_scheme == Crank_Nicolson:
    plt.legend(['Crank-Nicolson'])
elif temporal_scheme == RK4:
    plt.legend(['Runge-Kutta'])    
plt.show()



# All schemes within the same plot

U = Cauchy_Problem(time_domain = time_domain, temporal_scheme = Euler, F = F_Kepler, U0 = U0)
plt.plot(U[:,0], U[:,1], label = 'Euler', color = 'blue')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_Problem(time_domain = time_domain, temporal_scheme = Crank_Nicolson, F = F_Kepler, U0 = U0)
plt.plot(U[:,0], U[:,1], label = 'Crank-Nicolson', color = 'red')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_Problem(time_domain = time_domain, temporal_scheme = RK4, F = F_Kepler, U0 = U0)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4', color = 'yellow')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

plt.show()



 # Same scheme with different inputs

N = 100000

t1 = equispaced_time_domain(N=N, dt=0.01)
t2 = equispaced_time_domain(N=N, dt=0.001)
t3 = equispaced_time_domain(N=N, dt=0.0001)


U = Cauchy_Problem(time_domain = t1, temporal_scheme = RK4, F = F_Kepler, U0 = U0)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4, dt=0.01, N=100000', color = 'blue') 
plt.grid()
plt.title('Orbit') , 
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_Problem(time_domain = t2, temporal_scheme = RK4, F = F_Kepler, U0 = U0)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4, dt=0.001, N=100000', color = 'red')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_Problem(time_domain = t3, temporal_scheme = RK4, F = F_Kepler, U0 = U0)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4, dt=0.0001, N=100000', color = 'green')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

plt.show()

