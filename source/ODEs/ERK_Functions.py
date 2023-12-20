"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""



from numpy import zeros, matmul
from numpy.linalg import norm



"""
                   RK_stages
            --------------------------------------
    Inputs:  
           order: Order of accuracy for the method (1 or 2)
           U1: State vector at the current time step
           t: Current time
           dt: Time step size
           F: Function representing the system of ODEs
           

    Return: 
           U2: State vector at the next time step
 """
 
def RK_stages(order, U1, t, dt, F):
    
    orders, Ns, a, b, bs, c = butcher()
    
    Nk = len(U1)
    k = zeros([Ns, Nk])
    
    k[0,:] = F(U1, t + c[0]*dt)

    if order == 1:
        for i in range(1,Ns):
            
            Up = U1
            
            for j in range(i):
                
                Up = Up + dt * a[i,j] * k[j,:]
                
            k[i,:] = F(Up, t + c[i]*dt)
            
        
        U2 = U1 + dt*matmul(b,k)

    elif order == 2:
        for i in range(1,Ns):
            
            Up = U1
            
            for j in range(i):
                
                Up = Up + dt * a[i,j] * k[j,:]
                
            k[i,:] = F(Up, t + c[i]*dt)
            
        U2 = U1 + dt*matmul(bs,k)

    return U2




"""
                   StepSize
            --------------------------------------
    Inputs:  
           dU: Difference between two solutions
           tol: Tolerance for adaptive step size
           dt: Current time step
           orders: Orders of accuracy
           

    Return: 
           step_size: Adaptive time step size
 """
 

def StepSize(dU, tol, dt, orders): 
    error = norm(dU)

    if error > tol:
        step_size = dt*(tol/error)**(1/(orders+1))
    else:
        step_size = dt

    return step_size




"""
                   butcher
            --------------------------------------
    Return: 
           orders: List of orders of accuracy
           Ns: Number of stages in the Runge-Kutta method
           a: Coefficient matrix for the primary stage
           b: Coefficient vector for the primary stage
           bs: Coefficient vector for the embedded stage
           c: Coefficient vector for time integration
 """
 

def butcher():
 

    orders = [2, 1]     
    Ns = 2

    a = zeros([Ns, Ns-1])
    b = zeros([Ns])
    bs = zeros([Ns])
    c = zeros([Ns])

    c = [0., 1.]
    a[0, :] = [0.]
    a[1, :] = [1.]
    b[:] = [1./2, 1./2]
    bs[:] = [1., 0.]

    return orders, Ns, a, b, bs, c