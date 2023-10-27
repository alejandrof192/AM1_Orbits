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



def Euler(U, t1, t2, F):
    
    return U + (t2 - t1) * F(U, t1)



def Crank_Nicolson(U, t1, t2, F):
    
    def Residual_CN(X): 
         
         return  X - a - (t2 - t1)/2 *  F(X, t2)

    a = U  +  (t2 - t1)/2 * F(U, t1)
    return newton( Residual_CN, U )



def RK4(U, t1, t2, F ): 

     k1 = F( U, t1)
     k2 = F( U + (t2 - t1) * k1/2, t1 + (t2 - t1)/2 )
     k3 = F( U + (t2 - t1) * k2/2, t1 + (t2 - t1)/2 )
     k4 = F( U + (t2 - t1) * k3,   t1 + (t2 - t1)   )
 
     return  U + (t2 - t1) * ( k1 + 2*k2 + 2*k3 + k4 )/6
