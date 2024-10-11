import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
#INSTALR PILLOW USANDO "PIP INSTALL PILLOW"

main_window = ttk.Window(themename = 'superhero')
main_window.title("Sistema de gerenciamento de alunos")
img = ImageTk.PhotoImage(file=r"SGA\icon\icon.png")
main_window.iconphoto(False, img)

#COLOCA A PRIMEIRA TELA INTEIRA EM UM UNICO FRAME PARA FACILICAR A MUDANDA DE "JANELA" POSTERIORMENTE
start = ttk.Frame(main_window)

#GRID
start.columnconfigure((0,1),  weight= 1, uniform= 'a')
start.rowconfigure((0), weight= 1)

#CENTRALIZE APP ON THE SCREEN
x_app = 550
y_app = 350
x_screen = main_window.winfo_screenwidth()
y_screen = main_window.winfo_screenheight()

x = (x_screen / 2) - (x_app / 2)
y = (y_screen / 2) - (y_app / 2)

main_window.geometry(f"{x_app}x{y_app}+{int(x)}+{int(y)}")

#LOGO
logo = Image.open('SGA/icon/logo.png')
logo_img = ImageTk.PhotoImage(logo)
logo_place = tk.Label(start, image=logo_img)
logo_place.image = logo_img
logo_place.grid(column=0)

#BUTTONS
button_frame = ttk.Frame(start)
b1 = ttk.Button(button_frame, text= 'Consultar alunos', width= 30)
b1.pack(pady= 10)
b2 = ttk.Button(button_frame, text= 'Alterar informações', width= 30)
b2.pack(pady= 10)
button_frame.grid(column= 1, row=0, sticky= 'ew')

start.place(anchor='c', relx=.5, rely=.5)

main_window.mainloop()