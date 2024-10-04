import sys
import os
import tkinter as tk

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleDiferencias  # Importa tu archivo de estilos

class Diferencias:
    def __init__(self):
        self.root = tk.Tk()  # Crea la ventana principal
        self.entradaNumElementos, self.botonContinuar, self.etiquetaError = styleDiferencias.aplicarEstilosDiferencias(self.root)  # Aplica el estilo
        self.botonCalcular = tk.Button(self.root, text="Calcular", state="disabled")  # Crea el botón "Calcular"
        self.botonCalcular.config(command=self.calcular)  # Asigna la función calcular al botón
        self.botonContinuar.config(command=self.crear_campos)
        self.camposFunciones = []  # Inicializa la lista de campos de función

    def crear_campos(self):
        """Crea los campos de entrada cuando se presiona 'Continuar'"""
        try:
            numElementos = int(self.entradaNumElementos.get())
            self.camposFunciones = styleDiferencias.mostrarCamposDeEntrada(self.root, numElementos, self.botonCalcular)
        except ValueError:
            self.etiquetaError.config(text="Por favor ingrese un número válido.", fg="red")

    def calcular(self):
        """Calcula y muestra la tabla de diferencias divididas"""
        # Recoge los valores de las funciones ingresadas
        f_x = [float(entrada.get()) for entrada in self.camposFunciones]

        # Obtiene los x_i como valores de entrada
        x = [1.0 + i * 0.3 for i in range(len(f_x))]

        # Crea la tabla para mostrar los resultados
        self.mostrarTabla(x, f_x)

    def mostrarTabla(self, x, f_x):
        """Muestra la tabla de diferencias divididas"""
        # Crear una nueva ventana para mostrar la tabla
        tablaVentana = tk.Toplevel(self.root)
        tablaVentana.title("Tabla de Diferencias Divididas")

        # Encabezados de la tabla
        tk.Label(tablaVentana, text="i").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tablaVentana, text="xi").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(tablaVentana, text="F(xi)").grid(row=0, column=2, padx=10, pady=5)

        # Inicializa una lista para almacenar los resultados de las diferencias divididas
        diferencias = [[None] * (len(f_x) + 1) for _ in range(len(f_x))]

        # Llenar la tabla con valores
        for i in range(len(f_x)):
            tk.Label(tablaVentana, text=i).grid(row=i + 1, column=0, padx=10, pady=5)
            tk.Label(tablaVentana, text=x[i]).grid(row=i + 1, column=1, padx=10, pady=5)
            tk.Label(tablaVentana, text=f_x[i]).grid(row=i + 1, column=2, padx=10, pady=5)
            diferencias[i][0] = f_x[i]  # F(xi) son los valores que ingresa el usuario

        # Calcular las diferencias divididas
        for j in range(1, len(f_x)):
            for i in range(len(f_x) - j):
                # F[xi, xi+1] = (F[xi+1] - F[xi]) / (xi+1 - xi)
                diferencias[i][j] = (diferencias[i + 1][j - 1] - diferencias[i][j - 1]) / (x[i + j] - x[i])

        # Llenar la tabla con las diferencias calculadas
        for i in range(len(f_x)):
            for j in range(1, len(f_x) - i):
                if diferencias[i][j] is not None:
                    tk.Label(tablaVentana, text=f"{diferencias[i][j]:.4f}").grid(row=i + 1, column=j + 2, padx=10, pady=5)
                else:
                    # Coloca "sin valor" en las filas superiores
                    tk.Label(tablaVentana, text="sin valor").grid(row=i, column=j + 2, padx=10, pady=5)

    def iniciar(self):
        self.root.mainloop()  # Inicia el loop de la ventana

# Ejecuta la aplicación
if __name__ == "__main__":
    app = Diferencias()
    app.iniciar()