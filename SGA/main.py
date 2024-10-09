import tkinter
from tkinter import *
from PIL import ImageTk

#INSTALR PILLOW USANDO "PIP INSTALL PILLOW"

janela = Tk()
janela.title("Sistema de gerenciamento de alunos")
janela.config(bg="#99d8ea")
janela.resizable(False, False)
img = PhotoImage(file=r"SGA\icon\icon1.png")
janela.iconphoto(False, img)
janela.pack_propagate(False)

#centralizar app
x_app = 400
y_app = 450
x_tela = janela.winfo_screenwidth()
y_tela = janela.winfo_screenheight()

x = (x_tela / 2) - (x_app / 2)
y = (y_tela / 2) - (y_app / 2)

janela.geometry(f"{x_app}x{y_app}+{int(x)}+{int(y)}")

#widget
logo_img = ImageTk.PhotoImage(file=r"SGA/icon/icon2.png")
logo_widget = tkinter.Label(janela, image=logo_img, bg="#99d8ea")
logo_widget.image = logo_img
logo_widget.pack()

#botões
b_1 = Button(janela,
             text="Consultar alunos",
             cursor="hand2",
             width=20,
             height=2,
             font='Ivy 13 bold',
             relief=FLAT)
b_1.place(x=100, y=220)
b_2 = Button(janela,
             text="Alterar inormações",
             cursor="hand2",
             width=20,
             height=2,
             font='Ivy 13 bold',
             relief=FLAT)
b_2.place(x=100, y=300)

janela.mainloop()