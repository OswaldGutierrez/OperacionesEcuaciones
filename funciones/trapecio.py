import sys
import os
import tkinter as tk
from sympy import symbols, lambdify, diff, N

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleTrapecio  # Importa tu archivo de estilos

class Trapecio:
    def __init__(self):
        self.root = tk.Tk()
        self.entradaA, self.entrabaB, self.entradaFuncion, self.botonCalcular = styleTrapecio.aplicarEstiloTrapecio(self.root)

        # Configurar el botón
        self.botonCalcular.config(command=self.calcularIntegral)

    def calcularIntegral(self):
        try:
            a = float(self.entradaA.get())
            b = float(self.entrabaB.get())
            funcionStr = self.entradaFuncion.get()

            # Definir la variable simbólica
            x = symbols('x')

            # Convertir la función ingresada en una función lambda
            f = lambdify(x, funcionStr, "numpy")

            # Calcular el valor de la integral usando la regla del trapecio simple
            integral = self.reglaTrapecio(f, a, b)

            # Calcular el error
            error, epsilon = self.calcularError(funcionStr, a, b)  # Cambiar aquí para pasar la función como string

            self.mostrarResultado(f"Resultado de la integral: {integral:.4f}\nError: {error:.4f}\nValor de ε: {epsilon:.4f}")
        except Exception as e:
            self.mostrarResultado(f"Error: {str(e)}")

    def reglaTrapecio(self, f, a, b):
        """Calcula la integral definida usando la regla del trapecio."""
        return (f(a) + f(b)) * (b - a) / 2  # Fórmula del trapecio simple

    def calcularError(self, funcion_str, a, b):
        """Calcula el error usando la fórmula proporcionada."""
        # Calcular la segunda derivada de la función
        x = symbols('x')
        f_prime2 = diff(diff(funcion_str, x), x)  # Segunda derivada
        f_double_prime = lambdify(x, f_prime2, "numpy")

        # Elegir un valor de ε en el intervalo [a, b] (puedes usar el promedio)
        epsilon = (a + b) / 2
        error = ((b - a) ** 3 * abs(f_double_prime(epsilon))) / 12  # Fórmula del error

        return error, epsilon

    def mostrarResultado(self, mensaje):
        resultadoGui = tk.Toplevel(self.root)
        resultadoGui.title("Resultado")
        labelResultado = tk.Label(resultadoGui, text=mensaje)
        labelResultado.pack(padx=20, pady=20)

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Trapecio()
    app.iniciar()
