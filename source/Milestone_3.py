"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import array, zeros
import matplotlib.pyplot as plt
from numpy import  array, zeros  
from ODEs.time_domain import equispaced_time_domain
from Physics.Kepler_Problem import F_Kepler
from ODEs.temporal_schemes import Euler, Crank_Nicolson, RK4
from ODEs.Error import Error_Cauchy_Problem, Temporal_convergence_rate


################################### Temporal scheme and initial condition setup ###################################
N = 10000
time_domain = array(zeros(10000))
time_domain = equispaced_time_domain(N=N, dt=0.01)
U0 = array([1, 0, 0, 1])
order = 1
m = 5

temporal_scheme = Euler


##################################################### Error Plot ##################################################

print("Error Kepler orbit ") 
Error, U = Error_Cauchy_Problem( time_domain, F_Kepler,  Euler, order, U0 )

plt.plot(time_domain, Error[:,0] )
plt.axis('equal')
plt.grid()
plt.show()

print("Order Euler ") 
order, log_e, log_n = Temporal_convergence_rate( time_domain, F_Kepler, U0, Euler, m )

print( "order =", order)
plt.plot(log_n, log_e )
plt.axis('equal')
plt.grid()
plt.show()





