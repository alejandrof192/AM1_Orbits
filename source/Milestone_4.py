"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import  linspace, transpose
from ODEs.temporal_schemes import Euler, RK4, Crank_Nicolson 
import matplotlib.pyplot as plt
from Physics.Stability_Region import Stability_Region


# Plotting Stability Region

rho, x, y  = Stability_Region(RK4, 100, -4, 2, -4, 4)
plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
plt.axis('equal')
plt.grid()
plt.show()