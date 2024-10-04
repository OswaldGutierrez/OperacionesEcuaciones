import tkinter as tk

def aplicarEstilosRichardson(root):
    """Aplica los estilos básicos a la ventana principal y retorna los widgets necesarios"""
    root.title("Extrapolación de Richardson")
    
    # Hacer que la ventana sea responsiva
    root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
    root.columnconfigure([0, 1], weight=1)

    # Etiquetas
    etiquetaFuncion = tk.Label(root, text="Ingresa la función f(x):")
    etiquetaFuncion.grid(row=0, column=0, padx=10, pady=10)

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
    entradaFuncion = tk.Entry(root)
    entradaFuncion.grid(row=0, column=1, padx=10, pady=10)

    entradaX = tk.Entry(root)
    entradaX.grid(row=1, column=1, padx=10, pady=10)

    entradaP = tk.Entry(root)
    entradaP.grid(row=2, column=1, padx=10, pady=10)

    entradaR = tk.Entry(root)
    entradaR.grid(row=3, column=1, padx=10, pady=10)

    entradaH = tk.Entry(root)
    entradaH.grid(row=4, column=1, padx=10, pady=10)

    entradaQ = tk.Entry(root)
    entradaQ.grid(row=5, column=1, padx=10, pady=10)

    botonRichardson = tk.Button(root, text="Mejorar la precisión")
    botonRichardson.grid(row=6, column=1, padx=10, pady=10)

    return (entradaFuncion, entradaX, entradaP, entradaR, entradaH, entradaQ, botonRichardson)

