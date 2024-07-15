from tkinter import *

def open_admin_window():
    # Ocultar la ventana de inicio de sesión actual
    ventana.withdraw()

    # Crear la ventana de administración
    admin_window = Tk()
    admin_window.title("Ventana de Administración")
    admin_window.geometry("400x200")

    # Agregar widgets a la ventana de administración
    label = Label(admin_window, text="Bienvenido a la Ventana de Administración")
    label.pack()

    # Crear una función para volver atrás a la ventana de inicio de sesión
    def go_back():
        admin_window.destroy()
        ventana.deiconify()  # Mostrar la ventana de inicio de sesión nuevamente

    # Agregar un botón para volver atrás
    back_button = Button(admin_window, text="Atrás", command=go_back)
    back_button.pack()

    admin_window.mainloop()

# Crear la ventana de inicio de sesión
ventana = Tk()
FrameAd = Frame(ventana, width=600, height=400)
FrameAd.pack()

ventana.title("Poke Hotel")
ventana.iconbitmap("pokemon/hotel.ico")
ventana.geometry("300x300")
ventana.resizable(False, False)

CuadroUsuario = Entry(FrameAd)
CuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
CuadroUsuario.config(fg="red", justify="center")
UsuLabel = Label(FrameAd, text="Usuario:")
UsuLabel.grid(row=0, column=0, padx=10, pady=10)

CuadroCont = Entry(FrameAd)
CuadroCont.grid(row=1, column=1, padx=10, pady=10)
CuadroCont.config(fg="red", justify="center")
ContLabel = Label(FrameAd, text="Contraseña:")
ContLabel.grid(row=1, column=0, padx=10, pady=10)
CuadroCont.config(show=" ")

BotonAtras = Button(ventana, text="Atrás")
BotonAtras.pack()

BotonComprobacion = Button(ventana, text="Entrar", command=open_admin_window)
BotonComprobacion.pack()

ventana.mainloop()