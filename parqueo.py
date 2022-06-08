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
from turtle import window_width
import requests
import re
from tkinter import *
from tkinter import messagebox
from datetime import datetime
#########################
# VARIABLES IMPORTANTES #
#########################
configurado = True
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

#funcion para verificar si el formato de un email es válido
def email_format_checker(email):
    email_regex = re.compile(r"[^@]+@[^@]+.[^@]+")
    if email_regex.match(email):
        return True
    else:
        return False

#funcion para verificar si un email existe
def email_checker(email):
    email_address = email
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address})

    status = response.json()['status']
    if status == "valid":
        return True
    elif status == "invalid":
        return False
    else:
        return False

#funcion para reiniciar una ventana
def restartwindow(ventana, funcion):
    ventana.destroy()
    funcion()

#funcion para verificar si una entry tiene letras
def lettercheck(elemento):
    try:
        int(elemento.get())
        return True
    except:
        showerror("ERROR","¡Solo se permiten Números!")
        return False

#########################
# FUNCIONES PRINCIPALES #
#########################
#########
# Ayuda #
#########
#función que despliega el manual de usuario
def ayuda():
    path =  "manual_de_usuario.docx"
    os.startfile(path)

#################
# Configuración #
#################
#función de la configuración
def configuracion():
    window_main.state('withdrawn')
    window_configuracion = tk.Toplevel(window_main)
    window_configuracion.title('Configuración')
    window_configuracion.geometry("+650+300")
    window_configuracion.resizable(False,False)
    window_configuracion.protocol("WM_DELETE_WINDOW",lambda:volvermain(window_configuracion))
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
    ent_correosupervisor = tk.Entry(window_configuracion,width=30)
    ent_correosupervisor.grid(row= 4,column = 4)
    ###
    lbl_minsparasalir = tk.Label(window_configuracion,text="Minutos Máximos para Salir después del Pago:",font = ("Helvetica",15))
    lbl_minsparasalir.grid(row = 5,column = 1)
    ent_minsparasalir = tk.Entry(window_configuracion)
    ent_minsparasalir.grid(row= 5,column = 4)
    ###
    lbl_tiposmoneda = tk.Label(window_configuracion,text = "Tipos de Moneda:",font = ("Helvetica",15))
    lbl_tiposmoneda.grid(row = 6,column = 1)
    ###
    lbl_moneda1 = tk.Label(window_configuracion,text="Moneda 1:",font = ("Helvetica",15))
    lbl_moneda1.grid(row = 7,column = 1)
    ent_moneda1 = tk.Entry(window_configuracion)
    ent_moneda1.grid(row= 7,column = 4)
    ###
    lbl_moneda2 = tk.Label(window_configuracion,text="Moneda 2:",font = ("Helvetica",15))
    lbl_moneda2.grid(row = 8,column = 1)
    ent_moneda2 = tk.Entry(window_configuracion)
    ent_moneda2.grid(row= 8,column = 4)
    ###
    lbl_tiposbilletes = tk.Label(window_configuracion,text = "Tipos de Billetes:",font = ("Helvetica",15))
    lbl_tiposbilletes.grid(row = 9,column = 1)
    ###
    lbl_billete1 = tk.Label(window_configuracion,text = "Billete 1:",font = ("Helvetica",15))
    lbl_billete1.grid(row = 10,column = 1)
    ent_billete1 = tk.Entry(window_configuracion)
    ent_billete1.grid(row = 10,column = 4)
    ###
    lbl_billete2 = tk.Label(window_configuracion,text = "Billete 2:",font = ("Helvetica",15))
    lbl_billete2.grid(row = 11,column = 1)
    ent_billete2 = tk.Entry(window_configuracion)
    ent_billete2.grid(row = 11,column = 4)
    ###
    list_ents = [ent_correosupervisor,ent_preciohora,ent_pagominimo,ent_espaciosparqueo,ent_minsparasalir,ent_moneda1,
    ent_moneda2,ent_billete1,ent_billete2]
    btn_okconfig = tk.Button(window_configuracion,text= "Ok",font=("Helvetica",15),bg = "#2ded37",
    command = lambda: okcancelconfig(window_configuracion,1,list_ents))
    btn_okconfig.grid(row = 12,column = 4)
    btn_cancelconfig = tk.Button(window_configuracion,text= "Cancel",font=("Helvetica",15),bg = "#f74343",
    command = lambda: okcancelconfig(window_configuracion,2,list_ents))
    btn_cancelconfig.grid(row = 12,column = 2)
    ###
    window_configuracion.mainloop()

def okcancelconfig(window,opcion,list):#funcion para determinar que hacer con la configuracion
    if opcion == 2:#cancelar
        validate = messagebox.askokcancel("Cancelar","¿Está Seguro que desea cancelar el Proceso?")
        if validate:
            volvermain(window)
    elif opcion == 1:#aceptar
        letras = False
        vacio = False
        for element in list[3:]:
            if element.get() != "":
                if not lettercheck(element):
                    letras = True
                    break
            else:
                vacio = True
        if vacio == False:
            if letras == False:
                # list_ents = [ent_correosupervisor,ent_preciohora,ent_pagominimo,ent_espaciosparqueo,ent_minsparasalir,ent_moneda1,
                # ent_moneda2,ent_billete1,ent_billete2]
                valido = True
                #validaciones
                if int(list[3].get()) < 1:#cantidad de espacios en el parqueo
                    valido = False
                    showerror("ERROR","Debe haber almenos un espacio en el parqueo")
                try:
                    round(float(list[1].get()),2)#precio por hora
                    round(float(list[2].get()),2)#pago mínimo
                    if float(list[1].get()) < 0 or float(list[2].get()) < 0:
                        valido =  False
                        showerror("ERROR","Datos negativos")
                except:
                    valido = False
                    showerror("ERROR","¡Solo se permiten Números!")

                if email_format_checker(list[0].get()):#verifica el formato del email del supervisor
                    if not email_checker(list[0].get()):#verifica si el correo existe
                        valido = False
                        showerror("ERROR","Email Inexistente")
                else:
                    valido = False
                    showerror("ERROR","Formato de Email Inválido")

                if int(list[4].get()) < 0:#comprobar que los minutos para salir es almenos mayor a 0
                    valido = False
                    showerror("ERROR","Datos negativos")

                #monedas
                if int(list[5].get()) != 0:
                    if int(list[5].get()) >= 0:
                        if int(list[5].get()) >= int(list[6].get()):
                            valido = False
                            showerror("ERROR","La denominación Moneda 1 debe ser menor a la denominación Moneda 2")
                    else:
                        valido = False
                        showerror("ERROR","La denominación debe ser mayor a cero")
                elif int(list[6].get()) != 0:
                    if int(list[6].get()) >= 0:
                        valido = False
                        showerror("ERROR","Si una denominación es cero la otra también lo debe ser")
                    else:
                        valido = False
                        showerror("ERROR","La denominación debe ser mayor a cero")

                #billetes
                if int(list[7].get()) != 0:
                    if int(list[7].get()) >= 0:
                        if int(list[7].get()) >= int(list[8].get()):
                            valido = False
                            showerror("ERROR","La denominación Billete 1 debe ser menor a la denominación Billete 2")
                    else:
                        valido = False
                        showerror("ERROR","La denomacióndebe ser mayor a cero")
                elif int(list[8].get()) != 0:
                    if int(list[8].get()) >= 0:
                        valido = False
                        showerror("ERROR","Si una denominación es cero la otra también lo debe ser")
                    else:
                        valido = False
                        showerror("ERROR","La denomacióndebe ser mayor a cero")
                #probar si el pago mínimo se puede realizar conforme a las denominaciones
                if valido == True:
                    divisible = False
                    ceros = False
                    for entry in list[5:]:
                        if int(entry.get()) != 0:
                            if int(list[2].get()) % int(entry.get()) != 0:
                                continue
                            else:
                                divisible =  True
                                break
                        else:
                            ceros = True
                    if divisible == False and ceros == False:
                        valido =  False
                        showerror("ERROR","Pago mínimo irrealizable")

                if valido == True:#guardar valores en el archivo
                    configfile = open("configuración.dat","w")
                    for entry in list:
                        linea = str(entry.get()) + "\n"
                        configfile.write(linea)
                    configfile.close()
                    global configurado
                    configurado = True
                    volvermain(window)
        else:
            showerror("ERROR","Hay datos vacíos")
#################
# Cargar Cajero #
#################
def cargarcajero():
    global configurado
    if configurado == False:#en caso de no estar configurado no hace el proceso
        return
    window_main.state('withdrawn')
    window_cargarcajero = tk.Toplevel(window_main)
    window_cargarcajero.title('Cargar Cajero')
    window_cargarcajero.geometry("+650+355")  
    window_cargarcajero.resizable(False,False)
    window_cargarcajero.protocol("WM_DELETE_WINDOW",lambda:volvermain(window_cargarcajero))
    #SALDO ANTES DE LA CARGA
    lbl_saldoanterior = tk.Label(window_cargarcajero,text="SALDO ANTES DE LA CARGA",font = ("Helvetica",14))
    lbl_saldoanterior.grid(row = 1,column = 2,columnspan = 2)
    #DENOMINACIÓN-CANTIDAD-TOTAL
    lbl_denominacion = tk.Label(window_cargarcajero,text="DENOMINACIÓN",font = ("Helvetica",14))
    lbl_denominacion.grid(row = 2,column = 1)
    lbl_cantidad = tk.Label(window_cargarcajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 2)
    lbl_total = tk.Label(window_cargarcajero,text="TOTAL",font = ("Helvetica",14))
    lbl_total.grid(row = 2,column = 3,columnspan = 1)
    #ABRE EL ARCHIVO DE LA CONFIGURACIÓN PARA LEER CONTENIDOS
    configfile = open("configuración.dat","r")
    configlines = configfile.readlines()
    configfile.close()
    #MONEDAS
    textmoneda1 = "Monedas de "+str(configlines[5])
    lbl_moneda1 = tk.Label(window_cargarcajero,text= textmoneda1,font = ("Helvetica",13))
    lbl_moneda1.grid(row = 3,column = 1)
    lbl_cantmoneda1anterior = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantmoneda1anterior.grid(row=3,column = 2)
    lbl_totalmoneda1anterior = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalmoneda1anterior.grid(row =3,column = 3,columnspan = 1)
    ###
    textmoneda2 = "Monedas de "+str(configlines[6])
    lbl_moneda2 = tk.Label(window_cargarcajero,text= textmoneda2,font = ("Helvetica",13))
    lbl_moneda2.grid(row = 4,column = 1)
    lbl_cantmoneda2anterior = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantmoneda2anterior.grid(row=4,column = 2)
    lbl_totalmoneda2anterior = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalmoneda2anterior.grid(row =4,column = 3,columnspan = 1)
    #TOTAL
    lbl_totalmonedasanterior = tk.Label(window_cargarcajero,text = "TOTAL DE MONEDAS",font = ("Helvetica",14))
    lbl_totalmonedasanterior.grid(row = 5,column = 1)
    lbl_totalcantmonedasanterior = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmonedasanterior.grid(row = 5,column = 2)
    lbl_totaltotalmonedasanterior = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalmonedasanterior.grid(row = 5,column = 3,columnspan = 1)

    #BILLETES
    textbillete1 = "Billetes de "+str(configlines[7])
    lbl_billete1 = tk.Label(window_cargarcajero,text= textbillete1,font = ("Helvetica",13))
    lbl_billete1.grid(row = 6,column = 1)
    lbl_cantbillete1 = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantbillete1.grid(row=6,column = 2)
    lbl_totalbillete1 = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalbillete1.grid(row=6,column = 3,columnspan = 1)
    ###
    textbillete2 = "Billetes de "+str(configlines[8])
    lbl_billete2 = tk.Label(window_cargarcajero,text= textbillete2,font = ("Helvetica",13))
    lbl_billete2.grid(row = 7,column = 1)
    lbl_cantbillete2 = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantbillete2.grid(row=7,column = 2)
    lbl_totalbillete2 = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalbillete2.grid(row=7,column = 3,columnspan = 1)
    #TOTAL
    lbl_totalbilletesanterior = tk.Label(window_cargarcajero,text = "TOTAL DE BILLETES",font = ("Helvetica",14))
    lbl_totalbilletesanterior.grid(row = 8,column = 1)
    lbl_totalcantbilletesanterior = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbilletesanterior.grid(row = 8,column = 2)
    lbl_totaltotalbilletesanterior = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalbilletesanterior.grid(row = 8,column = 3,columnspan = 1)

    ###
    #CARGA
    lbl_carga = tk.Label(window_cargarcajero,text="CARGA",font = ("Helvetica",14))
    lbl_carga.grid(row = 1,column = 6)

    lbl_cantidad = tk.Label(window_cargarcajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 5)
    lbl_total2 = tk.Label(window_cargarcajero,text="TOTAL      ",font = ("Helvetica",14))
    lbl_total2.grid(row = 2,column = 7,columnspan = 1)
    #entrys monedas
    ent_moneda1 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_moneda1.grid(row = 3,column = 5)
    ent_moneda2 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_moneda2.grid(row = 4,column = 5)
    #totales
    lbl_totalcantmoneda1carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmoneda1carga.grid(row = 3,column = 7,columnspan = 1)
    lbl_totaltotalmoneda2carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalmoneda2carga.grid(row = 4,column = 7,columnspan = 1)
    #total de todos
    lbl_totalcantmonedascarga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmonedascarga.grid(row = 5,column = 5)
    lbl_totaltotalmonedascarga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalmonedascarga.grid(row = 5,column = 7,columnspan = 1)

    #entrys billetes
    ent_billete1 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_billete1.grid(row = 6,column = 5)
    ent_billete2 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_billete2.grid(row = 7,column = 5)
    #totales
    lbl_totalcantbillete1carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbillete1carga.grid(row = 6,column = 7,columnspan = 1)
    lbl_totaltotalbillete2carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalbillete2carga.grid(row = 7,column = 7,columnspan = 1)
    #total de todos
    lbl_totalcantbilletesanterior = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbilletesanterior.grid(row = 8,column = 5)
    lbl_totaltotalbilletesanterior = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalbilletesanterior.grid(row = 8,column = 7,columnspan = 1)

    ###
    #SALDO
    lbl_saldo = tk.Label(window_cargarcajero,text="SALDO",font = ("Helvetica",14))
    lbl_saldo.grid(row = 1,column = 10)
    lbl_cantidad = tk.Label(window_cargarcajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 9)
    lbl_total = tk.Label(window_cargarcajero,text="TOTAL",font = ("Helvetica",14))
    lbl_total.grid(row = 2,column = 11)
    #labels monedas
    lbl_cantmoneda1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantmoneda1saldo.grid(row=3,column = 9)
    lbl_totalmoneda1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalmoneda1saldo.grid(row =3,column = 11)

    lbl_cantmoneda2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantmoneda2saldo.grid(row=4,column = 9)
    lbl_totalmoneda2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalmoneda2saldo.grid(row =4,column = 11)

    #total monedas
    lbl_totalcantmonedassaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmonedassaldo.grid(row = 5,column = 9)
    lbl_totaltotalmonedassaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalmonedassaldo.grid(row = 5,column = 11)

    #labels billetes
    lbl_cantbillete1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantbillete1saldo.grid(row=6,column = 9)
    lbl_totalbillete1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalbillete1saldo.grid(row =6,column = 11)

    lbl_cantbillete2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantbillete2saldo.grid(row=7,column = 9)
    lbl_totalbillete2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalbillete2saldo.grid(row =7,column = 11)

    #total monedas
    lbl_totalcantbilletessaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbilletessaldo.grid(row = 8,column = 9)
    lbl_totaltotalbilletessaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalbilletessaldo.grid(row = 8,column = 11)

    #TOTAL DEL CAJERO
    lbl_totalcajero = tk.Label(window_cargarcajero,text = "TOTAL DEL CAJERO",font = ("Helvetica",14))
    lbl_totalcajero.grid(row = 9,column = 1)
    lbl_totalcajerocant = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",14))
    lbl_totalcajerocant.grid(row = 9,column = 11)


    btn_ok = tk.Button(window_cargarcajero,text = "Ok",font = ("Helvetica",14),bg = "#2ded37")
    btn_ok.grid(row = 10,column = 2)
    btn_cancelar = tk.Button(window_cargarcajero,text = "Cancelar",font = ("Helvetica",14),bg = "#f74343")
    btn_cancelar.grid(row = 10,column = 3)
    btn_vaciarcajero = tk.Button(window_cargarcajero,text = "Vaciar Cajero",font = ("Helvetica",14),bg = "skyblue")
    btn_vaciarcajero.grid(row = 10,column = 5)

    window_cargarcajero.mainloop()
######################
# Ingresos de Dinero #
######################
def ingresosDinero():
    global configurado
    if configurado == False:#en caso de no estar configurado no hace el proceso
        return
    window_main.state('withdrawn')
    window_ingresos = tk.Toplevel(window_main)
    window_ingresos.title('Ingresos de dinero')
    window_ingresos.geometry("+650+355")
    window_ingresos.resizable(False,False)
    window_ingresos.protocol("WM_DELETE_WINDOW",lambda:volvermain(window_ingresos))

    lbl_deldia = tk.Label(window_ingresos,text="Del día",font = ("Helvetica",15))
    lbl_deldia.grid(row = 1,column = 1)
    ent_deldia = tk.Entry(window_ingresos)
    ent_deldia.grid(row= 1,column = 2)
    ent_deldia.insert(END, 'dd/mm/aaaa')

    lbl_aldia = tk.Label(window_ingresos,text="Al día",font = ("Helvetica",15))
    lbl_aldia.grid(row = 2,column = 1)
    ent_aldia = tk.Entry(window_ingresos)
    ent_aldia.grid(row= 2,column = 2)
    ent_aldia.insert(END, 'dd/mm/aaaa')

    lbl_vacia = tk.Label(window_ingresos,text=" ")
    lbl_vacia.grid(row = 3,column = 1)

    lbl_totingefe = tk.Label(window_ingresos,text="Total de ingresos en efectivo",font = ("Helvetica",15))
    lbl_totingefe.grid(row = 4,column = 1,sticky=W)

    lbl_totingtar = tk.Label(window_ingresos,text="Total de ingresos por tarjeta de crédito",font = ("Helvetica",15))
    lbl_totingtar.grid(row = 5,column = 1, sticky=W)

    lbl_toting = tk.Label(window_ingresos,text="Total de ingresos",font = ("Helvetica",15))
    lbl_toting.grid(row = 6,column = 1,sticky=W)

    lbl_vacia = tk.Label(window_ingresos,text=" ")
    lbl_vacia.grid(row = 7,column = 1)

    lbl_toting = tk.Label(window_ingresos,text="Estimado de ingresos por recibir",font = ("Helvetica",15))
    lbl_toting.grid(row = 8,column = 1,sticky=W)

    btn_ok = tk.Button(window_ingresos,text="Ok",font = ("Helvetica",15),bg = "#2ded37", command= lambda: volvermain(window_ingresos))
    btn_ok.grid(row = 9, column= 1)

    window_ingresos.mainloop()

#######################
# Entrada de Vehículo #
#######################
def entradaVehiculo():
    global configurado
    if configurado == False:#en caso de no estar configurado no hace el proceso
        return
    window_main.state('withdrawn')
    ventana_entradaVehiculo = tk.Toplevel(window_main)
    ventana_entradaVehiculo.title('Entrada de vehículo')
    ventana_entradaVehiculo.resizable(False,False)
    ventana_entradaVehiculo.protocol("WM_DELETE_WINDOW",lambda:volvermain(ventana_entradaVehiculo))

    now = datetime.now()
    date = now.strftime("%H:%M %d/%m/%Y ")

    lbl_espdisp = tk.Label(ventana_entradaVehiculo, text = 'Espacios disponibles    ', font= ("Helvetica",12))
    lbl_espdisp.grid(row = 1,column = 1, sticky= W)

    lbl_vacia = tk.Label(ventana_entradaVehiculo,text=" ")
    lbl_vacia.grid(row = 2,column = 1)

    lbl_suplaca = tk.Label(ventana_entradaVehiculo, text = 'Su placa    ', font= ("Helvetica",15))
    lbl_suplaca.grid(row = 3,column = 1, sticky= W)

    ent_suplaca = tk.Entry(ventana_entradaVehiculo)
    ent_suplaca.grid(row = 3, column = 2)

    lbl_campasig = tk.Label(ventana_entradaVehiculo, text = 'Campo asignado    ', font= ("Helvetica",15))
    lbl_campasig.grid(row = 4,column = 1, sticky= W)

    lbl_horaent = tk.Label(ventana_entradaVehiculo, text = 'Hora de entrada          '+date, font= ("Helvetica",15))
    lbl_horaent.grid(row = 5,column = 1, sticky= W)

    lbl_preciohora = tk.Label(ventana_entradaVehiculo, text = 'Precio de entrada    ', font= ("Helvetica",15))
    lbl_preciohora.grid(row = 6,column = 1, sticky= W)

    btn_ok = tk.Button(ventana_entradaVehiculo,text="Ok",font = ("Helvetica",15))
    btn_ok.grid(row = 7, column= 1, sticky= E)
    btn_cancel = tk.Button(ventana_entradaVehiculo,text="Cancel",font = ("Helvetica",15), command= lambda: restartwindow(ventana_entradaVehiculo, entradaVehiculo))
    btn_cancel.grid(row = 7, column= 2, sticky= W)

    ventana_entradaVehiculo.mainloop()
######################
# Salida de Vehículo #
######################
def salidaVehiculo():
    global configurado
    if configurado == False:#en caso de no estar configurado no hace el proceso
        return
    window_main.state('withdrawn')
    ventana_salidaVehiculo = tk.Toplevel(window_main)
    ventana_salidaVehiculo.title('Salida de vehículo')
    ventana_salidaVehiculo.protocol("WM_DELETE_WINDOW",lambda:volvermain(ventana_salidaVehiculo))

    lbl_suplaca = tk.Label(ventana_salidaVehiculo, text = 'Su placa    ', font= ("Helvetica",15))
    lbl_suplaca.grid(row = 1,column = 1, sticky= W)

    ent_suplaca = tk.Entry(ventana_salidaVehiculo)
    ent_suplaca.grid(row = 1, column = 2)

    btn_ok = tk.Button(ventana_salidaVehiculo,text="Ok",font = ("Helvetica",15), command= lambda: restartwindow(ventana_salidaVehiculo, salidaVehiculo))
    btn_ok.grid(row = 2, column= 1)
    ventana_salidaVehiculo.mainloop()
######################
# PROGRAMA PRINCIPAL #
######################
window_main = tk.Tk()
window_main.title("Parqueo")
window_main.iconphoto(True,tk.PhotoImage(file="images\icon.png"))
window_main.resizable(False,False)
window_main.config(bg = fondo)
window_main.geometry("800x500+550+250")

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
activebackground=fondo,command =  cargarcajero)
btn_cargarcajero.pack(pady= 6)

img3 = PhotoImage(file="images\img3.png")
btn_saldocajero = tk.Button(frameizq,image =img3,bd = 0,bg = fondo,
activebackground=fondo)
btn_saldocajero.pack(pady= 6)

img4 = PhotoImage(file="images\img4.png")
btn_ingresos = tk.Button(frameizq,image =img4,bd = 0,bg = fondo,
activebackground=fondo,command = ingresosDinero)
btn_ingresos.pack(pady= 6)

img5 = PhotoImage(file="images\img5.png")
btn_entradavehiculo = tk.Button(frameder,image =img5,bd = 0,bg = fondo,
activebackground=fondo,command = entradaVehiculo)
btn_entradavehiculo.pack(pady= 6)

img6 = PhotoImage(file="images\img6.png")
btn_cajeroparqueo = tk.Button(frameder,image =img6,bd = 0,bg = fondo,
activebackground=fondo)
btn_cajeroparqueo.pack(pady= 6)

img7 = PhotoImage(file="images\img7.png")
btn_salidavehiculo = tk.Button(frameder,image =img7,bd = 0,bg = fondo,
activebackground=fondo,command = salidaVehiculo)
btn_salidavehiculo.pack(pady= 6)

img8 = PhotoImage(file="images\img8.png")
btn_ayuda = tk.Button(frameder,image =img8,bd = 0,bg = fondo,
activebackground=fondo,command = ayuda)
btn_ayuda.pack(pady= 6)

window_main.protocol("WM_DELETE_WINDOW",salir)#protocolo a la hora de salir del programa
window_main.mainloop()