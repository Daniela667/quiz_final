import tkinter as tk
from tkinter import messagebox

def limpiar():
    entrada_USD.delete(0, tk.END)
    label2.config(text="")
    
def convertir():
    entrada = entrada_USD.get()
    if entrada.isdigit():
        num = float(entrada)
        resultado = num/513.70
        label2.config(text=f"{resultado:.2f} CRC")
    else:
        messagebox.showerror("Error", "Por favor, ingresa solo números")

def confirmar_salida():
    respuesta1 = messagebox.askyesno("Confirmar", "¿Estás seguro que desea salir?")
    if respuesta1:
        respuesta2 = messagebox.askyesno("Confirmar", "¿Muy seguro?") 
        if respuesta2:
         ventana.destroy()

def widgets():
    label1 = tk.Label(ventana, font=("Helvetica", 12), fg="blue", text="Monto en USD:")
    label1.grid(row=0, column=0, padx=10, pady=10)
    
    entrada_USD.grid(row=0, column=1, padx=10, pady=10)
    
    boton_convertir = tk.Button(ventana, text="Convertir", command=convertir,font=("Helvetica", 10), fg="blue")
    boton_convertir.grid(row=1, column=0, padx=10, pady=10)

    boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar,font=("Helvetica", 10), fg="blue")
    boton_limpiar.grid(row=1, column=1, padx=10, pady=10)

    label2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de conversor de unidades")

entrada_USD = tk.Entry(ventana)
label2 = tk.Label(ventana, text="")

widgets()

ventana.protocol("WM_DELETE_WINDOW", confirmar_salida)

# Ejecutar la aplicación
ventana.mainloop()