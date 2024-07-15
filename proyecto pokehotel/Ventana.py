from tkinter import *

ventana = Tk()
ventana.geometry("1000x600")
ventana.config(bg="black")
ventana.title("Poke Hotel")

ventana.iconbitmap("pokemon/hotel.ico")
Frame1=Frame()
Frame1.pack(fill="both",expand="True")
Frame1.config(bg="cyan")
Frame1.config()
Frame1.config(width="1010",height="600")
Frame1.config(bd=25)
Frame1.config(relief="sunken")
Frame1.config(cursor="pirate")



Imagen1=PhotoImage(file="pokemon/OIG3.png")
label2 = Label(Frame1,image=Imagen1 )
label2.place(x=400, y=200)


botonAd = Button(ventana, text="Administrador", fg="Black", font=("Times New Roman", 20))
botonAd.place(x=1100, y=900)

botomRegister = Button(ventana, text="Registro", fg="Black", font=("Times New Roman", 20))
botomRegister.place(x=600, y=900)
ventana.mainloop()