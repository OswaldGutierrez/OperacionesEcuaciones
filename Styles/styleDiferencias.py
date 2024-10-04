import tkinter as tk

def aplicarEstilosDiferencias(root):
    """Aplica los estilos básicos a la ventana principal y crea el diseño"""
    root.title("Método diferencias divididas")
    root.geometry("400x400")

    # Etiqueta para solicitar el número de elementos
    etiquetaNumElementos = tk.Label(root, text="Por favor, ingrese el número de elementos de entrada:")
    etiquetaNumElementos.grid(row=0, column=0, padx=10, pady=10)

    # Entrada para el número de elementos
    entradaNumElementos = tk.Entry(root)
    entradaNumElementos.grid(row=0, column=1, padx=10, pady=10)

    # Botón para continuar
    botonContinuar = tk.Button(root, text="Continuar")
    botonContinuar.grid(row=1, column=1, padx=10, pady=10)

    # Etiqueta para mostrar mensajes de error
    etiquetaError = tk.Label(root, text="")
    etiquetaError.grid(row=2, column=0, columnspan=2)

    return entradaNumElementos, botonContinuar, etiquetaError

def mostrarCamposDeEntrada(root, numElementos, botonCalcular):
    """Genera los campos de entrada para las funciones f(xi) hasta f(xn)"""
    entradas = []
    
    for i in range(numElementos+1):
        etiquetaFuncion = tk.Label(root, text=f"Ingrese su función f(x{i}):")
        etiquetaFuncion.grid(row=i + 3, column=0, padx=10, pady=5)
        
        entradaFuncion = tk.Entry(root)
        entradaFuncion.grid(row=i + 3, column=1, padx=10, pady=5)
        entradas.append(entradaFuncion)

    # Coloca el botón "Calcular" debajo de los campos
    botonCalcular.grid(row=numElementos + 10, column=1, padx=10, pady=10)

    # Desactiva el botón "Calcular" hasta que todos los campos estén llenos
    def verificarCampos(event=None):
        if all(entrada.get() for entrada in entradas):
            botonCalcular.config(state="normal")
        else:
            botonCalcular.config(state="disabled")

    for entrada in entradas:
        entrada.bind("<KeyRelease>", verificarCampos)

    botonCalcular.config(state="disabled")

    return entradas
