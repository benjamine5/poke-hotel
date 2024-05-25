# lo necesario (crear un venv)
import tkinter as tk
import subprocess #la libreria para abrir lo demas
from PIL import Image, ImageTk

# creamos la pestaña
raiz = tk.Tk()
raiz.geometry('400x400')

# imagen de fondo
image = Image.open("image.png")
image = image.resize((400, 400))
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(raiz, image=photo_image)
image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# agregamos 2 botones
def on_button_click1():
    subprocess.Popen(["python","seatSelection.py"])

def on_button_click2():
    print("si lo clickearon ")

button1 = tk.Button(raiz, text="reverva", command=on_button_click1)
button1.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

button2 = tk.Button(raiz, text="Clickeame", command=on_button_click2)
button2.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

# si se reajusta el tamaño
raiz.resizable(True, True)

#main loop
raiz.mainloop()
