import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from PIL import Image, ImageTk

class MasterPanel:
    def __init__(self):
        self.ventana= tk.Tk()
        self.ventana.title("Empresa de Importaciones")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{w}x{h}+0+0")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap('./iconos/logo.ico')

        imagen=tk.Label(self.ventana,image=ImageTk.PhotoImage(Image.open("iconos/login.png")), bg='#3a7ff6')
        imagen.place(x=0,y=0,relwidth=1,relheight=1)
        self.ventana.mainloop() 