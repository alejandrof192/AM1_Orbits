"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""

from re import U
from numpy import array, zeros
import matplotlib.pyplot as plt
from numpy import array, zeros  
from ODEs.Cauchy_Problem import Cauchy_Problem
from ODEs.temporal_schemes import Euler, RK4, Crank_Nicolson
from ODEs.time_domain import equispaced_time_domain
from Physics.Kepler_Problem import F_Kepler




################################### Temporal scheme and initial condition setup ###################################
N = 10000
time_domain = array(zeros(10000))
time_domain = equispaced_time_domain(N=N, dt=0.01)

U0 = array([1, 0, 0, 1])

temporal_scheme = Euler

###################################################################################################################


U = Cauchy_Problem(time_domain, temporal_scheme=temporal_scheme, F=F_Kepler, U0=U0)

# Force of the Kepler Movement

F = array(zeros([len(time_domain), 4]))

for i in range(0,len(time_domain)):
    F[i,:] = F_Kepler(U[i,:], time_domain)

    

####################################################  PLOTS  #####################################################

#Plotting orbit with 'i' scheme

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






