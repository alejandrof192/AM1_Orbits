"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""

from re import A, U
from numpy import array, zeros
import matplotlib.pyplot as plt
from numba import njit
from scipy.linalg.blas import dtbmv
from scipy.optimize import fsolve, newton
from numpy import matmul, array, zeros, float64, dot, empty   
from numpy.linalg import norm 


def equispaced_time_domain(N, dt):
    
    t = array(zeros(N))
    
    for i in range(0, N-1):
        t[i+1] = t[i] + dt
        
    return t
