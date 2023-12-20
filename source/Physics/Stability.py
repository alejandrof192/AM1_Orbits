
"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import array, float64, zeros



"""
                   System_matrix
            --------------------------------------
    Inputs:  
           F: Function representing the system of ODEs
           U0: Initial condition
           t: Time
           

    Return: 
           A: Jacobian matrix of the system evaluated at U0 and t
 """

def System_matrix( F, U0, t ): 
   
     eps = 1e-6 
     N = len(U0) 
     A =  zeros( (N, N), dtype=float64)
     delta = zeros(N) 
     
     for j in range(N):  
         
         delta[:] = 0 
         delta[j] = eps 
         A[:, j] = ( F( U0 + delta, t ) - F( U0 - delta, t ) )/(2*eps)
  
     return A 



"""
                   Oscillator
            --------------------------------------
    Inputs:  
           U: State vector
           t: Time
           

    Return: 
           Array representing the derivatives of the simple oscillator system
 """



def Oscillator(U,t): 

   return array( [ U[1], -U[0] ] ) 





"""
                   test_system_matrix
            --------------------------------------
    Outputs:  
           Prints the Jacobian matrix of the oscillator system at the initial condition and time
 """


def test_system_matrix(): 

    U0 = array( [ 0., 0. ] ) 
    t = 0. 
    A = System_matrix(Oscillator,  U0, t)
    print("A=", A)
