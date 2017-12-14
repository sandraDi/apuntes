#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from json import dump
from json import loads


def datos():
    datosPersonales = {}
    datosPersonales["nombre"] = sd.askstring("nombre", "Ingrese su nombre:")
    datosPersonales["apellido"] = sd.askstring("apellido", "Ingrese su apellido:")
    datosPersonales["direccion"] = sd.askstring("direccion", "Ingrese su dirección:")
    datosPersonales["telefono"] = sd.askstring("telefono", "Ingrese su teléfono:")
             
    saveData(datosPersonales)


def saveData(datosPersonales):
   with open("datosPersonales.json", "w") as sandrita:
       dump(datosPersonales, sandrita)

def mostrarDatos():
    datos = loads(open("datosPersonales.json").read())
                                                      
    namelabel = tk.Label(mainForm, text = "Nombre: " + datos["nombre"])
    namelabel.place(x=10, y=50)
    surnamelabel = tk.Label(mainForm, text = "Apellido: " + datos["apellido"])
    surnamelabel.place(x=10, y=70)
    addresslabel = tk.Label(mainForm, text = "Dirección: " + datos["direccion"])
    addresslabel.place(x=10, y=90)
    phonelabel = tk.Label(mainForm, text = "Teléfono: " + datos["telefono"])
    phonelabel.place(x=10, y=110)

mainForm = tk.Tk()
mainForm.geometry("400x200")
mainForm.title("Datos Personales")

mainMenu = tk.Menu(mainForm)

fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit)
mainMenu.add_cascade(label = "Archivo", menu = fileMenu)

personMenu = tk.Menu(mainMenu, tearoff = 0)
personMenu.add_command(label = "Cargar datos...", command = datos)
personMenu.add_separator()
personMenu.add_command(label = "Mostrar datos...", command = mostrarDatos)
mainMenu.add_cascade(label = "Persona", menu = personMenu)

mainForm.config(menu = mainMenu)

mainForm.mainloop()

