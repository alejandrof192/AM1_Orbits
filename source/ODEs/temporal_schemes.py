"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""



from scipy.optimize import newton
from numpy import linspace, zeros
from ODEs.ERK_Functions import RK_stages, butcher, StepSize




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



# Embedded Runge-Kutta (order 3)

def ERK(U, t1, t2, F ):

    tol = 1e-9
    
    # Calculates Runge-Kutta of order 1 and order 2 
    stage1 = RK_stages(1, U, t1, t2-t1, F)  
    stage2 = RK_stages(2, U, t1, t2-t1, F) 
    
    # Define the butcher array
    orders, Ns, a, b, bs, c = butcher()
    
    # Determine the minimum step size between dt and the stepsize, which compares the error with the tolerance
    h = min(t2-t1, StepSize(stage1 - stage2, tol, t2-t1,  min(orders)))
    N_n = int(t2-t1/h) + 1        # Number of steps to update solution U2
    n_dt = t2-t1 / int(N_n)           
    stage1 = U
    stage2 = U

    for i in range(N_n):
        time = t1 + i * n_dt
        stage1 = stage2
        stage2 = RK_stages(1, stage1, time, n_dt, F)
        
    # Final solution
    U2 = stage2
    
    ierr = 0

    return U2




#===============================================================================
# METODO ADAMS-BASHFORTH DE ORDEN 4

def G(U, t1, t2 , F): 

    N = len(U)
    t_old = 0

    if t1 < t_old or t_old == 0:
        U2 = U + (t2-t1) * F(U,t1)
    else:
        U2 = U0 + 2 * (t2-t1) * F(U,t1)
        U0 = U

    t_old = t1 + (t2-t1)
    return U2

def AB4_(U, t1, t2, F):
    N = len(U)
    history = []

    if len(history) < 4:
        # Utiliza Euler para los primeros pasos si no hay suficientes datos
        if len(history) == 0:
            history.append(U)
        for _ in range(3 - len(history)):
            U_next = U + (t2-t1) * F(U, t1)
            history.append(U_next)
            U = U_next
            t1 += (t2-t1)

        return U_next

    # Adams-Bashforth de cuarto orden
    f0 = F(history[-1], t1 - 3 * (t2-t1))
    f1 = F(history[-2], t1 - 2 * (t2-t1))
    f2 = F(history[-3], t1 - (t2-t1))
    f3 = F(history[-4], t1)

    U_next = U + ((t2-t1) / 24) * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)
    history.append(U_next)
    return U_next


def AB4(U, t1, t2, F):
 
    N = len(U)
    if t1 == 0:
    
        global previous_U 
        global previous_U_state
        previous_U = zeros([3,N])
        previous_U_state = zeros([3,1])
 
    # Si hay resultados anteriores faltantes, utiliza Euler para calcularlos
    if any(previous_U_state == 0):
        for ii in range(3):
            if previous_U_state[ii] == 0:
                # Calcula los primeros pasos con el método de Euler
                previous_U[ii,:] = F(U, t1)
                previous_U_state[ii] = 1
                return (U + (t2-t1) * previous_U[ii,:]) # Devuelve el resultado final después de los primeros pasos
 
    # Almacena los valores de previous_U en unas variables auxiliares
    Un3 = previous_U[0,:]
    Un2 = previous_U[1,:]
    Un1 = previous_U[2,:]
 
    # Adams-Bashforth de cuarto orden
    f0 = Un3
    f1 = Un2
    f2 = Un1
    f3 = F(U, t1)
 
    # Actualiza el historial eliminando el resultado más antiguo y agregando el nuevo
    previous_U[0,:] = Un2
    previous_U[1,:] = Un1
    previous_U[2,:] = f3
 
    return U + ((t2-t1) / 24) * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)


