import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

# Cargar datos desde un archivo JSON
with open('datos.json', 'r') as file:
    datos_habitaciones = json.load(file)

# Datos de prueba: habitaciones ocupadas (simulación)
habitaciones_ocupadas = [datos_habitaciones["Habitacion"]]

def mostrar_datos_habitacion(habitacion_seleccionada):
    # Verificar si la habitación seleccionada está ocupada
    if habitacion_seleccionada in habitaciones_ocupadas:
        # Crear una nueva ventana
        ventana_datos = tk.Toplevel()
        ventana_datos.title(f"Datos de Habitación {habitacion_seleccionada}")
        ventana_datos.geometry("500x800")

        # Mostrar los datos de la habitación ocupada
        lbl_datos_habitacion = tk.Label(ventana_datos, text=f"Habitación {habitacion_seleccionada}", font=("Times New Roman", 18))
        lbl_datos_habitacion.pack(padx=10, pady=10)

        # Mostrar imagen (requiere una imagen llamada 'pokemon.png' en el directorio actual)
        try:
            imagen = Image.open("pokemon.png")
            imagen = imagen.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(imagen)
            lbl_imagen = tk.Label(ventana_datos, image=img)
            lbl_imagen.image = img  # Necesario para evitar que la imagen sea recolectada por el recolector de basura
            lbl_imagen.pack(pady=10)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        # Crear entradas para modificar los datos del entrenador Pokémon
        datos = datos_habitaciones

        lbl_datos_entrenador = tk.Label(ventana_datos, text="Entrenador:", font=("Times New Roman", 16))
        lbl_datos_entrenador.pack(pady=5)
        entry_nombre_entrenador = tk.Entry(ventana_datos, font=("Times New Roman", 16))
        entry_nombre_entrenador.pack(pady=5)
        entry_nombre_entrenador.insert(0, datos["Nombre"])

        lbl_datos_apellido = tk.Label(ventana_datos, text="Apellido:", font=("Times New Roman", 16))
        lbl_datos_apellido.pack(pady=5)
        entry_apellido_entrenador = tk.Entry(ventana_datos, font=("Times New Roman", 16))
        entry_apellido_entrenador.pack(pady=5)
        entry_apellido_entrenador.insert(0, datos["Apellido"])

        lbl_datos_pokemon = tk.Label(ventana_datos, text="Pokémon:", font=("Times New Roman", 16))
        lbl_datos_pokemon.pack(pady=5)
        entry_pokemon = tk.Entry(ventana_datos, font=("Times New Roman", 16))
        entry_pokemon.pack(pady=5)
        entry_pokemon.insert(0, datos["NombrePokemon"])

        lbl_tipos_pokemon = tk.Label(ventana_datos, text="Tipos:", font=("Times New Roman", 16))
        lbl_tipos_pokemon.pack(pady=5)
        entry_tipos_pokemon = tk.Entry(ventana_datos, font=("Times New Roman", 16))
        entry_tipos_pokemon.pack(pady=5)
        entry_tipos_pokemon.insert(0, datos["TipoPokemon"] + ", " + datos["SegundoTipoPokemon"])

        lbl_tiempo_estadia = tk.Label(ventana_datos, text="Tiempo de Estadía:", font=("Times New Roman", 16))
        lbl_tiempo_estadia.pack(pady=5)
        entry_tiempo_estadia = tk.Entry(ventana_datos, font=("Times New Roman", 16))
        entry_tiempo_estadia.pack(pady=5)
        entry_tiempo_estadia.insert(0, datos["TiempoEstadia"])

        lbl_telefono = tk.Label(ventana_datos, text="Número de teléfono:", font=("Times New Roman", 16))
        lbl_telefono.pack(pady=5)
        entry_telefono = tk.Entry(ventana_datos, font=("Times New Roman", 16))
        entry_telefono.pack(pady=5)
        entry_telefono.insert(0, datos["Telefono"])

        btn_guardar = tk.Button(ventana_datos, text="Guardar Cambios", command=lambda: guardar_cambios(entry_nombre_entrenador.get(), entry_apellido_entrenador.get(), entry_pokemon.get(), entry_tipos_pokemon.get(), entry_tiempo_estadia.get(), entry_telefono.get()), font=("Times New Roman", 16))
        btn_guardar.pack(pady=10)

        btn_eliminar = tk.Button(ventana_datos, text="Borrar Habitación", command=lambda: eliminar_habitacion(ventana_datos), font=("Times New Roman", 16))
        btn_eliminar.pack(pady=10)
    else:
        # Mostrar mensaje de habitación vacía
        messagebox.showinfo("Habitación Vacía", f"La habitación {habitacion_seleccionada} está vacía.")

def guardar_cambios(nombre, apellido, pokemon, tipos, tiempo, telefono):
    datos_habitaciones["Nombre"] = nombre
    datos_habitaciones["Apellido"] = apellido
    datos_habitaciones["NombrePokemon"] = pokemon
    tipo_split = tipos.split(", ")
    datos_habitaciones["TipoPokemon"] = tipo_split[0]
    datos_habitaciones["SegundoTipoPokemon"] = tipo_split[1] if len(tipo_split) > 1 else "Ninguno"
    datos_habitaciones["TiempoEstadia"] = tiempo
    datos_habitaciones["Telefono"] = telefono
    # Guardar los cambios en el archivo JSON
    with open('datos.json', 'w') as file:
        json.dump(datos_habitaciones, file, indent=4)
    messagebox.showinfo("Éxito", "Los cambios se han guardado correctamente.")

def eliminar_habitacion(ventana_datos):
    habitacion_eliminar = datos_habitaciones["Habitacion"]
    if habitacion_eliminar in habitaciones_ocupadas:
        habitaciones_ocupadas.remove(habitacion_eliminar)
        # Guardar los cambios en el archivo JSON
        with open('datos.json', 'w') as file:
            json.dump({}, file, indent=4)
        ventana_datos.destroy()
        # Actualizar la visualización de las habitaciones
        mostrar_habitaciones()
    else:
        messagebox.showwarning("Error", f"La habitación {habitacion_eliminar} no está ocupada.")

def mostrar_habitaciones():
    # Limpiar todos los widgets dentro de frame_principal
    for widget in frame_principal.winfo_children():
        widget.destroy()

    # Crear una matriz de botones para las habitaciones
    for fila in range(5):
        for columna in range(5):
            habitacion = f"{chr(65+fila)}{columna+1}"
            # Determinar el estado de la habitación (ocupada o vacía)
            estado_habitacion = "green" if habitacion in habitaciones_ocupadas else "white"
            
            # Crear botón para cada habitación
            btn_habitacion = tk.Button(frame_principal, text=habitacion, bg=estado_habitacion,
                                    command=lambda h=habitacion: mostrar_datos_habitacion(h), width=10, height=3,
                                    font=("Times New Roman", 14))
            btn_habitacion.grid(row=fila, column=columna, padx=10, pady=10)

# Crear la ventana principal
ventana_admin = tk.Tk()
ventana_admin.title("Panel de Administrador")
ventana_admin.geometry("800x600")

# Centrar la ventana en la pantalla
ancho_ventana = ventana_admin.winfo_reqwidth()
alto_ventana = ventana_admin.winfo_reqheight()
posicion_x = int(ventana_admin.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_y = int(ventana_admin.winfo_screenheight() / 2 - alto_ventana / 2)
ventana_admin.geometry(f"800x600+{posicion_x}+{posicion_y}")

# Frame principal para organizar widgets
frame_principal = tk.Frame(ventana_admin)
frame_principal.pack(padx=20, pady=20)

# Mostrar las habitaciones al inicio
mostrar_habitaciones()

# Ejecutar el bucle principal de la ventana
ventana_admin.mainloop()