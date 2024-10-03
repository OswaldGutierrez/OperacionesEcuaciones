import sys
import os
import tkinter as tk

# Añade el directorio raíz ('Ecuaciones') a las rutas de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleDiferencias  # Importa tu archivo de estilos

class Diferencias:
    def __init__(self):
        self.root = tk.Tk()  # Crea la ventana principal
        self.entrada_num_elementos, self.boton_continuar, self.etiqueta_error = styleDiferencias.aplicar_estilos(self.root)  # Aplica el estilo
        self.boton_calcular = tk.Button(self.root, text="Calcular", state="disabled")  # Crea el botón "Calcular"
        self.boton_calcular.config(command=self.calcular)  # Asigna la función calcular al botón
        self.boton_continuar.config(command=self.crear_campos)
        self.campos_funciones = []  # Inicializa la lista de campos de función

    def crear_campos(self):
        """Crea los campos de entrada cuando se presiona 'Continuar'"""
        try:
            num_elementos = int(self.entrada_num_elementos.get())
            self.campos_funciones = styleDiferencias.mostrar_campos_de_entrada(self.root, num_elementos, self.boton_calcular)
        except ValueError:
            self.etiqueta_error.config(text="Por favor ingrese un número válido.", fg="red")

    def calcular(self):
        """Calcula y muestra la tabla de diferencias divididas"""
        # Recoge los valores de las funciones ingresadas
        f_x = [float(entrada.get()) for entrada in self.campos_funciones]

        # Obtiene los x_i como valores de entrada
        x = [1.0 + i * 0.3 for i in range(len(f_x))]

        # Crea la tabla para mostrar los resultados
        self.mostrar_tabla(x, f_x)

    def mostrar_tabla(self, x, f_x):
        """Muestra la tabla de diferencias divididas"""
        # Crear una nueva ventana para mostrar la tabla
        tabla_ventana = tk.Toplevel(self.root)
        tabla_ventana.title("Tabla de Diferencias Divididas")

        # Encabezados de la tabla
        tk.Label(tabla_ventana, text="i").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tabla_ventana, text="xi").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(tabla_ventana, text="F(xi)").grid(row=0, column=2, padx=10, pady=5)

        # Inicializa una lista para almacenar los resultados de las diferencias divididas
        diferencias = [[None] * (len(f_x) + 1) for _ in range(len(f_x))]

        # Llenar la tabla con valores
        for i in range(len(f_x)):
            tk.Label(tabla_ventana, text=i).grid(row=i + 1, column=0, padx=10, pady=5)
            tk.Label(tabla_ventana, text=x[i]).grid(row=i + 1, column=1, padx=10, pady=5)
            tk.Label(tabla_ventana, text=f_x[i]).grid(row=i + 1, column=2, padx=10, pady=5)
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
                    tk.Label(tabla_ventana, text=f"{diferencias[i][j]:.4f}").grid(row=i + 1, column=j + 2, padx=10, pady=5)
                else:
                    # Coloca "sin valor" en las filas superiores
                    tk.Label(tabla_ventana, text="sin valor").grid(row=i, column=j + 2, padx=10, pady=5)

    def iniciar(self):
        self.root.mainloop()  # Inicia el loop de la ventana

# Ejecuta la aplicación
if __name__ == "__main__":
    app = Diferencias()
    app.iniciar()