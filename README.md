Lab 1: Numerical Integration Methods
 This lab explores numerical methods for approximating definite integrals: the rectangle, trapezoidal, and Simpson's methods. It calculates the integral of $$f(x)=x^3$$ 
 over a user-defined range and visualizes convergence and error analysis for each method using matplotlib.

Lab 2: Error Analysis
 This lab focuses on analyzing the true and estimated errors for numerical integration methods. It compares the errors of the trapezoidal and Simpson's methods with theoretical predictions, demonstrating how precision improves with increased subintervals.

Lab 3: Calculation of a definite integral
 The method is used to iteratively solve the system of equations 𝐴*𝑋=𝐵. Each iteration updates the solution vector 𝑋 by solving for each unknown sequentially, using the values from the previous iteration for other unknowns. The algorithm stops when the solution 
 converges or the maximum iteration count is reached.
 
Lab 4: Calculates errors using the Runge method for different time steps.
Visualizes error data for 9 numerical methods on logarithmic scales.
Euler Method for ODE (Other Inputs):

Solves 𝑑𝑇/𝑑𝑡 = −0.0059𝑇 using the explicit Euler method.
Compares the numerical solution with the analytical solution 
𝑇(𝑡) = 𝑇0𝑒^(−𝑘𝑡) via plots.

Lab 5: Numerical analysis of temperature evolution T(t), described by the equation 
𝑑𝑇/𝑑𝑡=−0.0059𝑇, and evaluates errors in numerical methods. The user can choose between visualizing errors (local and Runge) or solving the equation using the second-order Adams-Bashforth method.

In the graph mode (g/G), it plots the comparison of local errors and Runge errors for data with a time step Δ𝑇=100. In calculation mode (c/C), the differential equation is solved numerically: the first step uses Euler's method, and subsequent steps use the Adams-Bashforth method. Results are visualized as a temperature evolution graph over time.

Lab 6: This code numerically solves a system of differential equations modeling heat exchange between two objects with temperatures 
𝑇1(𝑡) and 𝑇2(𝑡). The equations are: 𝑑𝑇1/𝑑𝑡=0.01(𝑇2−𝑇1), 𝑑𝑇2/𝑑𝑡=0.01(𝑇1−𝑇2),
where 0.01 is the heat exchange rate.

The solution starts with initial conditions 𝑇1(0)=100 and 𝑇2(0)=0. Using Euler’s explicit method with a time step of h=1, the code iteratively calculates how temperatures evolve over time. The graph visualizes the results, showing 𝑇1(𝑡) decreasing and 𝑇2(𝑡) increasing until they reach equilibrium.
