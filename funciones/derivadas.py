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
        (self.entrada_funcion, self.entrada_x0, 
         self.botonCalcular2, self.botonCalcular3, self.botonCalcular5) = styleDerivadas.aplicar_estilos(self.root)  # Aplica el estilo

        # Conectar los botones a las funciones que calculan y muestran la tabla
        self.botonCalcular2.config(command=self.mostrar_tabla_2_puntos)
        self.botonCalcular3.config(command=self.mostrar_tabla_3_puntos)
        self.botonCalcular5.config(command=self.mostrar_tabla_5_puntos)

        # Variable para almacenar la tabla actual
        self.tabla_actual = None

    def procesar_funcion(self, funcion):
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
        funcion_procesada = self.procesar_funcion(funcion)
        return eval(funcion_procesada)

    def segunda_derivada(self, funcion, x0, h):
        return (self.f(funcion, x0 + h) - 2 * self.f(funcion, x0) + self.f(funcion, x0 - h)) / (h ** 2)

    def tercera_derivada(self, funcion, x0, h):
        return (self.f(funcion, x0 + 2*h) - 2 * self.f(funcion, x0 + h) + 2 * self.f(funcion, x0 - h) - self.f(funcion, x0 - 2*h)) / (2 * h ** 3)

    def quinta_derivada(self, funcion, x0, h):
        return (self.f(funcion, x0 - 2*h) - 8*self.f(funcion, x0 - h) + 8*self.f(funcion, x0 + h) - self.f(funcion, x0 + 2*h)) / (12 * h)

    def limpiar_tabla(self):
        """Elimina cualquier tabla anterior de la interfaz."""
        if self.tabla_actual is not None:
            self.tabla_actual.destroy()  # Destruye la tabla anterior si existe
            self.tabla_actual = None

    def mostrar_tabla_2_puntos(self):
        """Calcula y muestra la tabla para el método de 2 puntos."""
        self.limpiar_tabla()  # Limpiar la tabla anterior

        try:
            funcion = self.entrada_funcion.get()  # Obtener la función como string
            x0 = float(self.entrada_x0.get())  # Obtener el valor de x0
            h_values = [0.1, 0.01, 0.001]  # Valores de h

            # Crear la tabla para mostrar los resultados
            self.tabla_actual = ttk.Treeview(self.root, columns=("h", "f(x0+h)", "[f(x0+h) - f(x0)] / h", "h * f''(x0) / 2"), show='headings')
            self.tabla_actual.grid(row=21, column=0, columnspan=3, padx=10, pady=10)

            # Definir los encabezados de la tabla
            self.tabla_actual.heading("h", text="h")
            self.tabla_actual.heading("f(x0+h)", text="f(x0+h)")
            self.tabla_actual.heading("[f(x0+h) - f(x0)] / h", text="[f(x0+h) - f(x0)] / h")
            self.tabla_actual.heading("h * f''(x0) / 2", text="h * f''(x0) / 2")

            # Calcular los valores para cada h
            for h in h_values:
                fx0h = self.f(funcion, x0 + h)
                derivada = (fx0h - self.f(funcion, x0)) / h
                termino_adicional = (h * self.segunda_derivada(funcion, x0, h)) / 2

                # Insertar los valores en la tabla
                self.tabla_actual.insert("", "end", values=(h, round(fx0h, 5), round(derivada, 5), round(termino_adicional, 5)))

        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la tabla: {str(e)}")

    def mostrar_tabla_3_puntos(self):
        """Calcula y muestra la tabla para el método de 3 puntos."""
        self.limpiar_tabla()  # Limpiar la tabla anterior
        self.mostrar_tabla(lambda f, x0, h: (self.f(f, x0 + h) - self.f(f, x0 - h)) / (2 * h), "3 puntos")

    def mostrar_tabla_5_puntos(self):
        """Calcula y muestra la tabla para el método de 5 puntos."""
        self.limpiar_tabla()  # Limpiar la tabla anterior
        self.mostrar_tabla(lambda f, x0, h: (self.f(f, x0 - 2*h) - 8*self.f(f, x0 - h) + 8*self.f(f, x0 + h) - self.f(f, x0 + 2*h)) / (12 * h), "5 puntos")

    def mostrar_tabla(self, formula, metodo):
        """Calcula los valores para h y muestra la tabla con los resultados."""
        try:
            funcion = self.entrada_funcion.get()  # Obtener la función como string
            x0 = float(self.entrada_x0.get())  # Obtener el valor de x0
            h_values = [0.1, 0.01, 0.001]  # Valores de h

            # Crear la tabla para mostrar los resultados
            self.tabla_actual = ttk.Treeview(self.root, columns=("h", "f'(x0)", "Término adicional"), show='headings')
            self.tabla_actual.grid(row=21, column=0, columnspan=3, padx=10, pady=10)

            # Definir los encabezados de la tabla
            self.tabla_actual.heading("h", text="h")
            self.tabla_actual.heading("f'(x0)", text=f"f'(x0) - Método {metodo}")
            self.tabla_actual.heading("Término adicional", text="Término adicional")

            # Calcular los valores para cada h
            for h in h_values:
                derivada = formula(funcion, x0, h)
                termino_adicional = (h**2 / 6) * self.segunda_derivada(funcion, x0, h) if metodo == "3 puntos" else (h**4 / 30) * self.quinta_derivada(funcion, x0, h)

                # Insertar los valores en la tabla
                self.tabla_actual.insert("", "end", values=(h, round(derivada, 5), round(termino_adicional, 5)))

        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la tabla: {str(e)}")

    def iniciar(self):
        self.root.mainloop()  # Inicia el loop de la ventana

# Ejecuta la aplicación
if __name__ == "__main__":
    app = Derivadas()
    app.iniciar()