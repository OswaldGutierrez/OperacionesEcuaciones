import tkinter as tk

def aplicar_estilos(root):
    """Aplica los estilos básicos a la ventana principal y retorna los widgets necesarios"""
    root.title("Extrapolación de Richardson")
    
    # Hacer que la ventana sea responsiva
    root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
    root.columnconfigure([0, 1], weight=1)

    # Etiquetas
    etiqueta_funcion = tk.Label(root, text="Ingresa la función f(x):")
    etiqueta_funcion.grid(row=0, column=0, padx=10, pady=10)

    etiqueta_x = tk.Label(root, text="Ingresa el valor de x:")
    etiqueta_x.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_p = tk.Label(root, text="Ingresa el valor de p:")
    etiqueta_p.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_r = tk.Label(root, text="Ingresa el valor de r:")
    etiqueta_r.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_h = tk.Label(root, text="Ingresa el valor de h:")
    etiqueta_h.grid(row=4, column=0, padx=10, pady=10)

    etiqueta_q = tk.Label(root, text="Ingresa el valor de q:")
    etiqueta_q.grid(row=5, column=0, padx=10, pady=10)

    # Entradas
    entrada_funcion = tk.Entry(root)
    entrada_funcion.grid(row=0, column=1, padx=10, pady=10)

    entrada_x = tk.Entry(root)
    entrada_x.grid(row=1, column=1, padx=10, pady=10)

    entrada_p = tk.Entry(root)
    entrada_p.grid(row=2, column=1, padx=10, pady=10)

    entrada_r = tk.Entry(root)
    entrada_r.grid(row=3, column=1, padx=10, pady=10)

    entrada_h = tk.Entry(root)
    entrada_h.grid(row=4, column=1, padx=10, pady=10)

    entrada_q = tk.Entry(root)
    entrada_q.grid(row=5, column=1, padx=10, pady=10)

    botonRichardson = tk.Button(root, text="Mejorar la precisión")
    botonRichardson.grid(row=6, column=1, padx=10, pady=10)

    return (entrada_funcion, entrada_x, entrada_p, entrada_r, entrada_h, entrada_q, botonRichardson)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    entradas = aplicar_estilos(root)
    root.mainloop()
