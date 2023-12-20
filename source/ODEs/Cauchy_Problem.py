"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import array, zeros


"""
                   Cauchy_Problem
            -----------------------------
    Inputs:  
           F(U,t) : Function dU/dt = F(U,t) 
           time_domain : time partition t (vector of length N+1)
           U0 : initial condition at t=0
           temporal_scheme
           

    Return: 
           U: matrix[N+1, Nv], Nv state values at N+1 time steps     
 """



def Cauchy_Problem(time_domain, temporal_scheme, F, U0):

    U = array(zeros([len(time_domain), 4]))
    U[0,:] = U0    

    for i in range(0, len(time_domain)-1):
        U[i+1, :] = temporal_scheme(U = U[i, :], t1 = time_domain[i] , t2 = time_domain[i+1] , F = F )
    return U



def Cauchy_Problem_NBody_Problem(time_domain, temporal_scheme, F, U0):

    U = array(zeros([len(time_domain), 24]))
    U[0,:] = U0    

    for i in range(0, len(time_domain)-1):
        U[i+1, :] = temporal_scheme(U = U[i, :], t1 = time_domain[i] , t2 = time_domain[i+1] , F = F )
    return U


