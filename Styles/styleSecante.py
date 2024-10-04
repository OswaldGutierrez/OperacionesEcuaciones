import tkinter as tk

def aplicarEstiloSecante(root):
    """Aplica los estilos básicos a la ventana principal y retorna los widgets necesarios"""
    root.title("Método Newton")
    
    # Hacer que la ventana sea responsiva
    root.rowconfigure(0, weight=1)
    root.columnconfigure([0, 1, 2], weight=1)
    root.rowconfigure(1, weight=1)

    # Etiquetas
    etiquetaFuncion = tk.Label(root, text="Por favor ingresa tu función f(x)=")
    etiquetaFuncion.grid(row=0, column=0, padx=10, pady=10)

    etiqueta_x0 = tk.Label(root, text="Ingresa el valor de x:")
    etiqueta_x0.grid(row=1, column=0, padx=10, pady=10)

    # Entradas
    entradaFuncion = tk.Entry(root)
    entradaFuncion.grid(row=0, column=1, padx=10, pady=10)

    entrada_x0 = tk.Entry(root)
    entrada_x0.grid(row=1, column=1, padx=10, pady=10)

    botonCalcularNewton = tk.Button(root, text="Calcular")
    botonCalcularNewton.grid(row=2, column=1, padx=10, pady=10)

    return entradaFuncion, entrada_x0, botonCalcularNewton