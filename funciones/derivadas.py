import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox
import math

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleDerivadas  # Importa tu archivo de estilos


class Derivadas:
    def __init__(self):
        self.root = tk.Tk()  # Crea la ventana principal
        (self.entradaFuncion, self.entradax0, 
         self.botonCalcular2, self.botonCalcular3, self.botonCalcular5) = styleDerivadas.aplicarEstiloDerivadas(self.root)  # Aplica el estilo

        # Conectar los botones a las funciones que calculan y muestran la tabla
        self.botonCalcular2.config(command=self.mostrarTabla2Puntos)
        self.botonCalcular3.config(command=self.mostrarTabla3Puntos)
        self.botonCalcular5.config(command=self.mostrarTabla5Puntos)

        # Variable para almacenar la tabla actual
        self.tablaActual = None

    def procesarFuncion(self, funcion):
        """Reemplaza nombres comunes en la función ingresada con funciones válidas de Python."""
        # Cambia 'lnx' a 'math.log(x)' y 'cosx' a 'math.cos(x)'
        funcion = funcion.replace("lnx", "math.log(x)")
        funcion = funcion.replace("cosx", "math.cos(x)")
        funcion = funcion.replace("sinx", "math.sin(x)")
        funcion = funcion.replace("tanx", "math.tan(x)")
        funcion = funcion.replace("exp", "math.exp")
        funcion = funcion.replace("sqrt", "math.sqrt")
        return funcion

    def f(self, funcion, x):
        """Evalúa la función ingresada por el usuario."""
        funcionProcesada = self.procesarFuncion(funcion)
        return eval(funcionProcesada)

    def segundaDerivada(self, funcion, x0, h):
        return (self.f(funcion, x0 + h) - 2 * self.f(funcion, x0) + self.f(funcion, x0 - h)) / (h ** 2)

    def terceraDerivada(self, funcion, x0, h):
        return (self.f(funcion, x0 + 2*h) - 2 * self.f(funcion, x0 + h) + 2 * self.f(funcion, x0 - h) - self.f(funcion, x0 - 2*h)) / (2 * h ** 3)

    def quintaDerivada(self, funcion, x0, h):
        return (self.f(funcion, x0 - 2*h) - 8*self.f(funcion, x0 - h) + 8*self.f(funcion, x0 + h) - self.f(funcion, x0 + 2*h)) / (12 * h)

    def limpiarTabla(self):
        """Elimina cualquier tabla anterior de la interfaz."""
        if self.tablaActual is not None:
            self.tablaActual.destroy()  # Destruye la tabla anterior si existe
            self.tablaActual = None

    def mostrarTabla2Puntos(self):
        """Calcula y muestra la tabla para el método de 2 puntos."""
        self.limpiarTabla()  # Limpiar la tabla anterior

        try:
            funcion = self.entradaFuncion.get()  # Obtener la función como string
            x0 = float(self.entradax0.get())  # Obtener el valor de x0
            h_values = [0.1, 0.01, 0.001]  # Valores de h

            # Crear la tabla para mostrar los resultados
            self.tablaActual = ttk.Treeview(self.root, columns=("h", "f(x0+h)", "[f(x0+h) - f(x0)] / h", "h * f''(x0) / 2"), show='headings')
            self.tablaActual.grid(row=21, column=0, columnspan=3, padx=10, pady=10)

            # Definir los encabezados de la tabla
            self.tablaActual.heading("h", text="h")
            self.tablaActual.heading("f(x0+h)", text="f(x0+h)")
            self.tablaActual.heading("[f(x0+h) - f(x0)] / h", text="[f(x0+h) - f(x0)] / h")
            self.tablaActual.heading("h * f''(x0) / 2", text="h * f''(x0) / 2")

            # Calcular los valores para cada h
            for h in h_values:
                fx0h = self.f(funcion, x0 + h)
                derivada = (fx0h - self.f(funcion, x0)) / h
                terminoAdicional = (h * self.segundaDerivada(funcion, x0, h)) / 2

                # Insertar los valores en la tabla
                self.tablaActual.insert("", "end", values=(h, round(fx0h, 5), round(derivada, 5), round(terminoAdicional, 5)))

        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la tabla: {str(e)}")

    def mostrarTabla3Puntos(self):
        """Calcula y muestra la tabla para el método de 3 puntos."""
        self.limpiarTabla()  # Limpiar la tabla anterior
        self.mostrarTabla(lambda f, x0, h: (self.f(f, x0 + h) - self.f(f, x0 - h)) / (2 * h), "3 puntos")

    def mostrarTabla5Puntos(self):
        """Calcula y muestra la tabla para el método de 5 puntos."""
        self.limpiarTabla()  # Limpiar la tabla anterior
        self.mostrarTabla(lambda f, x0, h: (self.f(f, x0 - 2*h) - 8*self.f(f, x0 - h) + 8*self.f(f, x0 + h) - self.f(f, x0 + 2*h)) / (12 * h), "5 puntos")

    def mostrarTabla(self, formula, metodo):
        """Calcula los valores para h y muestra la tabla con los resultados."""
        try:
            funcion = self.entradaFuncion.get()  # Obtener la función como string
            x0 = float(self.entradax0.get())  # Obtener el valor de x0
            h_values = [0.1, 0.01, 0.001]  # Valores de h

            # Crear la tabla para mostrar los resultados
            self.tablaActual = ttk.Treeview(self.root, columns=("h", "f'(x0)", "Término adicional"), show='headings')
            self.tablaActual.grid(row=21, column=0, columnspan=3, padx=10, pady=10)

            # Definir los encabezados de la tabla
            self.tablaActual.heading("h", text="h")
            self.tablaActual.heading("f'(x0)", text=f"f'(x0) - Método {metodo}")
            self.tablaActual.heading("Término adicional", text="Término adicional")

            # Calcular los valores para cada h
            for h in h_values:
                derivada = formula(funcion, x0, h)
                terminoAdicional = (h**2 / 6) * self.segundaDerivada(funcion, x0, h) if metodo == "3 puntos" else (h**4 / 30) * self.quintaDerivada(funcion, x0, h)

                # Insertar los valores en la tabla
                self.tablaActual.insert("", "end", values=(h, round(derivada, 5), round(terminoAdicional, 5)))

        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la tabla: {str(e)}")

    def iniciar(self):
        self.root.mainloop()  # Inicia el loop de la ventana

# Ejecuta la aplicación
if __name__ == "__main__":
    app = Derivadas()
    app.iniciar()