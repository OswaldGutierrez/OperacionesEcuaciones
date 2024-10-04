import sys
import os
import tkinter as tk
from sympy import symbols, diff, lambdify, N
from secante import mostrarResultadoSecante

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleNewton  # Importa tu archivo de estilos

class Newton:
    def __init__(self):
        self.root = tk.Tk()
        self.entradaFuncion, self.entrada_p0, self.entradaTolerancia, self.entradaIteraciones, self.botonCalcular, self.botonSecante = styleNewton.aplicarEstilosNewton(self.root)
        
        # Configurar los botones
        self.botonCalcular.config(command=self.calcularNuevaRaiz)
        self.botonSecante.config(command=self.calcularSecante)  # Configura el botón para la secante

    def calcularNuevaRaiz(self):
        # Obtener valores de entrada
        funcion = self.entradaFuncion.get()
        p0 = float(self.entrada_p0.get())
        tolerancia = float(self.entradaTolerancia.get())
        max_iteraciones = int(self.entradaIteraciones.get())

        # Definición de la variable simbólica
        x = symbols('x')
        
        # Calcula la función y su derivada
        f = lambdify(x, funcion, "numpy")
        f_prime = lambdify(x, diff(funcion, x), "numpy")
        
        p = p0
        for i in range(1, max_iteraciones + 1):
            p = p0 - (f(p0) / f_prime(p0))
            if abs(p - p0) < tolerancia:
                self.mostrarResultado(f"Resultado: {N(p)}")
                return
            p0 = p
        
        self.mostrarResultado("No se pudo resolver en el número de iteraciones especificado.")

    def calcularSecante(self):
        funcion = self.entradaFuncion.get()
        p0 = float(self.entrada_p0.get())
        p1 = float(self.entradaIteraciones.get())  # Usamos el segundo punto como iteraciones para el método secante
        tolerancia = float(self.entradaTolerancia.get())
        max_iteraciones = int(self.entradaIteraciones.get())

        resultado = mostrarResultadoSecante(funcion, p0, p1, tolerancia, max_iteraciones)
        self.mostrarResultado(resultado)

    def mostrarResultado(self, mensaje):
        resultadoGui = tk.Toplevel(self.root)
        resultadoGui.title("Resultado")
        labelResultado = tk.Label(resultadoGui, text=mensaje)
        labelResultado.pack(padx=20, pady=20)

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Newton()
    app.iniciar()
