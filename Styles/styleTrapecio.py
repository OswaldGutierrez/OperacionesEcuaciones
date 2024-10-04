import tkinter as tk

def aplicarEstiloTrapecio(root):
    root.title("Método Trapecio")

    # Hacer que la ventana sea responsiva
    root.rowconfigure([0, 1, 2, 3], weight=1)
    root.columnconfigure([0, 1], weight=1)

    # Etiquetas
    etiquetaA = tk.Label(root, text="Límite inferior (a):")
    etiquetaA.grid(row=0, column=0, padx=10, pady=10)

    etiquetaB = tk.Label(root, text="Límite superior (b):")
    etiquetaB.grid(row=1, column=0, padx=10, pady=10)

    etiquetaFuncion = tk.Label(root, text="Función f(x):")
    etiquetaFuncion.grid(row=2, column=0, padx=10, pady=10)

    # Entradas
    entradaA = tk.Entry(root)
    entradaA.grid(row=0, column=1, padx=10, pady=10)

    entradaB = tk.Entry(root)
    entradaB.grid(row=1, column=1, padx=10, pady=10)

    entradaFuncion = tk.Entry(root)
    entradaFuncion.grid(row=2, column=1, padx=10, pady=10)

    botonCalcular = tk.Button(root, text="Calcular Integral")
    botonCalcular.grid(row=3, columnspan=2, padx=10, pady=10)

    return (entradaA, entradaB, entradaFuncion, botonCalcular)
