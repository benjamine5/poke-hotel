# lo necesario (crear un venv)
import tkinter as tk
from PIL import Image, ImageTk

# creamos la pestaña
raiz = tk.Tk()
raiz.geometry('400x400')  # Set the initial size of the window

# imagen del ditto
image = Image.open("ditto.png")
image = image.resize((200, 200)) # Set the desired width and height of the image
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(raiz, image=photo_image)
image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# boton
def on_button_click():
    print("clickeado")

button = tk.Button(raiz, text="clickeame", command=on_button_click)
button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# si se reagusta el tamaño
raiz.resizable(True, True)

#main loop
raiz.mainloop()
