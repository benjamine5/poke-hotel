import tkinter as tk
import subprocess
from tkinter import messagebox

class SeatSelection(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Habitaciones")
        self.geometry("800x600")
        self.resizable(True, True)
        self.config(bd=25, relief="groove")
        raiz.iconbitmap("pokemon.ico")

        self.selected_seats = []

        self.create_widgets()

    def create_widgets(self):
        Frame=tk.Frame(self)
        Frame.pack()
        label = tk.Label(Frame, text="Habitaciones Tomadas:", font=("Times New Romans", 20))
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
        
        # Add the button to the same window
        self.button = tk.Button(Frame, text="Siguiente", command=self.Registro, font=("Times New Romans", 21))
        self.button.grid(row=row+1, column=0, columnspan=5)
        
    def Registro(self):
        subprocess.Popen(["python","registro.py"])

    def on_seat_click(self, index):
        seat = self.seat_buttons[index]
        if seat.cget('bg') == 'SystemButtonFace':
            seat.config(bg='green')
            self.selected_seats.append(seat.cget('text'))
        else:
            seat.config(bg='SystemButtonFace')
            self.selected_seats.remove(seat.cget('text'))

        if len(self.selected_seats) > 0:
            messagebox.showinfo("Habitaciones_tomadas", ", ".join(self.selected_seats))
        else:
            messagebox.showinfo("Habitaciones_tomadas", "No hay habitaciones tomadas")

    def on_button_click(self):
        subprocess.Popen(["python","registro.py"])

if __name__ == "__main__":
    app = SeatSelection()
    app.mainloop()
