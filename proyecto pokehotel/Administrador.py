from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk  # Importamos PIL para manejar la imagen

def volver_atras():
    # Aquí puedes definir qué hacer cuando se presione el botón "Atrás"
    subprocess(["python","interfas.py"])

def comprobar_credenciales():
    usuario = CuadroUsuario.get()
    contraseña = CuadroCont.get()

    if not usuario or not contraseña:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")
    else:
        # Aquí puedes añadir la lógica para comprobar las credenciales
        if usuario == "blackcrip" and contraseña == "2468":  
            subprocess.Popen(["python","and.py"])
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = Tk()
ventana.title("Poke Hotel")
ventana.iconbitmap("pokemon/hotel.ico")  # Asegúrate de que el icono está en la ruta correcta
ventana.geometry("300x300")
ventana.resizable(False, False)

# Cargar la imagen
ruta_imagen = "pokemon/LEF.png"  # Asegúrate de que la imagen está en la carpeta "pokemon"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((100, 100), Image.LANCZOS)  # Ajustar el tamaño si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un label para mostrar la imagen
label_imagen = Label(ventana, image=imagen_tk)
label_imagen.pack(pady=10)

FrameAd = Frame(ventana, width=600, height=400)
FrameAd.pack()

CuadroUsuario = Entry(FrameAd)
CuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
CuadroUsuario.config(fg="red", justify="center",font=("Times New Roman", 10))
UsuLabel = Label(FrameAd, text="Usuario:",font=("Times New Roman", 15))
UsuLabel.grid(row=0, column=0, padx=10, pady=10)

CuadroCont = Entry(FrameAd)
CuadroCont.grid(row=1, column=1, padx=10, pady=10)
CuadroCont.config(fg="red", justify="center", show="*",font=("Times New Roman", 10))
ContLabel = Label(FrameAd, text="Contraseña:",font=("Times New Roman", 15))
ContLabel.grid(row=1, column=0, padx=10, pady=10)

# Crear un Frame adicional para los botones
FrameBotones = Frame(ventana)
FrameBotones.pack(pady=20)

BotonAtras = Button(FrameBotones, text="Atrás", font=("Times New Roman", 11),command=volver_atras)
BotonAtras.pack(side=LEFT, padx=20)

BotonComprobacion = Button(FrameBotones, text="Entrar",font=("Times New Roman", 11) ,command=comprobar_credenciales)
BotonComprobacion.pack(side=RIGHT, padx=20)

ventana.mainloop()