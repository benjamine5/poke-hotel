from tkinter import *
import subprocess  #libreria para abrir interfaz de actividades

ventana = Tk()
ventana.geometry("800x600")
ventana.config(bg="black")
ventana.title("Registro")

ventana.iconbitmap("pokemon.ico")
Frame1=Frame()
Frame1.pack(fill="both",expand="True")

Frame1.config()
Frame1.config(width="1010",height="600")
Frame1.config(bd=25)
Frame1.config(relief="sunken")
Imagen1=PhotoImage(file="Pokemon.png")
label2 = Label(Frame1,image=Imagen1 )
label2.place(x=350, y=100)

valor=StringVar()
drop=OptionMenu(ventana,valor,"Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho", "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Hielo", "Dragón", "Siniestro", "Hada")
drop.pack()
drop.place(x=250,y=150)
valor2=StringVar()
drop1=OptionMenu(ventana,valor2,"Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho", "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Hielo", "Dragón", "Siniestro", "Hada")
drop1.pack()
drop1.place(x=250,y=190)

CuadroNombre=Entry(Frame1)
CuadroNombre.grid(row=1, column=1,padx=10,pady=10)
CuadroNombre.config(fg="red",justify="center" )
ContLabel=Label(Frame1,text="Nombre Entrenador:")
ContLabel.grid(row=1, column=0,padx=10,pady=10)

# Crear campo de entrada para el apellido
CuadroApellido = Entry(Frame1)
CuadroApellido.grid(row=1, column=3, padx=10, pady=10)
CuadroApellido.config(fg="red", justify="center")
ApellidoLabel = Label(Frame1, text="Apellido Entrenador:")
ApellidoLabel.grid(row=1, column=2, padx=10, pady=10)

# Crear campo de entrada para el Rut
CuadroRut = Entry(Frame1)
CuadroRut.grid(row=3, column=1, padx=10, pady=10)
CuadroRut.config(fg="red", justify="center")
RutLabel = Label(Frame1, text="Rut Entrenador:")
RutLabel.grid(row=3, column=0, padx=10, pady=10)

# Crear campo de entrada para el Teléfono
CuadroTelefono = Entry(Frame1)
CuadroTelefono.grid(row=3, column=3, padx=10, pady=10)
CuadroTelefono.config(fg="red", justify="center")
TelefonoLabel = Label(Frame1, text="Teléfono Entrenador:")
TelefonoLabel.grid(row=3,column=2,padx=10,pady=10)



# Crear campo de entrada para el nombre del Pokémon
CuadroNombrePokemon = Entry(Frame1)
CuadroNombrePokemon.grid(row=5, column=1, padx=10, pady=10)
CuadroNombrePokemon.config(fg="red", justify="center")
NombrePokemonLabel = Label(Frame1, text="Nombre del Pokémon:")
NombrePokemonLabel.grid(row=5, column=0, padx=10, pady=10)

# Crear campo de entrada para el tipo del Pokémon
TipoPokemonLabel = Label(Frame1, text="Tipo del Pokémon:")
TipoPokemonLabel.grid(row=6, column=0, padx=10, pady=10)

# Crear campo de entrada para el segundo tipo del Pokémon
SegundoTipoPokemonLabel = Label(Frame1, text="Segundo Tipo del Pokémon:")
SegundoTipoPokemonLabel.grid(row=7, column=0, padx=10, pady=10)

# Crear campo de entrada para la edad del Pokémon
CuadroEdadPokemon = Entry(Frame1)
CuadroEdadPokemon.grid(row=8, column=1, padx=10, pady=10)
CuadroEdadPokemon.config(fg="red", justify="center")
EdadPokemonLabel = Label(Frame1, text="Edad del Pokémon:")
EdadPokemonLabel.grid(row=8, column=0, padx=10, pady=10)

# Crear campo de entrada para el tiempo de estadía del Pokémon
CuadroTiempoEstadia = Entry(Frame1)
CuadroTiempoEstadia.grid(row=9, column=1, padx=10, pady=10)
CuadroTiempoEstadia.config(fg="red", justify="center")
TiempoEstadiaLabel = Label(Frame1, text="Dias de Estadía del Pokémon:")
TiempoEstadiaLabel.grid(row=9, column=0, padx=10, pady=10)



#Funcion para que el boton "registrarse" ejecute la interfaz de actividades
#mezcle ambas funciones ya que el boton no permite dos command
def abrirPrograma():
    Nombre_entrenador=CuadroNombre.get()
    Apellido=CuadroApellido.get()
    Rut = CuadroRut.get()
    Telefono= CuadroTelefono
    nombre_pokemon = CuadroNombrePokemon.get()
    edad_pokemon = CuadroEdadPokemon.get()
    tiempo_estadia = CuadroTiempoEstadia.get()
    
    print("Datos guardados:")
    print("Nombre del Pokémon:", nombre_pokemon)
    print("Edad del Pokémon:", edad_pokemon)
    print("Dias de Estadía del Pokémon:", tiempo_estadia)
    
    
    subprocess.Popen(["python", "interfasActividades.py"]) #abrir la siguiente interfaz

# Crear botón de guardar
botomRegister = Button(ventana, text="Registrarse",command=abrirPrograma ,fg="Black", font=("Times New Roman", 20))
botomRegister.place(x=300, y=400)


ventana.mainloop()
