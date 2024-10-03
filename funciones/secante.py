import tkinter as tk
from sympy import symbols, lambdify, N

class Secante:
    def __init__(self, funcion, x0, x1, tolerancia, max_iteraciones):
        self.funcion = funcion
        self.x0 = x0
        self.x1 = x1
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones

        # Definición de la variable simbólica
        x = symbols('x')
        self.f = lambdify(x, funcion, "numpy")

    def calcular(self):
        for i in range(self.max_iteraciones):
            f_x0 = self.f(self.x0)
            f_x1 = self.f(self.x1)

            # Fórmula del método secante
            x2 = (self.x1 * f_x0 - self.x0 * f_x1) / (f_x0 - f_x1)

            # Verificar la convergencia
            if abs(x2 - self.x1) < self.tolerancia:
                return N(x2)  # Salida

            # Actualizar valores para la siguiente iteración
            self.x0, self.x1 = self.x1, x2
        
        return None  # No se encontró la raíz en el número de iteraciones especificado

def mostrar_resultado_secante(funcion, p0, p1, tolerancia, max_iteraciones):
    secante = Secante(funcion, p0, p1, tolerancia, max_iteraciones)
    resultado = secante.calcular()
    
    if resultado is not None:
        return f"Resultado: {resultado}"
    else:
        return "No se pudo resolver en el número de iteraciones especificado."

# Ejemplo de uso (puedes comentar esta sección si no la necesitas)
if __name__ == "__main__":
    funcion = "x**2 - 4"  # Ejemplo de función
    p0 = 2.0  # Valor inicial
    p1 = 3.0  # Valor inicial
    tolerancia = 0.01  # Tolerancia
    max_iteraciones = 100  # Iteraciones máximas

    print(mostrar_resultado_secante(funcion, p0, p1, tolerancia, max_iteraciones))
