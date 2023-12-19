"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""




from numpy import array




"""                             F_Kepler
                            -----------------
                Inputs: U, t
                Outputs: F(U,t) : Function dU/dt = F(U,t)
"""


def F_Kepler(U, t): 
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2+y**2)**1.5
    return array([vx, vy, -x / mr, -y / mr])
