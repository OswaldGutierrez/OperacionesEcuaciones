import tkinter as tk

def aplicarEstiloDerivadas(root):
    """Aplica los estilos básicos a la ventana principal y retorna los widgets necesarios"""
    root.title("Realiza tus derivadas")
    
    # Hacer que la ventana sea responsiva
    root.rowconfigure(0, weight=1)
    root.columnconfigure([0, 1, 2], weight=1)
    root.rowconfigure(1, weight=1)

    # Etiquetas
    etiquetaFuncion = tk.Label(root, text="Por favor ingresa tu función f(x)=")
    etiquetaFuncion.grid(row=0, column=0, padx=10, pady=10)

    etiquetax0 = tk.Label(root, text="Ingresa el valor de x0:")
    etiquetax0.grid(row=1, column=0, padx=10, pady=10)

    # Entradas
    entradaFuncion = tk.Entry(root)
    entradaFuncion.grid(row=0, column=1, padx=10, pady=10)

    entradax0 = tk.Entry(root)
    entradax0.grid(row=1, column=1, padx=10, pady=10)

    # Botones para calcular la derivada con diferentes métodos
    botonCalcular2 = tk.Button(root, text="Calcular para 2 puntos")
    botonCalcular2.grid(row=2, column=0, padx=10, pady=10)

    botonCalcular3 = tk.Button(root, text="Calcular para 3 puntos")
    botonCalcular3.grid(row=2, column=1, padx=10, pady=10)

    botonCalcular5 = tk.Button(root, text="Calcular para 5 puntos")
    botonCalcular5.grid(row=2, column=2, padx=10, pady=10)

    return entradaFuncion, entradax0, botonCalcular2, botonCalcular3, botonCalcular5
