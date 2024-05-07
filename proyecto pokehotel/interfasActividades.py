from tkinter import *

#Funcion recopiladora de datos de los checkbuttons (odie esta parte -n-)
def compra():
    if(paseo.get()==1):
        print("Paseo seleccionado")
    else:
        print("Paseo sin Seleccionar")
    if(nadar.get()==1):
        print("Nadar Seleccionado")
    else:
        print("Nadar sin Seleccionar")
    if(fogata.get()==1):
        print("Fogata Seleccionado")
    else:
        print("Fogata sin Seleccionar")
    if(juegos.get()==1):
        print("Juegos Seleccionado")
    else:
        print("Juegos sin Seleccionar")
    

#creamos la ventana :D
raiz=Tk()
raiz.geometry("800x600")
raiz.title("Actividades")
raiz.config(bd=10, relief="groove")
raiz.iconbitmap("pokemon.ico")

#texto actividad ;)
frameActividad=Frame(raiz)
frameActividad.pack(side="top", fill="x")
frameActividad.config(bd=10, relief="groove")
Label(frameActividad, text="Actividades", font=("Times New Romans", 35)).pack()

nadar=IntVar()
fogata=IntVar()
juegos=IntVar()
paseo=IntVar()

#Lista de actividades D:
Opcion1=Checkbutton(raiz, text="Paseo", font=("Times New Romans", 25), variable=paseo, onvalue=1, offvalue=0, command=compra).place(x=150, y=125)
Opcion2=Checkbutton(raiz, text="Nadar", font=("Times New Romans", 25), variable=nadar, onvalue=1, offvalue=0, command=compra).place(x=150, y=200)
Opcion3=Checkbutton(raiz, text="Fogata", font=("Times New Romans", 25), variable=fogata, onvalue=1, offvalue=0, command=compra).place(x=150, y=275)
Opcion4=Checkbutton(raiz, text="Juegos", font=("Times New Romans", 25), variable=juegos, onvalue=1, offvalue=0, command=compra).place(x=150, y=350)

#boton siguiente :>
def codigoBoton():
    print("Boton presionado")
botonEnvio=Button(raiz, text="Siguiente", font=("Times New Romans", 20), command=codigoBoton)
botonEnvio.place(x=500, y=450)

#main loop ;3
raiz.mainloop()
