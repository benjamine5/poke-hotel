import tkinter as tk
from tkinter import messagebox
import json
import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageTk

# Función para cargar el valor del JSON
def cargar_valor_json():
    try:
        with open("Actividades_data.json", "r") as f:
            data = json.load(f)
            return data.get("actividades", 0)
    except FileNotFoundError:
        return 0

# Función para validar la fecha de expiración de la tarjeta
def is_valid_exp_date(month, year):
    try:
        exp_month = int(month)
        exp_year = int("20" + year)
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        if exp_year < current_year or exp_year > 2032:
            return False
        if exp_year == current_year and exp_month < current_month:
            return False
        if exp_month < 1 or exp_month > 12:
            return False
        return True
    except ValueError:
        return False

# Función para validar el número de tarjeta utilizando el algoritmo de Luhn
def is_valid_card_number(card_number):
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    return luhn_checksum(card_number) == 0

# Funciones de validación para campos de entrada
def validate_card_number(P):
    return P.isdigit() and len(P) <= 16 or P == ""

def validate_date(P):
    return P.isdigit() and len(P) <= 2 or P == ""

def validate_cvv(P):
    return P.isdigit() and len(P) <= 4 or P == ""

def validate_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

# Función para enviar el comprobante de pago por correo electrónico
def enviar_comprobante_pago(destinatario, nombre, monto):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "trabajos.felipe2@gmail.com"
    smtp_password = "lnqd apvt hjrm igvv"

    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_user
    mensaje['To'] = destinatario
    mensaje['Subject'] = "Comprobante de Pago"

    cuerpo = f"""
    <html>
    <body>
        <p>Estimado/a {nombre},</p>
        <p>Nos complace informarle que hemos recibido su pago exitosamente.</p>
        <p>Detalles de la transacción:</p>
        <ul>
            <li>Monto: <strong>{monto}</strong></li>
            <li>Fecha: {datetime.datetime.now().strftime("%d/%m/%Y")}</li>
            <li>Hora: {datetime.datetime.now().strftime("%H:%M:%S")}</li>
        </ul>
        <p>Gracias por confiar en nosotros. Esperamos que disfrute de su estadía en Poke Hotel.</p>
        <p>Saludos cordiales,<br>El equipo de Poke Hotel</p>
    </body>
    </html>
    """
    cuerpo = cuerpo.encode('utf-8')  # Codificar el cuerpo como UTF-8

    mensaje.attach(MIMEText(cuerpo, 'html', 'utf-8'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, destinatario, mensaje.as_string())
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Función para obtener el tiempo de estadía desde el JSON
def obtener_tiempo_estadia(archivo_json):
    try:
        with open(archivo_json, "r") as f:
            data = json.load(f)
            return int(data.get("TiempoEstadia", 1))  # Valor predeterminado 1 si no se encuentra "TiempoEstadia"
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_json} no se encontró.")
        return 1
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return 1

# Función para procesar el pago
def process_payment():
    # Obtener los datos ingresados por el usuario
    name = ename.get()
    email = eemail.get()
    card_number = etargeta.get()
    exp_month = efechaexp.get()
    exp_year = efechaexp1.get()
    ccv = eccv.get()

    # Obtener el monto total de actividades desde el JSON
    monto_actividades = cargar_valor_json()
    
    # Obtener el tiempo de estadía desde el JSON
    tiempo_estadia = obtener_tiempo_estadia("datos.json")
    
    # Calcular el monto total
    monto_total = monto_actividades + (100000 * tiempo_estadia)

    # Validar los campos ingresados por el usuario
    if not name:
        messagebox.showerror("Error", "Nombre no puede estar vacío")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Correo no válido")
        return

    if not is_valid_exp_date(exp_month, exp_year):
        messagebox.showerror("Error", "Fecha de expiración no válida")
        return

    if not is_valid_card_number(card_number):
        messagebox.showerror("Error", "Número de tarjeta no válido")
        return

    messagebox.showinfo("Aceptada", "Su tarjeta ha sido aceptada")

    # Enviar el comprobante de pago con el monto total ajustado
    enviar_comprobante_pago(email, name, monto_total)

# Configuración de la interfaz gráfica
raiz = tk.Tk()
raiz.geometry("800x600")
raiz.title("Pago hotel")
raiz.config(bd=25, relief="sunken")

# Cargar imagen
ruta_imagen = "pokemon/pa.png"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((300, 280), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(raiz, image=imagen_tk)
label_imagen.place(x=590, y=410, anchor=tk.CENTER)

# Widgets de entrada y etiquetas
lname = tk.Label(raiz, text="Nombre:", font=("Times New Roman", 20))
lname.place(x=150, y=80, anchor=tk.CENTER)

ename = tk.Entry(raiz, font=("Times New Roman", 17), width=30)
ename.place(x=450, y=80, anchor=tk.CENTER)

lemail = tk.Label(raiz, text="Correo:", font=("Times New Roman", 20))
lemail.place(x=150, y=130, anchor=tk.CENTER)

eemail = tk.Entry(raiz, font=("Times New Roman", 17), width=30)
eemail.place(x=450, y=130, anchor=tk.CENTER)

ltargeta = tk.Label(raiz, text="Número de Tarjeta:", font=("Times New Roman", 20))
ltargeta.place(x=200, y=180, anchor=tk.CENTER)

etargeta = tk.Entry(raiz, font=("Times New Roman", 20), width=16, validate="key")
etargeta['validatecommand'] = (etargeta.register(validate_card_number), '%P')
etargeta.place(x=470, y=180, anchor=tk.CENTER)

lfechaexp = tk.Label(raiz, text="Fecha de Expiración:", font=("Times New Roman", 20))
lfechaexp.place(x=210, y=240, anchor=tk.CENTER)

efechaexp = tk.Entry(raiz, font=("Times New Roman", 20), width=2, validate="key")
efechaexp['validatecommand'] = (efechaexp.register(validate_date), '%P')
efechaexp.place(x=400, y=240, anchor=tk.CENTER)

slash = tk.Label(raiz, text="/", font=("Times New Roman", 40))
slash.place(x=430, y=240, anchor=tk.CENTER)

efechaexp1 = tk.Entry(raiz, font=("Times New Roman", 20), width=2, validate="key")
efechaexp1['validatecommand'] = (efechaexp1.register(validate_date), '%P')
efechaexp1.place(x=465, y=240, anchor=tk.CENTER)

lccv = tk.Label(raiz, text="CCV:", font=("Times New Roman", 20))
lccv.place(x=190, y=300, anchor=tk.CENTER)

eccv = tk.Entry(raiz, show="*", font=("Times New Roman", 20), width=4, validate="key")
eccv['validatecommand'] = (eccv.register(validate_cvv), '%P')
eccv.place(x=430, y=300, anchor=tk.CENTER)

# Botón para procesar el pago
bsubmit = tk.Button(raiz, text="Pagar", font=("Times New Roman", 20), command=process_payment)
bsubmit.place(x=400, y=380, anchor=tk.CENTER)

raiz.mainloop()
