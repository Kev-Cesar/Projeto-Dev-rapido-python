import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
#INSTALR PILLOW USANDO "PIP INSTALL PILLOW"

#FUNÇÕES

def clear_widgets(main_frame):
    #LIMPA OS WIDGETS DO FRAME PRINCIPAL EM EXBIÇÃO PARA EXIBIR O PROXIMO FRAME
    for frame in main_frame.winfo_children():
        frame.destroy()

def load_start():

    clear_widgets(consult)#USAR O FRAME A SER DESTRUIDO COMO PARAMETRO DA FUNÇÃO TODA VEZ QUE FOR CHAMADA
    start.tkraise()
    start.columnconfigure((0,1),  weight= 1, uniform= 'a')
    start.rowconfigure((0), weight= 1)

    #LOGO
    logo = Image.open('SGA/icon/logo.png')
    logo_img = ImageTk.PhotoImage(logo)
    logo_place = tk.Label(start, image=logo_img)
    logo_place.image = logo_img
    logo_place.grid(column=0)

    #BOTÕES
    button_frame = ttk.Frame(start)
    b1 = ttk.Button(button_frame, text= 'Consultar alunos', width= 30, command=lambda:load_consult())
    b1.pack(pady= 10)
    b2 = ttk.Button(button_frame, text= 'Alterar informações', width= 30)
    b2.pack(pady= 10)
    button_frame.grid(column= 1, row=0, sticky= 'ew')

    start.place(anchor='center', relx=.5, rely=.5)

def load_consult():
	
    clear_widgets(start)
    consult.tkraise()
    consult.columnconfigure((0,1),  weight= 1, uniform= 'a')
    consult.rowconfigure((0), weight= 1)

    #BOTÕES
    button_frame = ttk.Frame(consult)
    b1 = ttk.Button(button_frame, text= 'Voltar', width=10, command=load_start)
    b1.pack(pady= 10)
    button_frame.grid(column=0, row=0, sticky='nsew')

    consult.place(anchor='center', relx=.5, rely=.5)

main_window = ttk.Window(themename = 'superhero')
main_window.title("Sistema de gerenciamento de alunos")
img = ImageTk.PhotoImage(file=r"SGA\icon\icon.png")
main_window.iconphoto(False, img)
#CENTRALIZAR APP NA TELA
x_app = 550
y_app = 350
x_screen = main_window.winfo_screenwidth()
y_screen = main_window.winfo_screenheight()
x = (x_screen / 2) - (x_app / 2)
y = (y_screen / 2) - (y_app / 2)
main_window.geometry(f"{x_app}x{y_app}+{int(x)}+{int(y)}")

#COLOCA A PRIMEIRA TELA INTEIRA EM UM UNICO FRAME PARA FACILICAR A MUDANDA DE "JANELA" POSTERIORMENTE
start = ttk.Frame(main_window)
consult = ttk.Frame(main_window)

for main_frame in (start, consult):   #COMPACTA OS FRAMES EM UMA UNICA VARIAVEL PARA FACILITAR A LIMPEZA USANDO A FUNÇÃO clear_widgets
	main_frame.grid(column=0, row=0, sticky='nsew')

load_start()

main_window.mainloop()