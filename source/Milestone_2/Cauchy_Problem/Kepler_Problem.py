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



"""                             F_Kepler
                            -----------------
                Inputs: U, t
                Outputs: F(U,t) : Function dU/dt = F(U,t)
"""


def F_Kepler(U, t): 
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2+y**2)**1.5
    return array([vx, vy, -x / mr, -y / mr])
