import tkinter as tk
import subprocess

def abrirDerivadas():
    subprocess.Popen(["python", "derivadas.py"])
    botonDerivadas.config(state=tk.DISABLED)    
    
def abrirRichardson():
    subprocess.Popen(["python", "derivadas.py"])
    botonRichardon.config(state=tk.DISABLED)
    
def abrirSecante():
    subprocess.Popen(["python", "derivadas.py"])
    botonSecante.config(state=tk.DISABLED)
    
def abrirDiferencias():
    subprocess.Popen(["python", "derivadas.py"])
    botonDiferencias.config(state=tk.DISABLED)
    
def abrirTrapecio():
    subprocess.Popen(["python", "derivadas.py"])
    botonTrapecio.config(state=tk.DISABLED)
    


# Configuración de la ventana principal 'main'
root = tk.Tk()
root.title("Interfaz principal")

# Hacemos la ventana responsiva
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Configura marco principal
frame = tk.Frame(root, bg="#F0F8FF", padx=20, pady=20)
frame.grid(sticky="nsew")

# Botón para Derivadas
botonDerivadas = tk.Button(frame, text="Derivadas", font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonDerivadas.pack(pady=20)

# Botón para Extrapolación de Richardson
botonRichardon = tk.Button(frame, text="Extrapolación de Richardson", font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonRichardon.pack(pady=20)

# Botón para Secantes
botonSecante = tk.Button(frame, text="Secantes", font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonSecante.pack(pady=20)

# Botón para diferencias divididas
botonDiferencias = tk.Button(frame, text="diferencias divididas", font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonDiferencias.pack(pady=20)

# Botón para Trapecio
botonTrapecio = tk.Button(frame, text="Trapecio", font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonTrapecio.pack(pady=20)


# Ajustar el tamaño mínimo de la ventana
root.minsize(400, 200)

# Loop principal de la aplicación
root.mainloop()