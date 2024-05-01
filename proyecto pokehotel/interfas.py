# lo necesario (crear un venv)
import tkinter as tk
from PIL import Image, ImageTk

# creamos la pestaña
raiz = tk.Tk()
raiz.geometry('400x400')  # Set the initial size of the window
raiz.iconbitmap("pokemon.ico")

# imagen del ditto
image = Image.open("ditto.png")
image = image.resize((200, 200)) # Set the desired width and height of the image
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(raiz, image=photo_image)
image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# agregamos 2 botones
def on_button_click1():
    #crea la nueva ventana
    new_window = tk.Tk()

    # cambio del tamaño
    new_window.geometry('600x500')

    # hace las matrices
    for i in range(3):
        matrix = tk.Frame(new_window)
        matrix.pack()

        for j in range(6):
            label = tk.Label(matrix, text=f"Matrix {i+1}, Cell {j+1}")
            label.pack(side=tk.LEFT)

    # el loop de la nueva ventana
    new_window.mainloop()

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
