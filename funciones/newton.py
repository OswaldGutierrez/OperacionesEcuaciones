import sys
import os
import tkinter as tk
from sympy import symbols, diff, lambdify, N

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleNewton  # Importa tu archivo de estilos

class Newton:
    def __init__(self):
        self.root = tk.Tk()  # Crea la ventana principal
        self.entrada_funcion, self.entrada_p0, self.entrada_tolerancia, self.entrada_iteraciones, self.botonCalcular = styleNewton.aplicar_estilos(self.root)  # Aplica el estilo de styleDerivadas
        self.botonCalcular.config(command=self.calcular_nueva_raiz)  # Configura el botón para llamar a calcular_nueva_raiz

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
            # Paso 3
            p = p0 - (f(p0) / f_prime(p0))
            
            # Paso 4
            if abs(p - p0) < tolerancia:
                self.mostrar_resultado(f"Resultado: {N(p)}")  # Salida(p)
                return
            
            # Paso 5
            p0 = p
        
        # Paso 7
        self.mostrar_resultado("No se pudo resolver en el número de iteraciones especificado.")

    def mostrar_resultado(self, mensaje):
        # Crear una nueva ventana para mostrar el resultado
        resultado_window = tk.Toplevel(self.root)
        resultado_window.title("Resultado")
        label_resultado = tk.Label(resultado_window, text=mensaje)
        label_resultado.pack(padx=20, pady=20)

    def iniciar(self):
        self.root.mainloop()  # Inicia el loop de la ventana

# Ejecuta la aplicación
if __name__ == "__main__":
    app = Newton()
    app.iniciar()
