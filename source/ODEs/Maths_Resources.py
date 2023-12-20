"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import array, zeros, size 


"""
                   Jacobian
            --------------------------------------
    Inputs:  
           F: Function representing the system of ODEs
           U: State vector
           

    Return: 
           Jac: Jacobian matrix of the system evaluated at U
 """
 

def Jacobian(F, U):
	N = size(U)
	Jac = zeros([N,N])
	t = 1e-10

	for i in range(N):
		xj = zeros(N)
		xj[i] = t
		Jac[:,i] = (F(U + xj) - F(U - xj))/(2*t)
	return Jac


