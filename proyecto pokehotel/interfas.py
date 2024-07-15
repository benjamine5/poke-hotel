# lo necesario (crear un venv)
import tkinter as tk
import subprocess #para llamar a las interfaces
from PIL import Image, ImageTk #la libreria para abrir lo demas #type: ignore

# creamos la pestaña
raiz = tk.Tk()
raiz.title("Hotel Pokémon")
raiz.iconbitmap("pokemon/hotel.ico")
raiz.geometry('800x600')

# imagen de fondo
image = Image.open("pokemon/image.png")
image = image.resize((800, 600))
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(raiz, image=photo_image)
image_label.pack()

# agregamos 2 botones
def Reserva():
    subprocess.Popen(["python","Registro.py"])

def Estado():
    subprocess.Popen(["python","Administrador.py"])

button1 = tk.Button(raiz, text="Reserva de habitación", command=Reserva, font=("Times New Romans", 21))
button1.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

button2 = tk.Button(raiz, text="Administrador", command=Estado, font=("Times New Romans", 20))
button2.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# si se reajusta el tamaño
raiz.resizable(True, True)

#main loop
raiz.mainloop()