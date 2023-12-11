import sympy as sp

x, y = sp.symbols('x y')

expression = x**2 + y**2

derivative = sp.diff(expression, x) 
integral = sp.integrate(expression, y)  

print("Expression:", expression)
print("Derivative with respect to x:", derivative)
print("Integral with respect to y:", integral)
