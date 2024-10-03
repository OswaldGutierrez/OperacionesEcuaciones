import sys
import os
import tkinter as tk
from tkinter import messagebox  # Importar messagebox para mostrar resultados
import sympy as sp  # Importar sympy para calcular derivadas

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleRichardson  # Importa tu archivo de estilos

class Richardson:
    def __init__(self):
        self.root = tk.Tk()  # Crea la ventana principal
        styleRichardson.aplicar_estilos(self.root)  # Aplica el estilo de styleRichardson

        # Configura la interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la interfaz gráfica para la extrapolación de Richardson"""
        # Etiquetas
        tk.Label(self.root, text="Ingresa la función f(x):").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Ingresa el valor de x:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Ingresa el valor de p:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Ingresa el valor de r:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Ingresa el valor de h:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Ingresa el valor de q:").grid(row=5, column=0, padx=10, pady=10)

        # Entradas
        self.entrada_funcion = tk.Entry(self.root)
        self.entrada_funcion.grid(row=0, column=1, padx=10, pady=10)

        self.entrada_x = tk.Entry(self.root)
        self.entrada_x.grid(row=1, column=1, padx=10, pady=10)

        self.entrada_p = tk.Entry(self.root)
        self.entrada_p.grid(row=2, column=1, padx=10, pady=10)

        self.entrada_r = tk.Entry(self.root)
        self.entrada_r.grid(row=3, column=1, padx=10, pady=10)

        self.entrada_h = tk.Entry(self.root)
        self.entrada_h.grid(row=4, column=1, padx=10, pady=10)

        self.entrada_q = tk.Entry(self.root)
        self.entrada_q.grid(row=5, column=1, padx=10, pady=10)

        # Botón para mejorar la precisión
        botonRichardson = tk.Button(self.root, text="Mejorar la precisión", command=self.calcular_richardson)
        botonRichardson.grid(row=6, column=1, padx=10, pady=10)

    def calcular_richardson(self):
        """Calcula a0 usando la extrapolación de Richardson y muestra el resultado"""
        try:
            # Obtener los valores de entrada
            funcion_str = self.entrada_funcion.get()
            x = float(self.entrada_x.get())
            h = float(self.entrada_h.get())
            q = float(self.entrada_q.get())
            p = float(self.entrada_p.get())
            
            # Calcular f(x + h) y f(x)
            x_sym = sp.symbols('x')
            funcion = sp.sympify(funcion_str)  # Convierte la cadena a una expresión simbólica

            # Calcular F(h) y F(h/q)
            F_h = (funcion.subs(x_sym, x + h) - funcion.subs(x_sym, x)) / h
            F_h_q = (funcion.subs(x_sym, x + h/q) - funcion.subs(x_sym, x)) / (h/q)

            # Calcular a0 usando la nueva fórmula
            a0_resultado = F_h + ((F_h - F_h_q) / (q ** -p - 1))

            # Calcular la derivada de f(x)
            derivada = sp.diff(funcion, x_sym)  # Calcula la derivada
            derivada_valor = derivada.subs(x_sym, x)  # Evaluar la derivada en x

            # Mostrar el resultado en un mensaje
            messagebox.showinfo("Resultado", 
                f"f'({x}) = {derivada_valor:.4f}\n"
                f"F(h) = {F_h:.4f}\n"
                f"F(h/q) = {F_h_q:.4f}\n"
                f"El valor de a0 es: {a0_resultado:.4f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def iniciar(self):
        self.root.mainloop()  # Inicia el loop de la ventana

# Ejecuta la aplicación
if __name__ == "__main__":
    app = Richardson()
    app.iniciar()
