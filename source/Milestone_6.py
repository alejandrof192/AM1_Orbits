"""
                          Instituto Universitario de Microgravedad Ignacio Da Riva (IDR)
                          -------------------------------------------------------------                          
                                      Subject: Ampliacion de Matematicas I               
                                       
                                        Author: Alejandro Fernandez Ruiz  
                                                      MUSE                                                                                                                                                                    #
"""


from numpy import zeros, linspace, random
from ODEs.Cauchy_Problem import Cauchy_Problem
from Physics.ThreeRBP import CR3BP, Lagrange_points, Stability_LP
from ODEs.temporal_schemes import Euler, RK4, Crank_Nicolson, ERK
import matplotlib.pyplot as plt



mu = 1.2151e-2 


N = int(10000)
t = linspace(0, 10, N)
Np = 5         




U_0 = zeros([Np, 4])

U_0[0, :] = [0.1, 0, 0, 0]
U_0[1, :] = [0.8, 0.6, 0, 0]
U_0[2, :] = [-0.1, 0, 0, 0]
U_0[3, :] = [0.8, -0.6, 0, 0]
U_0[4, :] = [1.01, 0, 0, 0]


LP = Lagrange_points(U_0, Np, mu)


print("Lagrange Points:")
for i, point in enumerate(LP, start=1):
    print(f"LP{i} =", point)


selected_point = input("Enter the number of the desired Lagrange point in order to study its stability: ")

try:
    selected_point_index = int(selected_point)

    
    if 1 <= selected_point_index <= len(LP):
        selected_lagrange_point = LP[selected_point_index - 1]
        print(f"Lagrange Point {selected_point_index}: {selected_lagrange_point} selected")
    else:
        print("Invalid selection. Please enter a valid Lagrange point number.")
except ValueError:
    print("Invalid input. Please enter a number.")
    


U0 = zeros(4)
U0[0:2] = LP[selected_point_index - 1,:]
perturbation = 1e-4*random.random()             
U0 = U0 + perturbation


def F(U,t):
   return CR3BP(U, mu)



U = Cauchy_Problem(t, ERK, F, U0)


U0_stab = zeros(4)
U0_stab[0:2] = LP[selected_point_index - 1, :]
eingvalues = Stability_LP(U0_stab, mu)
#print(around(eingvalues.real, 8))

#  Plot the results

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(U[:, 0], U[:, 1], '-', color="red")
ax1.plot(-mu, 0, 'o', color="purple")
ax1.plot(1 - mu, 0, 'o', color="green")
for i in range(Np):
    ax1.plot(LP[i, 0], LP[i, 1], 'o', color="black")

ax2.plot(U[:, 0], U[:, 1], '-', color="red")

ax2.plot(LP[selected_point_index - 1, 0], LP[selected_point_index - 1, 1], 'o', color="black")
fig.suptitle(f"Orbit around Lagrange Point {selected_point_index}")


ax1.set_title("Orbital view, with the solutions from solving the Cauchy problem")
ax2.set_title("Lagrange point orbit")

for ax in fig.get_axes():
    ax.set(xlabel='x', ylabel='y')
    ax.grid()

plt.show()
