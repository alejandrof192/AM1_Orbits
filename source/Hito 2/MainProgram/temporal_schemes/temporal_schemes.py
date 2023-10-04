
"""
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


def F_Kepler(U, t): 
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2+y**2)**1.5
    return array([vx, vy, -x / mr, -y / mr])



def Euler(U, t, dt, F):
    
    return U + dt * F(U, t)



def Crank_Nicolson(U, dt, t, F):
    
    def Residual_CN(X): 
         
         return  X - a - dt/2 *  F(X, t + dt)

    a = U  +  dt/2 * F(U, t)
    return newton( Residual_CN, U )



def RK4(U, dt, t, F ): 

     k1 = F( U, t)
     k2 = F( U + dt * k1/2, t + dt/2 )
     k3 = F( U + dt * k2/2, t + dt/2 )
     k4 = F( U + dt * k3,   t + dt   )
 
     return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6



def Cauchy_problem(N, dt, U_i, scheme):
    
    U = array(zeros([N,4]))
    U[0,:] = U_i
    
    if scheme == 1:
        
        for i in range(0, N-1):
            t = i*dt
            U[i+1,:] = Euler(U[i,:], t, dt, F_Kepler)
            
    elif scheme == 2:
        
        for i in range(0, N-1):
            t = i*dt
            U[i+1,:] = Crank_Nicolson(U[i,:], dt, t, F_Kepler)
            
    elif scheme == 3:
        
        for i in range(0, N-1):
            t = i*dt
            U[i+1,:] = RK4(U[i,:], dt, t, F_Kepler)     
        
    return U
            