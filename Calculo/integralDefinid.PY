from scipy.integrate import quad
import sympy as sp

#Integral definida
# Define la función que deseas integrar
def f(x):
    return x**2

# Define los límites de integración
a = 0  # límite inferior
b = 1  # límite superior

# Realiza la integral
resultado, error = quad(f, a, b)

print("El resultado de la integral es:", resultado)


#Integral por sustitucion
# Define las variables
x = sp.symbols('x')
u = x**2

# Define la función a integrar
f = 2*x*sp.exp(u)

# Realiza la sustitución
f_sub = f.subs(x**2, u)

# Realiza la integral
resultado = sp.integrate(f_sub, x)

print("El resultado de la integral es:", resultado)

