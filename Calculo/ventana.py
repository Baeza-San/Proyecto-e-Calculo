from scipy.integrate import quad
import scipy.integrate
import sympy as sp
from tkinter import *
from tkinter import messagebox

#Funciones para intregral.
def IntegralDefinida(x):
    return x**2

def Calculo():  
 
    ValorA = float(EntradaDeDatoa.get()) 
    ValorB = float(EntradaDeDatob.get())
        
    ResulDeLaInetregal, error = quad(IntegralDefinida, ValorA, ValorB)
    Resultado_Integral.delete(0, 'end')  # Borra el contenido actual
    Resultado_Integral.insert(0, ResulDeLaInetregal)  # Inserta el nuevo resultado

#Ventanas
Menuin_principal = Tk()
Menuin_principal.title("Calculo Integral")
Menuin_principal.minsize(width=300, height=400)
Menuin_principal.config(padx=35, pady=35)

etiq1 = Label(text="Programa que resuelve una integral Definida.", font=("Arial", 14))
etiq1.grid(column=0, row=1)
Enblanco = Label(text=" ", font=("Arial", 14))
Enblanco.grid(column=0, row=2)

etiq2 = Label(text="Dame el valor de a:", font=("Arial", 14))
etiq2.grid(column=0, row=3)
EntradaDeDatoa = Entry(width=10, font=("Arial", 14))
EntradaDeDatoa .grid(column=1, row=3)
Enblanco = Label(text=" ", font=("Arial", 14))
Enblanco.grid(column=0, row=4)


etiq3 = Label(text="Dame el valor de b:", font=("Arial", 14))
etiq3.grid(column=0, row=5)
EntradaDeDatob = Entry(width=10, font=("Arial", 14))
EntradaDeDatob.grid(column=1, row=5)
Enblanco = Label(text=" ", font=("Arial", 14))
Enblanco.grid(column=0, row=6)

etiq4 = Label(text="El resultado es: ", font=("Arial", 14))
etiq4.grid(column=0, row=7)
Resultado_Integral = Entry(width=10, font=("Arial", 14))
Resultado_Integral.grid(column=1, row=7)

Enblanco = Label(text=" ", font=("Arial", 14))
Enblanco.grid(column=0, row=9)
boton1 = Button(text="Aceptar", font=("Arial", 14), command=Calculo)
boton1.grid(column=0, row=10)

boton1 = Button(text="Eliminar", font=("Arial", 14))
boton1.grid(column=1, row=10)
 
 
Menuin_principal.mainloop()