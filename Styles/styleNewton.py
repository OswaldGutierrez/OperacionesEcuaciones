import tkinter as tk

def aplicar_estilos(root):
    """Aplica los estilos básicos a la ventana principal y retorna los widgets necesarios"""
    root.title("Método Newton")
    
    # Hacer que la ventana sea responsiva
    root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)  # Agregar una fila más
    root.columnconfigure([0, 1], weight=1)

    # Etiquetas
    etiqueta_funcion = tk.Label(root, text="Por favor ingresa tu función f(x)=")
    etiqueta_funcion.grid(row=0, column=0, padx=10, pady=10)

    etiqueta_p0 = tk.Label(root, text="Ingresa el valor de p0:")
    etiqueta_p0.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_tolerancia = tk.Label(root, text="Ingresa el valor de tolerancia:")
    etiqueta_tolerancia.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_iteraciones = tk.Label(root, text="Ingresa el valor de iteraciones máximas:")
    etiqueta_iteraciones.grid(row=3, column=0, padx=10, pady=10)

    # Entradas
    entrada_funcion = tk.Entry(root)
    entrada_funcion.grid(row=0, column=1, padx=10, pady=10)

    entrada_p0 = tk.Entry(root)
    entrada_p0.grid(row=1, column=1, padx=10, pady=10)

    entrada_tolerancia = tk.Entry(root)
    entrada_tolerancia.grid(row=2, column=1, padx=10, pady=10)

    entrada_iteraciones = tk.Entry(root)
    entrada_iteraciones.grid(row=3, column=1, padx=10, pady=10)

    botonCalcularNewton = tk.Button(root, text="Calcular Newton")
    botonCalcularNewton.grid(row=4, column=1, padx=10, pady=10)

    botonCalcularSecante = tk.Button(root, text="Calcular Secante")
    botonCalcularSecante.grid(row=5, column=1, padx=10, pady=10)  # Agregar botón de secante

    return (entrada_funcion, entrada_p0, entrada_tolerancia, 
            entrada_iteraciones, botonCalcularNewton, botonCalcularSecante)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    aplicar_estilos(root)
    root.mainloop()
