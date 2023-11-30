import tkinter as tk
from tkinter import ttk
from config import COLOR_CUERPO_PRINCIPAL

class FormularioSitioImporteDesign():

    def __init__(self, panel_principal):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Formulario de Importación")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Campos del formulario
        self.labelNombre = tk.Label(panel_principal, text="Nombre:")
        self.entryNombre = ttk.Entry(panel_principal)

        self.labelCantidad = tk.Label(panel_principal, text="Cantidad:")
        self.entryCantidad = ttk.Entry(panel_principal)

        self.labelFecha = tk.Label(panel_principal, text="Fecha:")
        self.entryFecha = ttk.Entry(panel_principal)

        self.labelLugar = tk.Label(panel_principal, text="Lugar:")
        self.entryLugar = ttk.Entry(panel_principal)

        # Posicionando los campos en la ventana
        self.labelNombre.pack(pady=10)
        self.entryNombre.pack(pady=10)

        self.labelCantidad.pack(pady=10)
        self.entryCantidad.pack(pady=10)

        self.labelFecha.pack(pady=10)
        self.entryFecha.pack(pady=10)

        self.labelLugar.pack(pady=10)
        self.entryLugar.pack(pady=10)

        # Botón de registro
        self.botonRegistrar = ttk.Button(panel_principal, text="Registrar", command=self.registrar)
        self.botonRegistrar.pack(pady=20)

        # Segundo Label con la imagen
        self.label_imagen = tk.Label(self.barra_inferior, image=logo)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_imagen.config(fg="#fff", font=("Roboto", 10), bg=COLOR_CUERPO_PRINCIPAL)

    def registrar(self):
        # Función a ejecutar al hacer clic en el botón de registro
        # Puedes obtener los valores de los campos con self.entryNombre.get(), self.entryCantidad.get(), etc.
        print("Registro realizado:")
        print("Nombre:", self.entryNombre.get())
        print("Cantidad:", self.entryCantidad.get())
        print("Fecha:", self.entryFecha.get())
        print("Lugar:", self.entryLugar.get())
        print("Datos Guardados")
