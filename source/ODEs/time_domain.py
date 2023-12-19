"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import array, zeros




"""
                   equispaced_time_domain
            --------------------------------------
    Inputs:  
           N: Number of points in the temporal partition
           dt: Time step
           

    Return: 
           t: Array of length N representing the equispaced temporal partition
 """


def equispaced_time_domain(N, dt):
    
    t = array(zeros(N))
    
    for i in range(0, N-1):
        t[i+1] = t[i] + dt
        
    return t
