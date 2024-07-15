import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import re
import json
import subprocess

class SeatSelection(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Habitaciones")
        self.geometry("800x600")
        self.resizable(True, True)
        self.config(bd=25, relief="groove")
        self.iconbitmap("pokemon/hotel.ico")

        self.selected_seats = []
        self.create_widgets()

    def create_widgets(self):
        Frame = tk.Frame(self)
        Frame.pack()
        label = tk.Label(Frame, text="Habitaciones:", font=("Times New Roman", 20))
        label.grid(row=0, column=0, columnspan=5)

        self.seat_buttons = []
        seats = ['A1', 'A2', 'A3', 'A4', 'A5',
                'B1', 'B2', 'B3', 'B4', 'B5',
                'C1', 'C2', 'C3', 'C4', 'C5',
                'D1', 'D2', 'D3', 'D4', 'D5',
                'F1', 'F2', 'F3', 'F4', 'F5']

        row = 1
        col = 0
        for i, seat in enumerate(seats):
            button = tk.Button(Frame, text=seat, width=16, height=5, command=lambda i=i: self.on_seat_click(i))
            button.grid(row=row, column=col)
            self.seat_buttons.append(button)
            col += 1
            if col > 4:
                col = 0
                row += 1

        self.button = tk.Button(Frame, text="Siguiente", command=self.Registro, font=("Times New Roman", 21))
        self.button.grid(row=row+1, column=0, columnspan=5)

    def Registro(self):
        if not self.selected_seats:
            messagebox.showinfo("Error", "Debe seleccionar al menos una habitación.")
        else:
            seat = self.selected_seats[0]
            self.destroy()  # Cerrar la ventana actual
            RegistroApp(seat)  # Abrir la ventana de registro

    def on_seat_click(self, index):
        seat = self.seat_buttons[index]
        if seat.cget('bg') == 'SystemButtonFace':
            if len(self.selected_seats) < 1:
                seat.config(bg='green')
                self.selected_seats.append(seat.cget('text'))
            else:
                messagebox.showinfo("Error", "No puede elegir más de 1 habitación.")
        else:
            seat.config(bg='SystemButtonFace')
            self.selected_seats.remove(seat.cget('text'))


class RegistroApp(tk.Tk):
    
    def __init__(self, seat):
        super().__init__()
        self.title("Registro")
        self.geometry("800x600")
        self.config(bg="black")
        self.iconbitmap("pokemon/hotel.ico")

        self.seat = seat
        self.create_widgets()

    def create_widgets(self):
        Frame1 = tk.Frame(self)
        Frame1.pack(fill="both", expand=True)
        Frame1.config(width="800", height="600", bd=30, relief="sunken")

        Imagen1 = PhotoImage(file="pokemon/Pokemon.png")
        label2 = tk.Label(Frame1, image=Imagen1)
        label2.image = Imagen1  # Keep a reference
        label2.place(x=450, y=100)

        def solo_numeros(P):
            return P.isdigit() or P == ""

        validate_command = self.register(solo_numeros)

        self.CuadroNombre = tk.Entry(Frame1)
        self.CuadroNombre.grid(row=1, column=1, padx=10, pady=10)
        self.CuadroNombre.config(fg="black", justify="center")
        ContLabel = tk.Label(Frame1, text="Nombre entrenador:", font=("Times New Roman", 14))
        ContLabel.grid(row=1, column=0, padx=10, pady=10)

        self.CuadroApellido = tk.Entry(Frame1)
        self.CuadroApellido.grid(row=1, column=3, padx=10, pady=10)
        self.CuadroApellido.config(fg="black", justify="center")
        ApellidoLabel = tk.Label(Frame1, text="Apellido entrenador:", font=("Times New Roman", 14))
        ApellidoLabel.grid(row=1, column=2, padx=10, pady=10)

        self.CuadroRut = tk.Entry(Frame1)
        self.CuadroRut.grid(row=2, column=1, padx=10, pady=10)
        self.CuadroRut.config(fg="black", justify="center")
        RutLabel = tk.Label(Frame1, text="Rut entrenador:", font=("Times New Roman", 14))
        RutLabel.grid(row=2, column=0, padx=10, pady=10)

        self.CuadroTelefono = tk.Entry(Frame1, validate="key", validatecommand=(validate_command, '%P'))
        self.CuadroTelefono.grid(row=2, column=3, padx=10, pady=10)
        self.CuadroTelefono.config(fg="black", justify="center")
        TelefonoLabel = tk.Label(Frame1, text="Teléfono entrenador:", font=("Times New Roman", 14))
        TelefonoLabel.grid(row=2, column=2, padx=10, pady=10)

        self.CuadroNombrePokemon = tk.Entry(Frame1)
        self.CuadroNombrePokemon.grid(row=3, column=1, padx=10, pady=10)
        self.CuadroNombrePokemon.config(fg="black", justify="center")
        NombrePokemonLabel = tk.Label(Frame1, text="Nombre del pokémon:", font=("Times New Roman", 14))
        NombrePokemonLabel.grid(row=3, column=0, padx=10, pady=10)

        TipoPokemonLabel = tk.Label(Frame1, text="Tipo del pokémon:", font=("Times New Roman", 14))
        TipoPokemonLabel.grid(row=4, column=0, padx=10, pady=10)

        self.valor = tk.StringVar()
        self.valor.set("Normal")

        tipos_pokemon = [
            ("Normal", "pokemon/normal.png"),
            ("Lucha", "pokemon/lucha.png"),
            ("Volador", "pokemon/volador.png"),
            ("Veneno", "pokemon/veneno.png"),
            ("Tierra", "pokemon/tierra.png"),
            ("Roca", "pokemon/roca.png"),
            ("Bicho", "pokemon/bicho.png"),
            ("Fantasma", "pokemon/fantasma.png"),
            ("Acero", "pokemon/acero.png"),
            ("Fuego", "pokemon/fuego.png"),
            ("Agua", "pokemon/agua.png"),
            ("Planta", "pokemon/planta.png"),
            ("Eléctrico", "pokemon/electrico.png"),
            ("Psíquico", "pokemon/psiquico.png"),
            ("Hielo", "pokemon/hielo.png"),
            ("Dragón", "pokemon/dragon.png"),
            ("Siniestro", "pokemon/siniestro.png"),
            ("Hada", "pokemon/hada.png")
        ]

        imagenes_tipos = {}

        menu_tipos = tk.Menu(self, tearoff=0)
        for tipo, imagen in tipos_pokemon:
            img = Image.open(imagen).resize((24, 24), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            imagenes_tipos[tipo] = img
            menu_tipos.add_command(label=tipo, image=img, compound="left", command=lambda t=tipo: self.valor.set(t))

        def mostrar_menu_tipos(event):
            menu_tipos.tk_popup(event.x_root, event.y_root)

        boton_tipo = tk.Button(Frame1, textvariable=self.valor, width=20)
        boton_tipo.grid(row=4, column=1, padx=10, pady=10)
        boton_tipo.bind("<Button-1>", mostrar_menu_tipos)

        SegundoTipoPokemonLabel = tk.Label(Frame1, text="Segundo tipo del pokémon:", font=("Times New Roman", 14))
        SegundoTipoPokemonLabel.grid(row=5, column=0, padx=10, pady=10)

        self.valor2 = tk.StringVar()
        self.valor2.set("Ninguno")

        menu_tipos2 = tk.Menu(self, tearoff=0)
        for tipo, imagen in tipos_pokemon:
            img = Image.open(imagen).resize((24, 24), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            imagenes_tipos[tipo + "_2"] = img
            menu_tipos2.add_command(label=tipo, image=img, compound="left", command=lambda t=tipo: self.valor2.set(t))
        menu_tipos2.add_command(label="Ninguno", command=lambda: self.valor2.set("Ninguno"))

        def mostrar_menu_tipos2(event):
            menu_tipos2.tk_popup(event.x_root, event.y_root)

        boton_tipo2 = tk.Button(Frame1, textvariable=self.valor2, width=20)
        boton_tipo2.grid(row=5, column=1, padx=10, pady=10)
        boton_tipo2.bind("<Button-1>", mostrar_menu_tipos2)

        self.CuadroTiempoEstadia = tk.Entry(Frame1, validate="key", validatecommand=(validate_command, '%P'))
        self.CuadroTiempoEstadia.grid(row=7, column=1, padx=10, pady=10)
        self.CuadroTiempoEstadia.config(fg="black", justify="center")
        TiempoEstadiaLabel = tk.Label(Frame1, text="Días de estadía del pokémon:", font=("Times New Roman", 14))
        TiempoEstadiaLabel.grid(row=7, column=0, padx=10, pady=10)

        botonRegister = tk.Button(self, text="Registrarse", command=self.guardar_datos, font=("Times New Roman", 25), fg="Black")
        botonRegister.place(x=300, y=400)

            
    def guardar_datos(self):
        datos = {
            "Nombre": self.CuadroNombre.get(),
            "Apellido": self.CuadroApellido.get(),
            "Rut": self.CuadroRut.get(),
            "Telefono": self.CuadroTelefono.get(),
            "NombrePokemon": self.CuadroNombrePokemon.get(),
            "TipoPokemon": self.valor.get(),
            "SegundoTipoPokemon": self.valor2.get(),
            "TiempoEstadia": self.CuadroTiempoEstadia.get(),
            "Habitacion": self.seat
        }

        if not self.validar_rut(datos["Rut"]):
            messagebox.showinfo("Error", "El RUT ingresado no es válido.XX.XXX.XXX-X")
            return

        if not self.validar_telefono(datos["Telefono"]):
            messagebox.showinfo("Error", "El teléfono ingresado no es válido.")
            return

        with open("datos.json", "w") as file:
            json.dump(datos, file, indent=4)

        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        subprocess.Popen(["python","interfasActividades.py"])
    def validar_rut(self, rut):
        return re.match(r"^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$", rut)

    def validar_telefono(self, telefono):
        return telefono.isdigit() and len(telefono) == 8

  
    
 
if __name__ == "__main__":
    app = SeatSelection()
    app.mainloop()
