

"""noo
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""

from re import A
from numpy import array, zeros
import matplotlib.pyplot as plt
from numba import njit
from scipy.optimize import fsolve, newton
from numpy import matmul, array, zeros, float64, dot, empty   
from numpy.linalg import norm 
from temporal_schemes.temporal_schemes import Cauchy_problem, Euler, Crank_Nicolson, RK4


N = 10000
dt = 0.01
U_i = array([1,0,0,1])

"""
TEMPORAL SCHEME SELECTION
In order to choose the temporal scheme, the user has three different options:
1) Euler
2) Crank-Nicolson
3) Runge-Kutta 4th order
"""

scheme = 1

U = Cauchy_problem(N, dt, U_i, scheme)



# Plotting orbit with 'i' scheme

plt.plot(U[:,0], U[:,1], color='blue')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
if scheme == 1:
    plt.legend(['Euler'])
elif scheme == 2:
    plt.legend(['Crank-Nicolson'])
elif scheme == 3:
    plt.legend(['Runge-Kutta'])    
plt.show()



# All schemes in one plot

U = Cauchy_problem(N, dt, U_i, 1)
plt.plot(U[:,0], U[:,1], label = 'Euler', color = 'blue')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_problem(N, dt, U_i, 2)
plt.plot(U[:,0], U[:,1], label = 'Crank-Nicolson', color = 'red')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_problem(N, dt, U_i, 3)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4', color = 'yellow')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

plt.show()



 # Same schemes with different inputs

U = Cauchy_problem(100000, 0.01, U_i, 3)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4, dt=0.01, N=100000', color = 'blue') 
plt.grid()
plt.title('Orbit') , 
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_problem(100000, 0.001, U_i, 3)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4, dt=0.001, N=100000', color = 'red')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

U = Cauchy_problem(100000, 0.0001, U_i, 3)
plt.plot(U[:,0], U[:,1], label = 'Runge-Kutta 4, dt=0.0001, N=100000', color = 'green')
plt.grid()
plt.title('Orbit')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis('equal')
plt.legend()

plt.show()
    
