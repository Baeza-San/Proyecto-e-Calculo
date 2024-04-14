from scipy.integrate import quad
import sympy as sp
from sympy import symbols, integrate, exp


#Funcion que deceamos integrar.
def f(x):
    return x**2

#Pedimos el los valores de la integral. 

a = int(input("Dame el valor a de la integral: "))
b = int(input("Dame el valor b de la integral: "))

ResulDeLaInetregal, error = quad(f, a, b)

print("El resulta de la integral defina es: ", ResulDeLaInetregal)

#Prueva de integral por partes

# Definir las variables
x = symbols('x')

# Definir las funciones u y dv
u = x
dv = exp(x)

# Calcular du y v
du = u.diff(x)
v = integrate(dv, x)

# Aplicar la fórmula de integración por partes: ∫udv = uv - ∫vdu
integral = u*v - integrate(v*du, x)

print(integral)

