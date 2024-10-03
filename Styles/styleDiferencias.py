import tkinter as tk

def aplicar_estilos(root):
    """Aplica los estilos básicos a la ventana principal y crea el diseño"""
    root.title("Método diferencias divididas")
    root.geometry("400x400")

    # Etiqueta para solicitar el número de elementos
    etiqueta_num_elementos = tk.Label(root, text="Por favor, ingrese el número de elementos de entrada:")
    etiqueta_num_elementos.grid(row=0, column=0, padx=10, pady=10)

    # Entrada para el número de elementos
    entrada_num_elementos = tk.Entry(root)
    entrada_num_elementos.grid(row=0, column=1, padx=10, pady=10)

    # Botón para continuar
    boton_continuar = tk.Button(root, text="Continuar")
    boton_continuar.grid(row=1, column=1, padx=10, pady=10)

    # Etiqueta para mostrar mensajes de error
    etiqueta_error = tk.Label(root, text="")
    etiqueta_error.grid(row=2, column=0, columnspan=2)

    return entrada_num_elementos, boton_continuar, etiqueta_error

def mostrar_campos_de_entrada(root, num_elementos, boton_calcular):
    """Genera los campos de entrada para las funciones f(xi) hasta f(xn)"""
    entradas = []
    
    for i in range(num_elementos+1):
        etiqueta_funcion = tk.Label(root, text=f"Ingrese su función f(x{i}):")
        etiqueta_funcion.grid(row=i + 3, column=0, padx=10, pady=5)
        
        entrada_funcion = tk.Entry(root)
        entrada_funcion.grid(row=i + 3, column=1, padx=10, pady=5)
        entradas.append(entrada_funcion)

    # Coloca el botón "Calcular" debajo de los campos
    boton_calcular.grid(row=num_elementos + 10, column=1, padx=10, pady=10)

    # Desactiva el botón "Calcular" hasta que todos los campos estén llenos
    def verificar_campos(event=None):
        if all(entrada.get() for entrada in entradas):
            boton_calcular.config(state="normal")
        else:
            boton_calcular.config(state="disabled")

    for entrada in entradas:
        entrada.bind("<KeyRelease>", verificar_campos)

    boton_calcular.config(state="disabled")

    return entradas
