from tkinter import *
from tkinter import messagebox
import subprocess
import json
import datetime
import re

def validar_rut(rut):
    """Valida el formato del RUT chileno."""
    if not re.match(r"^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$", rut):
        return False
    return True

def validar_telefono(telefono):
    """Valida el formato del teléfono (8 dígitos)."""
    return telefono.isdigit() and len(telefono) == 8

def solo_numeros(P):
    """Valida que la entrada contenga solo números"""
    return P.isdigit() or P == ""

def abrirPrograma():
    Nombre_entrenador = CuadroNombre.get()
    Apellido = CuadroApellido.get()
    Rut = CuadroRut.get()
    Telefono = CuadroTelefono.get()
    nombre_pokemon = CuadroNombrePokemon.get()
    tipo_pokemon = valor.get()
    segundo_tipo_pokemon = valor2.get()
    edad_pokemon = CuadroEdadPokemon.get()
    tiempo_estadia = CuadroTiempoEstadia.get()
    
        # Validar RUT
    if not validar_rut(Rut):
        messagebox.showerror("Error", "RUT no válido. Debe tener el formato XX.XXX.XXX-X.")
        return
    
    # Validar Teléfono
    if not validar_telefono(Telefono):
        messagebox.showerror("Error", "Teléfono no válido. Debe contener 8 dígitos.")
        return

    # Guardar datos en un diccionario
    pokemon_data = {
        "nombre": Nombre_entrenador,
        "apellido": Apellido,
        "rut": Rut,
        "telefono": Telefono,
        "pokemon_name": nombre_pokemon,
        "tipo_pokemon": tipo_pokemon,
        "segundo_tipo_pokemon": segundo_tipo_pokemon,
        "edad_pokemon": edad_pokemon,
        "tiempo_estadia": tiempo_estadia,
        "hora_actual": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Convertir diccionario a JSON y guardar en un archivo
    pokemon_data_json = json.dumps(pokemon_data, indent=4)
    with open("pokemon_data.json", "w") as f:
        f.write(pokemon_data_json)

    print("Datos guardados en pokemon_data.json")
    print("Datos guardados:")
    print(pokemon_data)

    # Ejecutar otro script (asegurarse de que interfasActividades.py exista y funcione)
    subprocess.Popen(["python", "interfasActividades.py"])

ventana = Tk()
ventana.geometry("800x600")
ventana.config(bg="black")
ventana.title("Registro")
ventana.iconbitmap("pokemon.ico")

Frame1 = Frame(ventana, width=1010, height=600, bd=25, relief="groove")
Frame1.pack(fill="both", expand=True)

Imagen1 = PhotoImage(file="Pokemon.png")
label2 = Label(Frame1, image=Imagen1)
label2.place(x=350, y=100)

valor = StringVar()
drop = OptionMenu(ventana, valor, "Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho", "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Hielo", "Dragón", "Siniestro", "Hada")
drop.pack()
drop.place(x=250, y=150)

valor2 = StringVar()
drop1 = OptionMenu(ventana, valor2, "Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho", "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Hielo", "Dragón", "Siniestro", "Hada")
drop1.pack()
drop1.place(x=250, y=190)

CuadroNombre = Entry(Frame1)
CuadroNombre.grid(row=1, column=1, padx=10, pady=10)
CuadroNombre.config(fg="red", justify="center")
ContLabel = Label(Frame1, text="Nombre entrenador:", font=("Times New Roman", 10))
ContLabel.grid(row=1, column=0, padx=10, pady=10)

CuadroApellido = Entry(Frame1)
CuadroApellido.grid(row=1, column=3, padx=10, pady=10)
CuadroApellido.config(fg="red", justify="center")
ApellidoLabel = Label(Frame1, text="Apellido entrenador:", font=("Times New Roman", 10))
ApellidoLabel.grid(row=1, column=2, padx=10, pady=10)

CuadroRut = Entry(Frame1)
CuadroRut.grid(row=3, column=1, padx=10, pady=10)
CuadroRut.config(fg="red", justify="center")
RutLabel = Label(Frame1, text="Rut entrenador:", font=("Times New Roman", 10))
RutLabel.grid(row=3, column=0, padx=10, pady=10)

CuadroTelefono = Entry(Frame1)
CuadroTelefono.grid(row=3, column=3, padx=10, pady=10)
CuadroTelefono.config(fg="red", justify="center")
TelefonoLabel = Label(Frame1, text="Teléfono entrenador:", font=("Times New Roman", 10))
TelefonoLabel.grid(row=3, column=2, padx=10, pady=10)

CuadroNombrePokemon = Entry(Frame1)
CuadroNombrePokemon.grid(row=5, column=1, padx=10, pady=10)
CuadroNombrePokemon.config(fg="red", justify="center")
NombrePokemonLabel = Label(Frame1, text="Nombre del Pokémon:", font=("Times New Roman", 10))
NombrePokemonLabel.grid(row=5, column=0, padx=10, pady=10)

TipoPokemonLabel = Label(Frame1, text="Tipo del Pokémon:", font=("Times New Roman", 10))
TipoPokemonLabel.grid(row=6, column=0, padx=10, pady=10)

SegundoTipoPokemonLabel = Label(Frame1, text="Segundo tipo del Pokémon:", font=("Times New Roman", 10))
SegundoTipoPokemonLabel.grid(row=7, column=0, padx=10, pady=10)

CuadroEdadPokemon = Entry(Frame1)
CuadroEdadPokemon.grid(row=8, column=1, padx=10, pady=10)
CuadroEdadPokemon.config(fg="red", justify="center")
EdadPokemonLabel = Label(Frame1, text="Edad del Pokémon:", font=("Times New Roman", 10))
EdadPokemonLabel.grid(row=8, column=0, padx=10, pady=10)

CuadroTiempoEstadia = Entry(Frame1)
CuadroTiempoEstadia.grid(row=9, column=1, padx=10, pady=10)
CuadroTiempoEstadia.config(fg="red", justify="center")
TiempoEstadiaLabel = Label(Frame1, text="Días de estadía del Pokémon:", font=("Times New Roman", 10))
TiempoEstadiaLabel.grid(row=9, column=0, padx=10, pady=10)

botomRegister = Button(ventana, text="Registrar", command=abrirPrograma, fg="Black", font=("Times New Roman", 20))
botomRegister.place(x=300, y=400)

ventana.mainloop()
