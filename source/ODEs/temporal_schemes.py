"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""







from scipy.optimize import  newton




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



def Adams_Moulton(F, t1, t2, U1, N):
    def runge_kutta_4th_order(F, U, t, dt):
        k1 = dt * F(U, t)
        k2 = dt * F(U + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * F(U + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * F(U + k3, t + dt)
        return (k1 + 2*k2 + 2*k3 + k4) / 6.0

    dt = (t2 - t1) / N
    t_values = linspace(t1, t2, N + 1)

    U_values = [U1]

    for i in range(N):
        F1 = runge_kutta_4th_order(F, U1, t_values[i], dt)
        
        if i == 0:
            U2 = [U1[j] + dt * F1[j] for j in range(len(U1))]
        elif i == 1:
            F0 = F1
            U2 = [U1[j] + dt/2 * (3 * F1[j] - F0[j]) for j in range(len(U1))]
        else:
            F0, Fm1 = F1, F0
            U2 = [U1[j] + dt/12 * (23 * F1[j] - 16 * F0[j] + 5 * Fm1[j]) for j in range(len(U1))]

        U_values.append(U2)
        U1 = U2

    return U_values
