from tkinter import *
import subprocess
import json


#Funcion recopiladora de datos de los checkbuttons 
def compra():
    totalActividades=0
    if(paseo.get()==1):
        totalActividades+=2000
    if(nadar.get()==1):
        totalActividades+=2000
    if(fogata.get()==1):
        totalActividades+=2000
    if(juegos.get()==1):
        totalActividades+=2000
    
    print(totalActividades)
    
    
    Total = {
        "actividades" : totalActividades,
    }
    
    # Convertir diccionario a JSON y guardar en un archivo
    ValorTotal = json.dumps(Total, indent=4)
    with open("Actividades_data.json", "w") as f:
        f.write(ValorTotal)    
    

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

nadar=IntVar()
fogata=IntVar()
juegos=IntVar()
paseo=IntVar()

#Lista de actividades 
Opcion1=Checkbutton(raiz, text="Paseo ($2000)", font=("Times New Romans", 25), variable=paseo, onvalue=1, offvalue=0, command=compra).place(x=150, y=125)
Opcion2=Checkbutton(raiz, text="Nadar ($2000)", font=("Times New Romans", 25), variable=nadar, onvalue=1, offvalue=0, command=compra).place(x=150, y=200)
Opcion3=Checkbutton(raiz, text="Fogata ($2000)", font=("Times New Romans", 25), variable=fogata, onvalue=1, offvalue=0, command=compra).place(x=150, y=275)
Opcion4=Checkbutton(raiz, text="Juegos ($2000)", font=("Times New Romans", 25), variable=juegos, onvalue=1, offvalue=0, command=compra).place(x=150, y=350)

#boton siguiente 
def codigoBoton():
    #Asegurar de que Pago.py exista y se ejecute
    subprocess.Popen(["python","Pago.py"])
botonEnvio=Button(raiz, text="Siguiente", font=("Times New Romans", 20), command=codigoBoton)
botonEnvio.place(x=500, y=450)

raiz.mainloop()
