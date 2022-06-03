#PROYECTOS PROGRAMADOS - PRIMER SEMESTRE 2022
#PROGRAMA 3 - Parqueo
#ITCR - Escuela de Computación- Taller de Programación(IC-1803)
#Profesor: William Mata Rodríguez
#Estudiante: Dominic José Casares Aguirre C.2022085016
#Fecha: 21/6/2022

###############
#   MÓDULOS   #
###############
from email import message
import tkinter as tk
import pickle
import os
from tkinter import *
from tkinter import messagebox
from datetime import datetime
#########################
# VARIABLES IMPORTANTES #
#########################
#############
#  COLORES  #
#############
fondo = "#161622"
########################
# FUNCIONES AUXILIARES #
########################
#función auxiliar para mostrar un mensaje de información
def showmensaje(titulo, mensaje):
	messagebox.showinfo(titulo, mensaje)

#función auxiliar para mostrar un error
def showerror(titulo,mensaje):
    messagebox.showerror(titulo,mensaje)

#función para salir de la ventana
def salir():
    validate = messagebox.askokcancel("Salir","¿Está seguro que desea salir?")
    if validate:
        window_main.destroy()

#funcion para volver a la ventana anterior
def volvermain(ventana):
    ventana.destroy()
    window_main.state("normal")
    window_main.attributes('-topmost', True)
#########################
# FUNCIONES PRINCIPALES #
#########################
#función que despliega el manual de usuario
def ayuda():
    path =  "manual_de_usuario.docx"
    os.startfile(path)

#función de la configuración
def configuracion():
    window_main.state('withdrawn')
    window_configuracion = tk.Toplevel(window_main)
    window_configuracion.title('Configuración')
    # window_configuracion.geometry("800x500+500+100")
    window_configuracion.resizable(False,False)

    ###
    lbl_espaciosparqueo = tk.Label(window_configuracion,text="Cantidad de Espacios en el Parqueo:",font = ("Helvetica",15))
    lbl_espaciosparqueo.grid(row = 1,column = 1)
    ent_espaciosparqueo = tk.Entry(window_configuracion)
    ent_espaciosparqueo.grid(row= 1,column = 4)
    ###
    lbl_preciohora = tk.Label(window_configuracion,text="Precio por Hora:",font = ("Helvetica",15))
    lbl_preciohora.grid(row = 2,column = 1)
    ent_preciohora = tk.Entry(window_configuracion)
    ent_preciohora.grid(row= 2,column = 4)
    ###
    lbl_pagominimo = tk.Label(window_configuracion,text="Pago Mínimo:",font = ("Helvetica",15))
    lbl_pagominimo.grid(row = 3,column = 1)
    ent_pagominimo = tk.Entry(window_configuracion)
    ent_pagominimo.grid(row= 3,column = 4)
    ###
    lbl_correosupervisor = tk.Label(window_configuracion,text="Correo Electrónico del Supervisor:",font = ("Helvetica",15))
    lbl_correosupervisor.grid(row = 4,column = 1)
    ent_correosupervisor = tk.Entry(window_configuracion)
    ent_correosupervisor.grid(row= 4,column = 4)
    ###
    lbl_minsparasalir = tk.Label(window_configuracion,text="Minutos Máximos para Salir después del Pago:",font = ("Helvetica",15))
    lbl_minsparasalir.grid(row = 4,column = 1)
    ent_minsparasalir = tk.Entry(window_configuracion)
    ent_minsparasalir.grid(row= 4,column = 4)

    ###
    lbl_tiposmoneda = tk.Label(window_configuracion,text = "Tipos de Moneda:",font = ("Helvetica",15))
    lbl_tiposmoneda.grid(row = 5,column = 1)
    ###
    lbl_moneda1 = tk.Label(window_configuracion,text="Moneda 1:",font = ("Helvetica",15))
    lbl_moneda1.grid(row = 6,column = 1)
    ent_moneda1 = tk.Entry(window_configuracion)
    ent_moneda1.grid(row= 6,column = 4)
    ###
    lbl_moneda2 = tk.Label(window_configuracion,text="Moneda 2:",font = ("Helvetica",15))
    lbl_moneda2.grid(row = 7,column = 1)
    ent_moneda2 = tk.Entry(window_configuracion)
    ent_moneda2.grid(row= 7,column = 4)
    ###
    lbl_tiposbilletes = tk.Label(window_configuracion,text = "Tipos de Billetes:",font = ("Helvetica",15))
    lbl_tiposbilletes.grid(row = 8,column = 1)
    ###
    lbl_billete1 = tk.Label(window_configuracion,text = "Billete 1:",font = ("Helvetica",15))
    lbl_billete1.grid(row = 9,column = 1)
    ent_billete1 = tk.Entry(window_configuracion)
    ent_billete1.grid(row = 9,column = 4)
    ###
    lbl_billete2 = tk.Label(window_configuracion,text = "Billete 2:",font = ("Helvetica",15))
    lbl_billete2.grid(row = 10,column = 1)
    ent_billete2 = tk.Entry(window_configuracion)
    ent_billete2.grid(row = 10,column = 4)

    window_configuracion.protocol("WM_DELETE_WINDOW",lambda:volvermain(window_configuracion))
    window_configuracion.mainloop()

######################
# PROGRAMA PRINCIPAL #
######################
window_main = tk.Tk()
window_main.title("Parqueo")
window_main.iconphoto(True,tk.PhotoImage(file="images\icon.png"))
window_main.resizable(False,False)
window_main.config(bg = fondo)
window_main.geometry("800x500+500+100")

#frames menú principal
frameizq = tk.Frame(window_main,bg = fondo)
frameizq.place(x= 90,y=100)
frameder = tk.Frame(window_main,bg = fondo)
frameder.place(x= 440,y=100)

#titulo menú principal
img9 = PhotoImage(file="images\img9.png")
lbl_menuprin = tk.Label(window_main,image=img9,bg= fondo,fg = fondo)
lbl_menuprin.pack()

#definición botones menú principal
img1 = PhotoImage(file="images\img1.png")
btn_config = tk.Button(frameizq,image =img1,bd = 0,bg = fondo,
activebackground=fondo,command = configuracion)
btn_config.pack(pady= 6)

img2 = PhotoImage(file="images\img2.png")
btn_cargarcajero = tk.Button(frameizq,image =img2,bd = 0,bg = fondo,
activebackground=fondo)
btn_cargarcajero.pack(pady= 6)

img3 = PhotoImage(file="images\img3.png")
btn_saldocajero = tk.Button(frameizq,image =img3,bd = 0,bg = fondo,
activebackground=fondo)
btn_saldocajero.pack(pady= 6)

img4 = PhotoImage(file="images\img4.png")
btn_ingresos = tk.Button(frameizq,image =img4,bd = 0,bg = fondo,
activebackground=fondo)
btn_ingresos.pack(pady= 6)

img5 = PhotoImage(file="images\img5.png")
btn_entradavehiculo = tk.Button(frameder,image =img5,bd = 0,bg = fondo,
activebackground=fondo)
btn_entradavehiculo.pack(pady= 6)

img6 = PhotoImage(file="images\img6.png")
btn_cajeroparqueo = tk.Button(frameder,image =img6,bd = 0,bg = fondo,
activebackground=fondo)
btn_cajeroparqueo.pack(pady= 6)

img7 = PhotoImage(file="images\img7.png")
btn_salidavehiculo = tk.Button(frameder,image =img7,bd = 0,bg = fondo,
activebackground=fondo)
btn_salidavehiculo.pack(pady= 6)

img8 = PhotoImage(file="images\img8.png")
btn_ayuda = tk.Button(frameder,image =img8,bd = 0,bg = fondo,
activebackground=fondo,command = ayuda)
btn_ayuda.pack(pady= 6)

window_main.protocol("WM_DELETE_WINDOW",salir)#protocolo a la hora de salir del programa
window_main.mainloop()