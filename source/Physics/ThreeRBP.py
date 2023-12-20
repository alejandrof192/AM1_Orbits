"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import sqrt, array, zeros
from scipy.optimize import fsolve
from numpy.linalg import eig
from ODEs.Maths_Resources import Jacobian




"""
                   CR3BP
            --------------------------------------
    Inputs:  
           U: State vector [x, y, dx/dt, dy/dt]
           mu: Mass ratio parameter
           

    Return: 
           Array representing the derivatives of the Circular Restricted Three-Body Problem
 """


def CR3BP(U, mu):
    r = U[0:2]          # Position vector            
    drdt = U[2:4]       # Velocity vector

    # Positions 1 and 2
    r1 = sqrt((r[0]+mu)**2 + r[1]**2)       
    r2 = sqrt((r[0]-1+mu)**2 + r[1]**2)

    # Accelerations 1 and 2
    dvdt_1 = - (1 - mu)*(r[0] + mu)/(r1**3) - mu*(r[0] - 1 + mu)/(r2**3)
    dvdt_2 = - (1 - mu)*r[1]/(r1**3) - mu*r[1]/(r2**3)

    return array([drdt[0], drdt[1], 2*drdt[1] + r[0] + dvdt_1, -2*drdt[0] + r[1] + dvdt_2])



"""
                   Lagrange_points
            --------------------------------------
    Inputs:  
           U_0: Initial guesses for Lagrange points
           Np: Number of Lagrange points (Np <= 5)
           mu: Mass ratio parameter
           

    Return: 
           Array representing the Lagrange points obtained by solving the system of equations
 """


def Lagrange_points(U_0, Np, mu):
    
    L_P = zeros([5,2])

    def F(Y):
        X = zeros(4)
        X[0:2] = Y
        X[2:4] = 0
        FX = CR3BP(X, mu)
        return FX[2:4]
   
    for i in range (Np):
        L_P[i,:] = fsolve(F, U_0[i,0:2])

    return L_P




"""
                   Stability_LP
            --------------------------------------
    Inputs:  
           U_0: Lagrange points
           mu: Mass ratio parameter
           

    Return: 
           Array representing the eigenvalues of the Jacobian matrix evaluated at the Lagrange points
 """


def Stability_LP(U_0, mu):

    def F(Y):
        return CR3BP(Y, mu)

    A = Jacobian(F, U_0)
    values, vectors = eig(A)

    return values