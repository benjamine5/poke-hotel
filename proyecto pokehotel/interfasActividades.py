import tkinter as tk
from tkinter import *
import subprocess
import json

# Función recopiladora de datos de los checkbuttons 
def compra():
    totalActividades = 0
    if paseo.get() == 1:
        totalActividades += 16000
    if nadar.get() == 1:
        totalActividades += 20000
    if fogata.get() == 1:
        totalActividades += 10000
    if juegos.get() == 1:
        totalActividades += 5000
    
    print(totalActividades)
    
    Total = {
        "actividades" : totalActividades,
    }
    
    # Convertir diccionario a JSON y guardar en un archivo
    ValorTotal = json.dumps(Total, indent=4)
    with open("Actividades_data.json", "w") as f:
        f.write(ValorTotal)    

# Función para abrir la ventana de pago
def abrir_pago():
    subprocess.Popen(["python", "Pago.py"])

# Creación de la ventana principal
raiz = tk.Tk()
raiz.geometry("800x600")
raiz.title("Actividades")
raiz.config(bd=10, relief="groove")
raiz.iconbitmap("pokemon/hotel.ico")

# Texto de actividad
frameActividad = Frame(raiz)
frameActividad.pack(side="top", fill="x")
frameActividad.config(bd=10, relief="groove")
Label(frameActividad, text="Actividades", font=("Times New Romans", 35)).pack()

nadar = IntVar()
fogata = IntVar()
juegos = IntVar()
paseo = IntVar()

# Lista de actividades
Opcion1 = Checkbutton(raiz, text="Paseo ($16.000)", font=("Times New Romans", 25), variable=paseo, onvalue=1, offvalue=0, command=compra)
Opcion1.place(x=150, y=125)

Opcion2 = Checkbutton(raiz, text="Nadar ($20.000)", font=("Times New Romans", 25), variable=nadar, onvalue=1, offvalue=0, command=compra)
Opcion2.place(x=150, y=200)

Opcion3 = Checkbutton(raiz, text="Fogata ($10.000)", font=("Times New Romans", 25), variable=fogata, onvalue=1, offvalue=0, command=compra)
Opcion3.place(x=150, y=275)

Opcion4 = Checkbutton(raiz, text="Juegos ($5.000)", font=("Times New Romans", 25), variable=juegos, onvalue=1, offvalue=0, command=compra)
Opcion4.place(x=150, y=350)

# Botón siguiente
botonEnvio = Button(raiz, text="Siguiente", font=("Times New Romans", 20), command=abrir_pago)
botonEnvio.place(x=500, y=450)

raiz.mainloop()
