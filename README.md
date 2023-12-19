# Instituto Universitario Ignacio da Riva
## Master Universitario en Sistemas Espaciales
### Alejandro Fernandez Ruiz
#### MUSE

---

In the initial section, you will find the **`ODEs`:** directory, housing the following modules:

- **`Cauchy_Problem`:** Implementation of a numerical solver designed for solving ordinary differential equations (ODEs) utilizing the Cauchy problem approach.

- **`Temporal_Schemes`:** Diverse numerical methods for solving ordinary differential equations (ODEs), each offering distinct approaches based on factors such as accuracy, stability, and efficiency.

- **`time_domain`:** This function generates an equispaced temporal partition for a specified number of points (N) and time step (dt). It is commonly employed in numerical simulations requiring uniform time sampling.

- **`Error`:** These functions are crafted for analyzing the convergence behavior of a temporal scheme when solving Cauchy problems. The `Error_Cauchy_Problem` function computes the error and corrected solution for a given scheme, while the `Temporal_convergence_rate` function estimates the temporal convergence rate through iterative refinement of the temporal partition.

---

On the other hand, within the **`Physics`:** directory, various modules associated with the physics of the problem are stored:

- **`Stability`:** Functions related to the stability analysis of a system of ordinary differential equations (ODEs). The `System_matrix` function calculates the Jacobian matrix of the system at a given state (U0) and time (t). The `Oscillator` function represents a simple oscillator system. The `test_system_matrix` function is a test case demonstrating the usage of the `System_matrix` function with the `Oscillator` system. This analysis is commonly used in stability studies, particularly when considering linearization around equilibrium points to understand the system's behavior.

- **`Stability_Region`:** This function visualizes the stability region of a numerical scheme in the complex plane. It computes the stability region by evaluating the scheme's stability function over a grid of complex values. The resulting 2D array rho represents the magnitude of the stability function at each point in the complex plane. The function returns the stability region (rho) and the corresponding `\(x^2\)` and `\(y^2\)` axis values.

- **`Kepler_Problem`:** The `F_Kepler` function represents the right-hand side of the system of ordinary differential equations (ODEs) for the two-dimensional Kepler problem. The input U is a state vector [x, y, vx, vy] representing the position and velocity components in the x and y directions. The function computes and returns the derivatives of each component with respect to time, defining the dynamics of the Kepler problem.

- **`NBody_Problem`:** The primary purpose of this code is to simulate the dynamic behavior of an N-body system interacting gravitationally. This simulation is crucial for understanding and visualizing the orbits and complex interactions between celestial bodies, such as planets in a solar system or stars in a galaxy. The code provides a tool for studying the temporal evolution of a gravitationally interactive system.

---

In addition, you will find various milestones achieved throughout the course:

- Milestone_2 (also includes 1)
- Milestone_3
- Milestone_4
- Milestone_5
- Milestone_6
