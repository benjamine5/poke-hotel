import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import stripe  #instalar con "pip install stripe"
import datetime
import subprocess

# Configuración de Stripe
stripe.api_key = 'sk_test_tu_clave_secreta_de_stripe'

def is_valid_exp_date(month, year):
    """Verifica si la fecha de expiración es válida"""
    try:
        exp_month = int(month)
        exp_year = int("20" + year)  # Convertir año a formato YYYY
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        if exp_year < current_year or exp_year > 2028:
            return False
        if exp_year == current_year and exp_month < current_month:
            return False
        if exp_month < 1 or exp_month > 12:
            return False
        return True
    except ValueError:
        return False

def is_valid_card_number(card_number):
    """Verifica si los primeros cuatro dígitos de la tarjeta son válidos"""
    valid_prefixes = ['4', '5', '6', '37']  # Ejemplos de prefijos válidos para Visa, MasterCard, Discover, Amex
    return any(card_number.startswith(prefix) for prefix in valid_prefixes)

def validate_card_number(P):
    """Valida que la entrada del número de tarjeta sea numérica y tenga hasta 16 dígitos"""
    return P.isdigit() and len(P) <= 16 or P == ""

def validate_date(P):
    """Valida que la entrada de la fecha de expiración sea numérica y tenga hasta 2 dígitos"""
    return P.isdigit() and len(P) <= 2 or P == ""

def validate_cvv(P):
    """Valida que la entrada del CVV sea numérica y tenga hasta 4 dígitos"""
    return P.isdigit() and len(P) <= 4 or P == ""

def process_payment():
    # Recopilar información del formulario
    amount = 10000  # Ejemplo: $100.00 en centavos
    card_number = etargeta.get()
    exp_month = efechaexp.get()
    exp_year = efechaexp1.get()
    ccv = eccv.get()

    # Validar fecha de expiración
    if not is_valid_exp_date(exp_month, exp_year):
        messagebox.showerror("Error", "Fecha de expiración no válida")
        return

    # Validar número de tarjeta
    if not is_valid_card_number(card_number):
        messagebox.showerror("Error", "Número de tarjeta no válido")
        return

    # Crear un diccionario con los datos de la tarjeta
    card_data = {
        'number': card_number,
        'exp_month': exp_month,
        'exp_year': exp_year,
        'cvc': ccv
    }

    try:
        # Simular el cargo a través de Stripe
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Ejemplo de pago',
            source={
                'object': 'card',
                'number': card_data['number'],
                'exp_month': card_data['exp_month'],
                'exp_year': card_data['exp_year'],
                'cvc': card_data['cvc']
            }  # Pasar los datos de la tarjeta como fuente
        )
        messagebox.showinfo("Éxito", "Pago procesado correctamente")
    except stripe.error.StripeError:
        messagebox.showerror("Error", "Error al procesar el pago")

raiz = tk.Tk()

raiz.geometry("800x600")
raiz.title("Pago Hotel")
raiz.config(bd=25)
raiz.config(relief="sunken")
raiz.iconbitmap("pokemon.ico")

# Cargar la imagen
image = PhotoImage(file="pngegg.png")

# Crear un widget Label para la imagen
label_image = tk.Label(raiz, image=image)
label_image.place(x=550, y=420, anchor=tk.CENTER)

ltargeta = tk.Label(raiz, text="Número de Tarjeta:", font=("Times New Roman", 20))
ltargeta.place(x=200, y=160, anchor=tk.CENTER)

etargeta = tk.Entry(raiz, font=("Times New Roman", 20), validate="key")
etargeta['validatecommand'] = (etargeta.register(validate_card_number), '%P')
etargeta.place(x=470, y=160, anchor=tk.CENTER)

lfechaexp = tk.Label(raiz, text="Fecha de Expiración:", font=("Times New Roman", 20))
lfechaexp.place(x=210, y=220, anchor=tk.CENTER)

efechaexp = tk.Entry(raiz, font=("Times New Roman", 20), width=2, validate="key")
efechaexp['validatecommand'] = (efechaexp.register(validate_date), '%P')
efechaexp.place(x=400, y=220, anchor=tk.CENTER)

slash = tk.Label(raiz, text="/", font=("Times New Roman", 40))
slash.place(x=430, y=220, anchor=tk.CENTER)

efechaexp1 = tk.Entry(raiz, font=("Times New Roman", 20), width=2, validate="key")
efechaexp1['validatecommand'] = (efechaexp1.register(validate_date), '%P')
efechaexp1.place(x=465, y=220, anchor=tk.CENTER)

lccv = tk.Label(raiz, text="CCV:", font=("Times New Roman", 20))
lccv.place(x=123, y=280, anchor=tk.CENTER)

eccv = tk.Entry(raiz, show="*", font=("Times New Roman", 20), width=3, validate="key")
eccv['validatecommand'] = (eccv.register(validate_cvv), '%P')
eccv.place(x=430, y=280, anchor=tk.CENTER)

bpago = tk.Button(raiz, text="Pagar", font=("Times New Roman", 25), command=process_payment)
bpago.place(x=300, y=380, anchor=tk.CENTER)


raiz.mainloop()
