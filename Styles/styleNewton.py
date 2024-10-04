import tkinter as tk

def aplicarEstilosNewton(root):
    """Aplica los estilos básicos a la ventana principal y retorna los widgets necesarios"""
    root.title("Método Newton")
    
    # Hacer que la ventana sea responsiva
    root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)  # Agregar una fila más
    root.columnconfigure([0, 1], weight=1)

    # Etiquetas
    etiquetaFuncion = tk.Label(root, text="Por favor ingresa tu función f(x)=")
    etiquetaFuncion.grid(row=0, column=0, padx=10, pady=10)

    etiqueta_p0 = tk.Label(root, text="Ingresa el valor de p0:")
    etiqueta_p0.grid(row=1, column=0, padx=10, pady=10)

    etiquetaTolerancia = tk.Label(root, text="Ingresa el valor de tolerancia:")
    etiquetaTolerancia.grid(row=2, column=0, padx=10, pady=10)

    etiquetaIteraciones = tk.Label(root, text="Ingresa el valor de iteraciones máximas:")
    etiquetaIteraciones.grid(row=3, column=0, padx=10, pady=10)

    # Entradas
    entradaFuncion = tk.Entry(root)
    entradaFuncion.grid(row=0, column=1, padx=10, pady=10)

    entrada_p0 = tk.Entry(root)
    entrada_p0.grid(row=1, column=1, padx=10, pady=10)

    entradaTolerancia = tk.Entry(root)
    entradaTolerancia.grid(row=2, column=1, padx=10, pady=10)

    entradaIteraciones = tk.Entry(root)
    entradaIteraciones.grid(row=3, column=1, padx=10, pady=10)

    botonCalcularNewton = tk.Button(root, text="Calcular Newton")
    botonCalcularNewton.grid(row=4, column=1, padx=10, pady=10)

    botonCalcularSecante = tk.Button(root, text="Calcular Secante")
    botonCalcularSecante.grid(row=5, column=1, padx=10, pady=10)  # Agregar botón de secante

    return (entradaFuncion, entrada_p0, entradaTolerancia, 
            entradaIteraciones, botonCalcularNewton, botonCalcularSecante)

