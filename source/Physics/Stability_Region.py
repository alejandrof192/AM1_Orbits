"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import zeros, linspace, abs, float64
from ODEs.temporal_schemes import Euler, RK4, Crank_Nicolson 



"""
                   Stability_Region
            --------------------------------------
    Inputs:  
           Scheme: Function representing the numerical scheme
           N: Number of points in the x and y directions
           x0, xf: Range for the x-axis
           y0, yf: Range for the y-axis
           

    Return: 
           rho: 2D array representing the stability region
           x: 1D array representing the x-axis values
           y: 1D array representing the y-axis values
 """



def Stability_Region(Scheme, N, x0, xf, y0, yf): 

    x, y = linspace(x0, xf, N), linspace(y0, yf, N)
    rho =  zeros( (N, N),  dtype=float64)

    for i in range(N): 
      for j in range(N):

          w = complex(x[i], y[j])
          r = Scheme( 1., 1., 0., lambda u, t: w*u )
          rho[i, j] = abs(r) 

    return rho, x, y  


 



