#importamos las librerias
from tkinter import *

#creamos la ventana
raiz=Tk()
raiz.geometry("800x600")
raiz.title("Actividades")
raiz.config(bd=10, relief="groove")
raiz.iconbitmap("pokemon.ico")

#texto actividad
frameActividad=Frame(raiz)
frameActividad.pack(side="top", fill="x")
frameActividad.config(bd=10, relief="groove")
Label(frameActividad, text="Actividades", font=("Times New Romans", 35)).pack()

#Lista de actividades
Checkbutton(raiz, text="Paseo", font=("Times New Romans", 25)).place(x=150, y=125)
Checkbutton(raiz, text="Nadar", font=("Times New Romans", 25)).place(x=150, y=200)
Checkbutton(raiz, text="Fogata", font=("Times New Romans", 25)).place(x=150, y=275)
Checkbutton(raiz, text="sJuegos", font=("Times New Romans", 25)).place(x=150, y=350)

#boton siguiente
def codigoBoton():
    print("Boton presionado")
botonEnvio=Button(raiz, text="Siguiente", font=("Times New Romans", 20), command=codigoBoton)
botonEnvio.place(x=500, y=450)

#main loop ;3
raiz.mainloop()