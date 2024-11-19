1st lab implements several numerical methods for finding the root of a given function $$f(x)=4x-ln(x)-5$$, which is solved for $$f(x)=0$$.The methods included are:
1. Bisection Metod $$-$$ Divides an interval and repeatedly narrows down the search range for the root based on the sign of the function at the endpoints.
2. Simple Iteration Method $$–$$ Uses a transformation function $$-$$Uses a transformation function $$g(x)$$ to iteratively update guesses for the root.
3. Newton-Raphson Method $$–$$ Utilizes the function and its derivative to refine the guess for the root using the formula $$x_{n+1}=x_n-f(x_n)/f'(x_n)$$
4. Secant Method $$–$$ Uses two initial guesses and approximates the derivative of the function to find the root.
5. Chord Method $$–$$ Similar to the Secant Method but uses the endpoints of an interval to iteratively update the root approximation.
6. Idrichli Method $$–$$ A variation of the secant method using two initial approximations.


Key Features:
  Target Function: x must be greater than zero due to the natural logarithm.
  User Input: The code allows the user to choose between the different root-finding methods, providing initial values for the methods where necessary (e.g., interval endpoints or initial guesses).
  Error Handling: Several checks are in place, including validation of initial conditions (e.g., ensuring valid intervals for methods like bisection, secant, and chord) and conditions for convergence.
  Iterations Tracking: Each method records the values of the function or approximations at each iteration, which are plotted after the method completes.
  Plotting: The plot_iterations function visualizes the progression of the root approximation across iterations for the selected method.

This code is intended to demonstrate and compare various root-finding methods using an example function. It allows users to experiment with different techniques and visualize the convergence behavior. 
This can be helpful for understanding numerical methods in calculus or for solving real-world problems where finding roots of nonlinear equations is required.
