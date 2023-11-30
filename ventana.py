#importando las librerías
import tkinter as tk
from tkinter import ttk
#creando la ventana
main=tk.Tk()

#titulo de la ventana
main.title("Empresa de importaciones")

#Información de las dimensiones de la ventana
width=720
height=600
#obteniendo ancho y alto de la pantalla usada
wwidth=main.winfo_screenwidth()
wheight=main.winfo_screenheight()
#calculando el centro de la pantalla
center_x=int(wwidth/2-width/2)
center_y=int(wheight/2-height/2)
#estableciendo la geometría de la pantalla (los valores antes calculados) (anchoventanaxaltoventana+espacioenx+espacioeny)
main.geometry(f"{width}x{height}+{center_x}+{center_y}")

#añadiendo el ícono del logo a la ventana
main.iconbitmap('./iconos/logo.png')

#Creando el botón de login
boton=ttk.Button(
    #ventana en la que trabajará
    main,
    #imagen en el botón
    image=tk.PhotoImage(file='./iconos/login.png'),
    #texto
    text="Ingresar",
    command=lambda: main.quit()
)

boton.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

main.mainloop()