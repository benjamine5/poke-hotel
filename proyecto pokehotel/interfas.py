# lo necesario (crear un venv)
import tkinter as tk
import subprocess #la libreria para abrir lo demas
from PIL import Image, ImageTk

# creamos la pestaña
raiz = tk.Tk()
raiz.title("Hotel Pokemon")
raiz.iconbitmap("pokemon.ico")
raiz.geometry('800x600')

# imagen de fondo
image = Image.open("image.png")
image = image.resize((800, 600))
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(raiz, image=photo_image)
image_label.pack()

# agregamos 2 botones
def Reserva():
    subprocess.Popen(["python","seatSelection.py"])

def Estado():
    print("si lo clickearon ")

button1 = tk.Button(raiz, text="Reservar Habitacion", command=Reserva, font=("Times New Romans", 21))
button1.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

button2 = tk.Button(raiz, text="Estado del Pokemon", command=Estado, font=("Times New Romans", 20))
button2.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# si se reajusta el tamaño
raiz.resizable(True, True)

#main loop
raiz.mainloop()
