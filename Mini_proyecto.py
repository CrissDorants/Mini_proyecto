#Estas son las librerias utilizadas para la aplicación
#Utilizamos tk.Tk() para crear la ventana principal de la aplicación.
import tkinter as tk
from tkinter import messagebox
import secrets
import string
#Se crea una función con la cual vamos a generar nuestra contraseña
def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))#Utilizamos secrets.choice() para seleccionar caracteres aleatorios de un conjunto que incluye letras, dígitos y signos de puntuación.
    return contraseña
#Se crea otra funcion con la cual vamos a dar muestra de la contraseña ya generada
def mostrar_contraseña():
    try:
        longitud = int(entrada_longitud.get())
        if longitud < 8:
            messagebox.showwarning("Advertencia", "La longitud mínima recomendada es 8 caracteres.")
            return
        contraseña = generar_contraseña(longitud)
        etiqueta_contraseña.config(text=f"Contraseña generada: {contraseña}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")#messagebox se utiliza para mostrar mensajes de advertencia o error.
#Creamos nuestra ventana en la cual mostraremos nuestra información
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x200")

#Creamos etiquetas con instrucciones y atributos
#Creamos varios widgets como Label, Entry, y Button para construir la interfaz gráfica.
etiqueta_instruccion = tk.Label(ventana, text="Introduce la longitud de la contraseña:")
etiqueta_instruccion.pack(pady=10)
#Creamos una entrada donde será ingresada la contraseña
entrada_longitud = tk.Entry(ventana)
entrada_longitud.pack(pady=10)
#Se crean los botones para dar funcionalidad a las funciones
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=mostrar_contraseña)
boton_generar.pack(pady=10)
#Se crea una etiqueta que nos muestre cuando la contraseña ya sea creada
etiqueta_contraseña = tk.Label(ventana, text="Contraseña generada: ")
etiqueta_contraseña.pack(pady=10)

#Este mini-proyecto demuestra cómo las librerías externas como tkinter y secrets pueden facilitar la programación en Python:
#tkinter simplifica la creación de interfaces gráficas, haciendo que la aplicación sea más accesible para el usuario final.
#secrets asegura que las contraseñas generadas sean seguras y adecuadas para su uso en aplicaciones que requieren alta seguridad.
ventana.mainloop()