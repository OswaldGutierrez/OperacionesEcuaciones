import sys
import os
import tkinter as tk
from sympy import symbols, diff, lambdify, N
from secante import mostrar_resultado_secante

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleNewton  # Importa tu archivo de estilos

class Newton:
    def __init__(self):
        self.root = tk.Tk()
        self.entrada_funcion, self.entrada_p0, self.entrada_tolerancia, self.entrada_iteraciones, self.botonCalcular, self.botonSecante = styleNewton.aplicar_estilos(self.root)
        
        # Configurar los botones
        self.botonCalcular.config(command=self.calcular_nueva_raiz)
        self.botonSecante.config(command=self.calcular_secante)  # Configura el botón para la secante

    def calcular_nueva_raiz(self):
        # Obtener valores de entrada
        funcion = self.entrada_funcion.get()
        p0 = float(self.entrada_p0.get())
        tolerancia = float(self.entrada_tolerancia.get())
        max_iteraciones = int(self.entrada_iteraciones.get())

        # Definición de la variable simbólica
        x = symbols('x')
        
        # Calcula la función y su derivada
        f = lambdify(x, funcion, "numpy")
        f_prime = lambdify(x, diff(funcion, x), "numpy")
        
        p = p0
        for i in range(1, max_iteraciones + 1):
            p = p0 - (f(p0) / f_prime(p0))
            if abs(p - p0) < tolerancia:
                self.mostrar_resultado(f"Resultado: {N(p)}")
                return
            p0 = p
        
        self.mostrar_resultado("No se pudo resolver en el número de iteraciones especificado.")

    def calcular_secante(self):
        funcion = self.entrada_funcion.get()
        p0 = float(self.entrada_p0.get())
        p1 = float(self.entrada_iteraciones.get())  # Usamos el segundo punto como iteraciones para el método secante
        tolerancia = float(self.entrada_tolerancia.get())
        max_iteraciones = int(self.entrada_iteraciones.get())

        resultado = mostrar_resultado_secante(funcion, p0, p1, tolerancia, max_iteraciones)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, mensaje):
        resultado_window = tk.Toplevel(self.root)
        resultado_window.title("Resultado")
        label_resultado = tk.Label(resultado_window, text=mensaje)
        label_resultado.pack(padx=20, pady=20)

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Newton()
    app.iniciar()
