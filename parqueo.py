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
import requests
import re
from tkinter import *
from tkinter import messagebox
from datetime import datetime
##########################
# VALIDACIONES INICIALES #
##########################
#valida si se debe crear el parqueo al inicio del programa.
try:
    fileparqueo = open("parqueo.dat","rb")
    x = pickle.load(fileparqueo)
    fileparqueo.close()
except EOFError:
    print("Se creó")
    fileparqueo = open("parqueo.dat","wb")
    pickle.dump({},fileparqueo)
    fileparqueo.close()
#########################
# VARIABLES IMPORTANTES #
#########################
configurado = True
lleno =  False
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

#función para validar entrys y verificar que solo se pongan números
def solonumeros(letra):
    try:
        if int(letra) or letra == "" or letra == "0":#el caracter solo se despliega si es un número
            return True
    except:#caso contrario no lo hace
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

    verif = window_configuracion.register(solonumeros)
    ent_espaciosparqueo.config(validate="key",validatecommand=(verif,"%P"))
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

            # list_ents = [ent_correosupervisor,ent_preciohora,ent_pagominimo,ent_espaciosparqueo,ent_minsparasalir,ent_moneda1,
            # ent_moneda2,ent_billete1,ent_billete2]
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
    #ABRE EL ARCHIVO DE LA CONFIGURACIÓN PARA LEER CONTENIDO
    configfile = open("configuración.dat","r")
    configlines = configfile.readlines()
    configfile.close()
    #ABRE EL ARCHIVO DEL CAJERO PARA LEER CONTENIDO
    cajerofile = open("cajero.dat","r")
    denominaciones = cajerofile.readlines()
    cajerofile.close()
    #MONEDAS
    textmoneda1 = "Monedas de "+str(configlines[5])
    lbl_moneda1 = tk.Label(window_cargarcajero,text= textmoneda1,font = ("Helvetica",13))
    lbl_moneda1.grid(row = 3,column = 1)

    cantmoneda1 = str(denominaciones[0])

    lbl_cantmoneda1anterior = tk.Label(window_cargarcajero,text= cantmoneda1,font = ("Helvetica",13))
    lbl_cantmoneda1anterior.grid(row=3,column = 2)

    totalmoneda1anterior = str(int(denominaciones[0]) * int(configlines[5]))

    lbl_totalmoneda1anterior = tk.Label(window_cargarcajero,text= totalmoneda1anterior,font = ("Helvetica",13))
    lbl_totalmoneda1anterior.grid(row =3,column = 3,columnspan = 1)
    ###
    textmoneda2 = "Monedas de "+str(configlines[6])
    lbl_moneda2 = tk.Label(window_cargarcajero,text= textmoneda2,font = ("Helvetica",13))
    lbl_moneda2.grid(row = 4,column = 1)

    cantmoneda2 = str(denominaciones[1])

    lbl_cantmoneda2anterior = tk.Label(window_cargarcajero,text= cantmoneda2,font = ("Helvetica",13))
    lbl_cantmoneda2anterior.grid(row=4,column = 2)

    totalmoneda2anterior = str(int(denominaciones[1]) * int(configlines[6]))

    lbl_totalmoneda2anterior = tk.Label(window_cargarcajero,text= totalmoneda2anterior,font = ("Helvetica",13))
    lbl_totalmoneda2anterior.grid(row =4,column = 3,columnspan = 1)
    #TOTAL
    lbl_totalmonedasanterior = tk.Label(window_cargarcajero,text = "TOTAL DE MONEDAS",font = ("Helvetica",14))
    lbl_totalmonedasanterior.grid(row = 5,column = 1)

    totalcantmonedasanterior = str(int(cantmoneda1) + int(cantmoneda2))

    lbl_totalcantmonedasanterior = tk.Label(window_cargarcajero,text = totalcantmonedasanterior,font = ("Helvetica",13))
    lbl_totalcantmonedasanterior.grid(row = 5,column = 2)

    totalmonedasanterior = str(int(totalmoneda1anterior) + int(totalmoneda2anterior))

    lbl_totaltotalmonedasanterior = tk.Label(window_cargarcajero,text = totalmonedasanterior,font = ("Helvetica",13))
    lbl_totaltotalmonedasanterior.grid(row = 5,column = 3,columnspan = 1)

    #BILLETES
    textbillete1 = "Billetes de "+str(configlines[7])
    lbl_billete1 = tk.Label(window_cargarcajero,text= textbillete1,font = ("Helvetica",13))
    lbl_billete1.grid(row = 6,column = 1)

    cantbillete1 = str(denominaciones[2])

    lbl_cantbillete1 = tk.Label(window_cargarcajero,text= cantbillete1,font = ("Helvetica",13))
    lbl_cantbillete1.grid(row=6,column = 2)

    totalbillete1anterior = str(int(denominaciones[2])*int(configlines[7]))

    lbl_totalbillete1 = tk.Label(window_cargarcajero,text= totalbillete1anterior,font = ("Helvetica",13))
    lbl_totalbillete1.grid(row=6,column = 3,columnspan = 1)
    ###
    textbillete2 = "Billetes de "+str(configlines[8])
    lbl_billete2 = tk.Label(window_cargarcajero,text= textbillete2,font = ("Helvetica",13))
    lbl_billete2.grid(row = 7,column = 1)

    cantbillete2 = str(denominaciones[3])

    lbl_cantbillete2 = tk.Label(window_cargarcajero,text= cantbillete2,font = ("Helvetica",13))
    lbl_cantbillete2.grid(row=7,column = 2)

    totalbillete2anterior = str(int(denominaciones[3])*int(configlines[8]))

    lbl_totalbillete2 = tk.Label(window_cargarcajero,text= totalbillete2anterior,font = ("Helvetica",13))
    lbl_totalbillete2.grid(row=7,column = 3,columnspan = 1)
    #TOTAL
    lbl_totalbilletesanterior = tk.Label(window_cargarcajero,text = "TOTAL DE BILLETES",font = ("Helvetica",14))
    lbl_totalbilletesanterior.grid(row = 8,column = 1)

    totalcantbilletesanterior = str(int(cantbillete1) + int(cantbillete2))

    lbl_totalcantbilletesanterior = tk.Label(window_cargarcajero,text = totalcantbilletesanterior,font = ("Helvetica",13))
    lbl_totalcantbilletesanterior.grid(row = 8,column = 2)

    totalbilletesanterior = str(int(totalbillete1anterior) + int(totalbillete2anterior))

    lbl_totaltotalbilletesanterior = tk.Label(window_cargarcajero,text = totalbilletesanterior,font = ("Helvetica",13))
    lbl_totaltotalbilletesanterior.grid(row = 8,column = 3,columnspan = 1)

    #CARGA
    lbl_carga = tk.Label(window_cargarcajero,text="CARGA",font = ("Helvetica",14))
    lbl_carga.grid(row = 1,column = 6)
    lbl_cantidad = tk.Label(window_cargarcajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 5)
    lbl_total2 = tk.Label(window_cargarcajero,text="TOTAL      ",font = ("Helvetica",14))
    lbl_total2.grid(row = 2,column = 7,columnspan = 1)

    #entrys monedas
    global ent_moneda1
    ent_moneda1 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_moneda1.grid(row = 3,column = 5)
    global ent_moneda2
    ent_moneda2 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_moneda2.grid(row = 4,column = 5)

    #totales
    global lbl_totalcantmoneda1carga
    lbl_totalcantmoneda1carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmoneda1carga.grid(row = 3,column = 7,columnspan = 1)

    global lbl_totalcantmoneda2carga
    lbl_totalcantmoneda2carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmoneda2carga.grid(row = 4,column = 7,columnspan = 1)

    #total de todos
    global lbl_totalcantmonedascarga
    lbl_totalcantmonedascarga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmonedascarga.grid(row = 5,column = 5)

    global lbl_totaltotalmonedascarga
    lbl_totaltotalmonedascarga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalmonedascarga.grid(row = 5,column = 7,columnspan = 1)

    #entrys billetes
    global ent_billete1
    ent_billete1 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_billete1.grid(row = 6,column = 5)
    global ent_billete2
    ent_billete2 = tk.Entry(window_cargarcajero,font = ("Helvetica",13),width =10)
    ent_billete2.grid(row = 7,column = 5)
    #totales
    global lbl_totalcantbillete1carga
    lbl_totalcantbillete1carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbillete1carga.grid(row = 6,column = 7,columnspan = 1)
    global lbl_totalcantbillete2carga
    lbl_totalcantbillete2carga = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbillete2carga.grid(row = 7,column = 7,columnspan = 1)
    #total de todos
    global lbl_totalcantbilletescargar
    lbl_totalcantbilletescargar = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbilletescargar.grid(row = 8,column = 5)
    global lbl_totaltotalbilletescargar
    lbl_totaltotalbilletescargar = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalbilletescargar.grid(row = 8,column = 7,columnspan = 1)

    ###
    #SALDO
    lbl_saldo = tk.Label(window_cargarcajero,text="SALDO",font = ("Helvetica",14))
    lbl_saldo.grid(row = 1,column = 10)
    lbl_cantidad = tk.Label(window_cargarcajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 9)
    lbl_total = tk.Label(window_cargarcajero,text="TOTAL",font = ("Helvetica",14))
    lbl_total.grid(row = 2,column = 11)
    #labels monedas
    global lbl_cantmoneda1saldo
    lbl_cantmoneda1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantmoneda1saldo.grid(row=3,column = 9)
    global lbl_totalmoneda1saldo
    lbl_totalmoneda1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalmoneda1saldo.grid(row =3,column = 11)

    global lbl_cantmoneda2saldo
    lbl_cantmoneda2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantmoneda2saldo.grid(row=4,column = 9)
    global lbl_totalmoneda2saldo
    lbl_totalmoneda2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalmoneda2saldo.grid(row =4,column = 11)

    #total monedas
    global lbl_totalcantmonedassaldo
    lbl_totalcantmonedassaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantmonedassaldo.grid(row = 5,column = 9)
    global lbl_totaltotalmonedassaldo
    lbl_totaltotalmonedassaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalmonedassaldo.grid(row = 5,column = 11)

    #labels billetes
    global lbl_cantbillete1saldo
    lbl_cantbillete1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantbillete1saldo.grid(row=6,column = 9)
    global lbl_totalbillete1saldo
    lbl_totalbillete1saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalbillete1saldo.grid(row =6,column = 11)

    global lbl_cantbillete2saldo
    lbl_cantbillete2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_cantbillete2saldo.grid(row=7,column = 9)
    global lbl_totalbillete2saldo
    lbl_totalbillete2saldo = tk.Label(window_cargarcajero,text= "0",font = ("Helvetica",13))
    lbl_totalbillete2saldo.grid(row =7,column = 11)

    #total monedas
    global lbl_totalcantbilletessaldo
    lbl_totalcantbilletessaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totalcantbilletessaldo.grid(row = 8,column = 9)
    global lbl_totaltotalbilletessaldo
    lbl_totaltotalbilletessaldo = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",13))
    lbl_totaltotalbilletessaldo.grid(row = 8,column = 11)

    #TOTAL DEL CAJERO
    lbl_totalcajero = tk.Label(window_cargarcajero,text = "TOTAL DEL CAJERO",font = ("Helvetica",14))
    lbl_totalcajero.grid(row = 9,column = 1)
    global lbl_totalcajerocant
    lbl_totalcajerocant = tk.Label(window_cargarcajero,text = "0",font = ("Helvetica",14))
    lbl_totalcajerocant.grid(row = 9,column = 11)

    #registros
    actvalues = window_cargarcajero.register(actualizarvalores)#registro para la validación de los entrys

    # actualizarvalores(numero,indice,totalentry,totalcantcarga,totaltodocarga,cantsaldo,totalsaldo,totalcantsaldo,totaltodosaldo,totalcajero)
    ent_moneda1.config(validate = "key",validatecommand=(actvalues,"%P",0))
    ent_moneda2.config(validate = "key",validatecommand=(actvalues,"%P",1))
    ent_billete1.config(validate = "key",validatecommand=(actvalues,"%P",2))
    ent_billete2.config(validate = "key",validatecommand=(actvalues,"%P",3))

    btn_ok = tk.Button(window_cargarcajero,text = "Ok",font = ("Helvetica",14),bg = "#2ded37",
    command = lambda: okcargarcajero(window_cargarcajero))
    btn_ok.grid(row = 10,column = 2)
    btn_cancelar = tk.Button(window_cargarcajero,text = "Cancelar",font = ("Helvetica",14),bg = "#f74343",
    command = lambda : volvermain(window_cargarcajero))
    btn_cancelar.grid(row = 10,column = 3)
    btn_vaciarcajero = tk.Button(window_cargarcajero,text = "Vaciar Cajero",font = ("Helvetica",14),bg = "skyblue")
    btn_vaciarcajero.grid(row = 10,column = 5)

    window_cargarcajero.mainloop()

#función para actualizar las labels del cargar cajero conforme se dan
def actualizarvalores(numero,indice):
    global lbl_totalcantmoneda1carga
    global lbl_totalcantmoneda2carga
    global lbl_totalcantmonedascarga
    global lbl_totaltotalmonedascarga
    global lbl_totalcantbillete1carga
    global lbl_totalcantbillete2carga
    global lbl_totalcantbilletescargar
    global lbl_totaltotalbilletescargar
    global lbl_cantmoneda1saldo
    global lbl_totalmoneda1saldo
    global lbl_cantmoneda2saldo
    global lbl_totalmoneda2saldo
    global lbl_totalcantmonedassaldo
    global lbl_totaltotalmonedassaldo
    global lbl_cantbillete1saldo
    global lbl_totalbillete1saldo
    global lbl_cantbillete2saldo
    global lbl_totalbillete2saldo
    global lbl_totalcantbilletessaldo
    global lbl_totaltotalbilletessaldo
    global lbl_totalcajerocant
    global ent_moneda1
    global ent_moneda2
    global ent_billete1
    global ent_billete2
    #abrir el archivo del cajero para leer vlaores
    configfile = open("configuración.dat","r")
    denominaciones = configfile .readlines()
    denominaciones = denominaciones[5:]
    configfile.close()
    cajerofile = open("cajero.dat","r")
    cantdenominaciones = cajerofile.readlines()
    cajerofile.close()

    if ent_moneda1.get() == "":
        moneda1 = 0
    else:
        moneda1 = ent_moneda1.get()

    if ent_moneda2.get() == "":
        moneda2 = 0
    else:
        moneda2 = ent_moneda2.get()

    if ent_billete1.get() == "":
        billete1 = 0
    else:
        billete1 = ent_billete1.get()

    if ent_billete2.get() == "":
        billete2 = 0
    else:
        billete2 = ent_billete2.get()

    try:
        if int(numero) or numero == "" or numero == "0":
            if int(indice) == 0:#moneda1
                lbl_totalcantmoneda1carga.config(text = str(int(numero)*int(denominaciones[int(indice)])))
                lbl_totalcantmonedascarga.config(text = int(numero)+int(moneda2))
                lbl_cantmoneda1saldo.config(text = int(numero)+int(cantdenominaciones[int(indice)]))
                lbl_totalmoneda1saldo.config(text = int(lbl_cantmoneda1saldo['text'])*int(denominaciones[int(indice)]))
                lbl_totalcantmonedassaldo.config(text = int(lbl_cantmoneda1saldo['text'])+int(lbl_cantmoneda2saldo['text']))
                lbl_totaltotalmonedassaldo.config(text = int(lbl_totalmoneda1saldo['text'])+int(lbl_totalmoneda2saldo['text']))
                lbl_totaltotalmonedascarga.config(text = int(lbl_totalcantmoneda1carga['text']) + int(lbl_totalcantmoneda2carga['text']))
            elif int(indice) == 1:#moneda2
                lbl_totalcantmoneda2carga.config(text = str(int(numero)*int(denominaciones[int(indice)])))
                lbl_totalcantmonedascarga.config(text = int(numero)+int(moneda1))
                lbl_cantmoneda2saldo.config(text = int(numero)+int(cantdenominaciones[int(indice)]))
                lbl_totalmoneda2saldo.config(text = int(lbl_cantmoneda2saldo['text'])*int(denominaciones[int(indice)]))
                lbl_totalcantmonedassaldo.config(text = int(lbl_cantmoneda2saldo['text'])+int(lbl_cantmoneda1saldo['text']))
                lbl_totaltotalmonedassaldo.config(text = int(lbl_totalmoneda2saldo['text'])+int(lbl_totalmoneda1saldo['text']))
                lbl_totaltotalmonedascarga.config(text = int(lbl_totalcantmoneda2carga['text']) + int(lbl_totalcantmoneda1carga['text']))
            elif int(indice) == 2:#billete1
                lbl_totalcantbillete1carga.config(text = str(int(numero)*int(denominaciones[int(indice)])))
                lbl_totalcantbilletescargar.config(text = int(numero)+int(billete2))
                lbl_cantbillete1saldo.config(text = int(numero)+int(cantdenominaciones[int(indice)]))
                lbl_totalbillete1saldo.config(text = int(lbl_cantbillete1saldo['text'])*int(denominaciones[int(indice)]))
                lbl_totalcantbilletessaldo.config(text = int(lbl_cantbillete1saldo['text'])+int(lbl_cantbillete2saldo['text']))
                lbl_totaltotalbilletessaldo.config(text = int(lbl_totalbillete1saldo['text'])+int(lbl_totalbillete2saldo['text']))
                lbl_totaltotalbilletescargar.config(text = int(lbl_totalcantbillete1carga['text']) + int(lbl_totalcantbillete2carga['text']))
            else:#billete2
                lbl_totalcantbillete2carga.config(text = str(int(numero)*int(denominaciones[int(indice)])))
                lbl_totalcantbilletescargar.config(text = int(numero)+int(billete1))
                lbl_cantbillete2saldo.config(text = int(numero)+int(cantdenominaciones[int(indice)]))
                lbl_totalbillete2saldo.config(text = int(lbl_cantbillete2saldo['text'])*int(denominaciones[int(indice)]))
                lbl_totalcantbilletessaldo.config(text = int(lbl_cantbillete2saldo['text'])+int(lbl_cantbillete1saldo['text']))
                lbl_totaltotalbilletessaldo.config(text = int(lbl_totalbillete2saldo['text'])+int(lbl_totalbillete1saldo['text']))
                lbl_totaltotalbilletescargar.config(text = int(lbl_totalcantbillete2carga['text']) + int(lbl_totalcantbillete1carga['text']))

            lbl_totalcajerocant.config(text =int(lbl_totaltotalmonedassaldo['text']) + int(lbl_totaltotalbilletessaldo['text'])  )
            return True
    except:
        return False

def okcargarcajero(window):
    global lbl_cantmoneda1saldo
    global lbl_cantbillete2saldo
    global lbl_cantbillete1saldo
    global lbl_cantbillete2saldo
    global ent_moneda1
    global ent_moneda2
    global ent_billete1
    global ent_billete2
    if ent_moneda1.get() != "" and ent_moneda2.get() != "" and ent_billete1.get() != "" and ent_billete2.get() != "":
        cajerofile = open("cajero.dat","w")
        cajerofile.write(str(lbl_cantmoneda1saldo['text'])+"\n")
        cajerofile.write(str(lbl_cantmoneda2saldo['text'])+"\n")
        cajerofile.write(str(lbl_cantbillete1saldo['text'])+"\n")
        cajerofile.write(str(lbl_cantbillete2saldo['text'])+"\n")
        cajerofile.close()
        volvermain(window)
        cargarcajero()

######################
#  Saldo del Cajero  #
######################
def saldocajero():
    global configurado
    if configurado == False:#en caso de no estar configurado no hace el proceso
        return
    window_main.state('withdrawn')
    window_saldocajero = tk.Toplevel(window_main)
    window_saldocajero.title('Saldo del Cajero')
    window_saldocajero.geometry("+650+355")
    window_saldocajero.resizable(False,False)
    window_saldocajero.protocol("WM_DELETE_WINDOW",lambda:volvermain(window_saldocajero))
    #ENTRADAS
    lbl_saldoanterior = tk.Label(window_saldocajero,text="ENTRADAS",font = ("Helvetica",14))
    lbl_saldoanterior.grid(row = 1,column = 3,columnspan =1)
    #DENOMINACIÓN-CANTIDAD-TOTAL
    lbl_denominacion = tk.Label(window_saldocajero,text="DENOMINACIÓN",font = ("Helvetica",14))
    lbl_denominacion.grid(row = 2,column = 1)
    lbl_cantidad = tk.Label(window_saldocajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 2)
    lbl_total = tk.Label(window_saldocajero,text="TOTAL",font = ("Helvetica",14))
    lbl_total.grid(row = 2,column = 4,columnspan = 1)
    #ABRE EL ARCHIVO DE LA CONFIGURACIÓN PARA LEER CONTENIDO
    configfile = open("configuración.dat","r")
    configlines = configfile.readlines()
    configfile.close()
    #ABRE EL ARCHIVO DEL CAJERO PARA LEER CONTENIDO
    cajerofile = open("cajero.dat","r")
    denominaciones = cajerofile.readlines()
    cajerofile.close()
    entradas = eval(denominaciones[4])
    #MONEDAS
    textmoneda1 = "Monedas de "+str(configlines[5])
    lbl_moneda1 = tk.Label(window_saldocajero,text= textmoneda1,font = ("Helvetica",13))
    lbl_moneda1.grid(row = 3,column = 1)
    cantmoneda1 = str(entradas[0])
    lbl_cantmoneda1anterior = tk.Label(window_saldocajero,text= cantmoneda1,font = ("Helvetica",13))
    lbl_cantmoneda1anterior.grid(row=3,column = 2)
    totalmoneda1anterior = str(int(entradas[0]) * int(configlines[5]))
    lbl_totalmoneda1anterior = tk.Label(window_saldocajero,text= totalmoneda1anterior,font = ("Helvetica",13))
    lbl_totalmoneda1anterior.grid(row =3,column = 4,columnspan = 1)
    ###
    textmoneda2 = "Monedas de "+str(configlines[6])
    lbl_moneda2 = tk.Label(window_saldocajero,text= textmoneda2,font = ("Helvetica",13))
    lbl_moneda2.grid(row = 4,column = 1)
    cantmoneda2 = str(entradas[1])
    lbl_cantmoneda2anterior = tk.Label(window_saldocajero,text= cantmoneda2,font = ("Helvetica",13))
    lbl_cantmoneda2anterior.grid(row=4,column = 2)
    totalmoneda2anterior = str(int(entradas[1]) * int(configlines[6]))
    lbl_totalmoneda2anterior = tk.Label(window_saldocajero,text= totalmoneda2anterior,font = ("Helvetica",13))
    lbl_totalmoneda2anterior.grid(row =4,column = 4,columnspan = 1)
    #TOTAL
    lbl_totalmonedasanterior = tk.Label(window_saldocajero,text = "TOTAL DE MONEDAS",font = ("Helvetica",14))
    lbl_totalmonedasanterior.grid(row = 5,column = 1)
    totalmonedas = str(int(entradas[0]) + int(entradas[1]))
    lbl_totalcantmonedasanterior = tk.Label(window_saldocajero,text = totalmonedas,font = ("Helvetica",13,"bold"))
    lbl_totalcantmonedasanterior.grid(row = 5,column = 2)
    totaltotalesmonedas = str(int(totalmoneda1anterior) + int(totalmoneda2anterior))
    lbl_totaltotalmonedasanterior = tk.Label(window_saldocajero,text = totaltotalesmonedas,font = ("Helvetica",13,"bold"))
    lbl_totaltotalmonedasanterior.grid(row = 5,column = 4,columnspan = 1)

    #BILLETES
    textbillete1 = "Billetes de "+str(configlines[7])
    lbl_billete1 = tk.Label(window_saldocajero,text= textbillete1,font = ("Helvetica",13))
    lbl_billete1.grid(row = 6,column = 1)
    cantbillete1 = str(entradas[2])
    lbl_cantbillete1 = tk.Label(window_saldocajero,text= cantbillete1,font = ("Helvetica",13))
    lbl_cantbillete1.grid(row=6,column = 2)
    totalcantbillete1 = str(int(entradas[2]) * int(configlines[7]))
    lbl_totalbillete1 = tk.Label(window_saldocajero,text= totalcantbillete1,font = ("Helvetica",13))
    lbl_totalbillete1.grid(row=6,column = 4,columnspan = 1)
    ###
    textbillete2 = "Billetes de "+str(configlines[8])
    lbl_billete2 = tk.Label(window_saldocajero,text= textbillete2,font = ("Helvetica",13))
    lbl_billete2.grid(row = 7,column = 1)
    cantbillete2 = str(entradas[3])
    lbl_cantbillete2 = tk.Label(window_saldocajero,text= cantbillete2,font = ("Helvetica",13))
    lbl_cantbillete2.grid(row=7,column = 2)
    totalcantbillete2 = str(int(entradas[3]) * int(configlines[8]))
    lbl_totalbillete2 = tk.Label(window_saldocajero,text= totalcantbillete2,font = ("Helvetica",13))
    lbl_totalbillete2.grid(row=7,column = 4,columnspan = 1)
    #TOTAL
    lbl_totalbilletesanterior = tk.Label(window_saldocajero,text = "TOTAL DE BILLETES",font = ("Helvetica",14))
    lbl_totalbilletesanterior.grid(row = 8,column = 1)
    totalbilletes = str(int(entradas[2]) + int(entradas[3]))
    lbl_totalcantbilletesanterior = tk.Label(window_saldocajero,text = totalbilletes,font = ("Helvetica",13,"bold"))
    lbl_totalcantbilletesanterior.grid(row = 8,column = 2)
    totaltotalesbilletes = str(int(totalcantbillete1) + int(totalcantbillete2))
    lbl_totaltotalbilletesanterior = tk.Label(window_saldocajero,text = totaltotalesbilletes,font = ("Helvetica",13,"bold"))
    lbl_totaltotalbilletesanterior.grid(row = 8,column = 4,columnspan = 1)
    ###
    #CARGA
    lbl_carga = tk.Label(window_saldocajero,text="SALIDAS",font = ("Helvetica",14))
    lbl_carga.grid(row = 1,column = 6)

    lbl_cantidad = tk.Label(window_saldocajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 5)
    lbl_total2 = tk.Label(window_saldocajero,text="TOTAL      ",font = ("Helvetica",14))
    lbl_total2.grid(row = 2,column = 7,columnspan = 1)
    #entrys monedas
    salidas = eval(denominaciones[5])
    lbl_salidas_moneda1 = tk.Label(window_saldocajero,text = salidas[0],font = ("Helvetica",13),width =10)
    lbl_salidas_moneda1.grid(row = 3,column = 5)
    lbl_salidas_moneda2 = tk.Label(window_saldocajero,text = salidas[1],font = ("Helvetica",13),width =10)
    lbl_salidas_moneda2.grid(row = 4,column = 5)
    #totales
    totalsalidasmoneda1 = str(int(salidas[0]) * int(configlines[5]))
    lbl_totalcantmoneda1carga = tk.Label(window_saldocajero,text = totalsalidasmoneda1,font = ("Helvetica",13))
    lbl_totalcantmoneda1carga.grid(row = 3,column = 7,columnspan = 1)
    totalsalidasmoneda2 = str(int(salidas[1]) * int(configlines[6]))
    lbl_totaltotalmoneda2carga = tk.Label(window_saldocajero,text = totalsalidasmoneda2,font = ("Helvetica",13))
    lbl_totaltotalmoneda2carga.grid(row = 4,column = 7,columnspan = 1)
    #total de todos
    totalcantmonedassalidas =  str(int(salidas[0]) + int(salidas[1]))
    lbl_totalcantmonedascarga = tk.Label(window_saldocajero,text = totalcantmonedassalidas,font = ("Helvetica",13,"bold"))
    lbl_totalcantmonedascarga.grid(row = 5,column = 5)
    totalmonedassalidas = str(int(totalsalidasmoneda1) + int(totalsalidasmoneda2))
    lbl_totaltotalmonedascarga = tk.Label(window_saldocajero,text = totalmonedassalidas,font = ("Helvetica",13,"bold"))
    lbl_totaltotalmonedascarga.grid(row = 5,column = 7,columnspan = 1)

    #entrys billetes
    lbl_salidas_billete1 = tk.Label(window_saldocajero,text = salidas[2],font = ("Helvetica",13),width =10)
    lbl_salidas_billete1.grid(row = 6,column = 5)
    lbl_salidas_billete2 = tk.Label(window_saldocajero,text = salidas[3],font = ("Helvetica",13),width =10)
    lbl_salidas_billete2.grid(row = 7,column = 5)
    #totales
    totalsalidasbillete1 = str(int(salidas[2]) * int(configlines[7]))
    lbl_totalcantbillete1carga = tk.Label(window_saldocajero,text = totalsalidasbillete1,font = ("Helvetica",13))
    lbl_totalcantbillete1carga.grid(row = 6,column = 7,columnspan = 1)
    totalsalidasbillete2 = str(int(salidas[3]) * int(configlines[8]))
    lbl_totaltotalbillete2carga = tk.Label(window_saldocajero,text = totalsalidasbillete2,font = ("Helvetica",13))
    lbl_totaltotalbillete2carga.grid(row = 7,column = 7,columnspan = 1)
    #total de todos
    totalcantbilletessalidas =  str(int(salidas[2]) + int(salidas[3]))
    lbl_totalcantbilletesanterior = tk.Label(window_saldocajero,text = totalcantbilletessalidas,font = ("Helvetica",13,"bold"))
    lbl_totalcantbilletesanterior.grid(row = 8,column = 5)
    totalbilletessalidas = str(int(totalsalidasbillete1) + int(totalsalidasbillete2))
    lbl_totaltotalbilletesanterior = tk.Label(window_saldocajero,text = totalbilletessalidas,font = ("Helvetica",13,"bold"))
    lbl_totaltotalbilletesanterior.grid(row = 8,column = 7,columnspan = 1)

    ###
    #SALDO
    lbl_saldo = tk.Label(window_saldocajero,text="SALDO",font = ("Helvetica",14))
    lbl_saldo.grid(row = 1,column = 10)
    lbl_cantidad = tk.Label(window_saldocajero,text="CANTIDAD",font = ("Helvetica",14))
    lbl_cantidad.grid(row = 2,column = 9)
    lbl_total = tk.Label(window_saldocajero,text="TOTAL",font = ("Helvetica",14))
    lbl_total.grid(row = 2,column = 11)
    #labels monedas
    saldomoneda1 = str(int(entradas[0] - int(salidas[0])))
    lbl_cantmoneda1saldo = tk.Label(window_saldocajero,text= saldomoneda1,font = ("Helvetica",13))
    lbl_cantmoneda1saldo.grid(row=3,column = 9)
    totalsaldomoneda1 = str(int(saldomoneda1) * int(configlines[5]))
    lbl_totalmoneda1saldo = tk.Label(window_saldocajero,text= totalsaldomoneda1,font = ("Helvetica",13))
    lbl_totalmoneda1saldo.grid(row =3,column = 11)
    saldomoneda2 = str(int(entradas[1] - int(salidas[1])))
    lbl_cantmoneda2saldo = tk.Label(window_saldocajero,text= saldomoneda2,font = ("Helvetica",13))
    lbl_cantmoneda2saldo.grid(row=4,column = 9)
    totalsaldomoneda2 = str(int(saldomoneda2) * int(configlines[6]))
    lbl_totalmoneda2saldo = tk.Label(window_saldocajero,text= totalsaldomoneda2,font = ("Helvetica",13))
    lbl_totalmoneda2saldo.grid(row =4,column = 11)
    #total monedas
    totalcantmonedassaldo = str(int(saldomoneda1)+int(saldomoneda2))
    lbl_totalcantmonedassaldo = tk.Label(window_saldocajero,text = totalcantmonedassaldo,font = ("Helvetica",13,"bold"))
    lbl_totalcantmonedassaldo.grid(row = 5,column = 9)
    totalmonedassaldo = str(int(totalsaldomoneda1) + int(totalsaldomoneda2))
    lbl_totaltotalmonedassaldo = tk.Label(window_saldocajero,text = totalmonedassaldo,font = ("Helvetica",13,"bold"))
    lbl_totaltotalmonedassaldo.grid(row = 5,column = 11)

    #labels billetes
    saldobillete1 = str(int(entradas[2] - int(salidas[2])))
    lbl_cantbillete1saldo = tk.Label(window_saldocajero,text= saldobillete1,font = ("Helvetica",13))
    lbl_cantbillete1saldo.grid(row=6,column = 9)
    totalsaldobillete1 = str(int(saldobillete1) * int(configlines[7]))
    lbl_totalbillete1saldo = tk.Label(window_saldocajero,text= totalsaldobillete1,font = ("Helvetica",13))
    lbl_totalbillete1saldo.grid(row =6,column = 11)

    saldobillete2 = str(int(entradas[3] - int(salidas[3])))
    lbl_cantbillete2saldo = tk.Label(window_saldocajero,text= saldobillete2,font = ("Helvetica",13))
    lbl_cantbillete2saldo.grid(row=7,column = 9)
    totalsaldobillete2 = str(int(saldobillete2) * int(configlines[8]))
    lbl_totalbillete2saldo = tk.Label(window_saldocajero,text= totalsaldobillete2,font = ("Helvetica",13))
    lbl_totalbillete2saldo.grid(row =7,column = 11)

    #total monedas
    totalcantbilletessaldo = str(int(saldobillete1)+int(saldobillete2))
    lbl_totalcantbilletessaldo = tk.Label(window_saldocajero,text = totalcantbilletessaldo,font = ("Helvetica",13,"bold"))
    lbl_totalcantbilletessaldo.grid(row = 8,column = 9)
    totalbilletessaldo = str(int(totalsaldobillete1) + int(totalsaldobillete2))
    lbl_totaltotalbilletessaldo = tk.Label(window_saldocajero,text = totalbilletessaldo,font = ("Helvetica",13,"bold"))
    lbl_totaltotalbilletessaldo.grid(row = 8,column = 11)

    btn_ok = tk.Button(window_saldocajero,text = "Ok",font = ("Helvetica",14),bg = "#2ded37",width = 8,
    command= lambda : volvermain(window_saldocajero))
    btn_ok.grid(row = 10,column = 2)

    window_saldocajero.mainloop()

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
    global lleno
    if configurado == False:#en caso de no estar configurado no hace el proceso
        return
    window_main.state('withdrawn')
    ventana_entradaVehiculo = tk.Toplevel(window_main)
    ventana_entradaVehiculo.title('Entrada de vehículo')
    ventana_entradaVehiculo.resizable(False,False)
    ventana_entradaVehiculo.protocol("WM_DELETE_WINDOW",lambda:volvermain(ventana_entradaVehiculo))
    ventana_entradaVehiculo.geometry("+700+400")

    #ABRE EL ARCHIVO DE LA CONFIGURACIÓN PARA LEER CONTENIDOS
    configfile = open("configuración.dat","r")
    configlines = configfile.readlines()
    configfile.close()
    #define la fecha actual
    now = datetime.now()
    horaentrada = now.strftime("%H:%M %d/%m/%Y ")

    #lee la cantidad de espacios ocupados
    parqueofile = open("parqueo.dat","rb")
    parqueo = pickle.load(parqueofile)
    espaciosusados = int(len(parqueo))
    parqueofile.close()

    espaciosdisponibles = str(int(configlines[3]) - espaciosusados)#saca los espacios disponibles

    if int(espaciosdisponibles) == 0:#valida si hay espacios disponibles
        lleno = True
        noespacios = tk.Label(ventana_entradaVehiculo,text = "NO HAY ESPACIO",font = ("Helvetica",20),fg = "red")
        noespacios.grid(row = 1,column = 3,sticky= W)

    lbl_espdisp = tk.Label(ventana_entradaVehiculo, text = 'Espacios disponibles:  '+ espaciosdisponibles, font= ("Helvetica",15))
    lbl_espdisp.grid(row = 1,column = 1, sticky= W)

    lbl_vacia = tk.Label(ventana_entradaVehiculo,text=" ")
    lbl_vacia.grid(row = 2,column = 1)

    lbl_suplaca = tk.Label(ventana_entradaVehiculo, text = 'Su placa:', font= ("Helvetica",15))
    lbl_suplaca.grid(row = 3,column = 1, sticky= W)

    ent_suplaca = tk.Entry(ventana_entradaVehiculo)
    ent_suplaca.grid(row = 3, column = 2)

    campo = 1
    while True:#busca el espacio asignado
        if campo not in parqueo:
            break
        campo+= 1

    lbl_campasig = tk.Label(ventana_entradaVehiculo, text = 'Campo asignado: '+str(campo), font= ("Helvetica",15))
    lbl_campasig.grid(row = 4,column = 1, sticky= W)

    lbl_horaent = tk.Label(ventana_entradaVehiculo, text = 'Hora de entrada: '+ horaentrada, font= ("Helvetica",15))
    lbl_horaent.grid(row = 5,column = 1, sticky= W)

    preciohora = configlines[1]
    lbl_preciohora = tk.Label(ventana_entradaVehiculo, text = 'Precio por hora:  '+preciohora, font= ("Helvetica",15))
    lbl_preciohora.grid(row = 6,column = 1, sticky= W)

    btn_ok = tk.Button(ventana_entradaVehiculo,text="Ok",font = ("Helvetica",15),bg ="#2ded37",
    command= lambda: asignarcampo(campo,ent_suplaca.get(),horaentrada,parqueo,ventana_entradaVehiculo))
    btn_ok.grid(row = 7, column= 1, sticky= E)
    btn_cancel = tk.Button(ventana_entradaVehiculo,text="Cancel",font = ("Helvetica",15), bg = "#f74343",
    command= lambda: ent_suplaca.delete(0,END))
    btn_cancel.grid(row = 7, column= 2, sticky= W)

    ventana_entradaVehiculo.mainloop()

#función para asignar campo a un vehículo según su placa
def asignarcampo(campo,placa,horaentrada,parqueo,ventana_entradaVehiculo):
    global lleno
    fileparqueo = open("parqueo.dat","wb")
    existe = False
    if placa != "" and lleno == False:
        if parqueo != {}:
            for espacio in parqueo:
                if placa == parqueo[espacio][0]:
                    existe = True
                    showerror("ERROR","¡La placa ya está registrada!")
                    pickle.dump(parqueo,fileparqueo)
                    fileparqueo.close()
            if existe == False:
                parqueo[campo] = [placa,horaentrada,"",0]
                pickle.dump(parqueo,fileparqueo)
                fileparqueo.close()
        else:#caso especial si el parqueo está vacío
            parqueo[campo] = [placa,horaentrada,"",0]
            pickle.dump(parqueo,fileparqueo)
            fileparqueo.close()
        #reinicia la ventana
        if existe == False:
            ventana_entradaVehiculo.destroy()
            entradaVehiculo()
    else:
        pickle.dump(parqueo,fileparqueo)
    fileparqueo.close()
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

def ponerinfo(placa):
    global lbl_hora_entrada
    global lbl_hora_salida
    global lbl_tiempo_cobrado
    global lbl_aPagar


    arch_parqueo = open('parqueo.dat', 'rb')
    parqueo = pickle.load(arch_parqueo)
    arch_parqueo.close()

    for placas in parqueo:
        if placa == parqueo[placas][0]:
            hora_entrada = str(parqueo[placas][1])
            existe = True
        else:
            existe = False


    if existe == True:
        lbl_hora_entrada.config(text = 'Hora de entrada '+ hora_entrada)
        lbl_hora_entrada.place(x =10, y =80)
        lbl_hora_salida.place(x = 10, y = 110)
        lbl_tiempo_cobrado.place(x = 10, y = 140)
        lbl_aPagar.place(x = 695, y = 215)
    else:
        messagebox.showerror('Aviso','Placa inexistente')

######################
# Cajero del Parqueo #
######################
def cajeroParqueo():
    window_main.state('withdrawn')
    ventana_cajeroParqueo = tk.Toplevel(window_main)
    ventana_cajeroParqueo.title('Cajero del Parqueo')
    ventana_cajeroParqueo.protocol("WM_DELETE_WINDOW",lambda:volvermain(ventana_cajeroParqueo))
    ventana_cajeroParqueo.geometry("870x530+500+250")

    configfile = open('configuración.dat', 'r')
    config = configfile.readlines()
    configfile.close()


    lbl_titulo = tk.Label(ventana_cajeroParqueo, text = 'Cajero del parqueo', font = ('Helvetica',15,'bold'))
    lbl_titulo.place(x = 10, y = 8)
                                                            #Global precio por hora
    lbl_precio_hora = tk.Label(ventana_cajeroParqueo, text= config[1][:-1]+ ' por hora', font = 'Helvetica 14')
    lbl_precio_hora.place(x =300, y =10 )

    lbl_su_placa = tk.Label(ventana_cajeroParqueo, text= 'Paso 1: Su placa', font = 'Helvetica 14')
    lbl_su_placa.place(x =10, y =50)
    ent_su_placa = tk.Entry(ventana_cajeroParqueo, font = 'Helvetica 14', width= 7)
    ent_su_placa.place(x =165, y =50)

    btn_buscar = tk.Button(ventana_cajeroParqueo, text= 'Buscar', font = 'Helvetica 11', bg = '#a9d4f5', command= lambda: ponerinfo(ent_su_placa.get()))
    btn_buscar.place(x = 250, y = 47)

    global lbl_hora_entrada
    lbl_hora_entrada = tk.Label(ventana_cajeroParqueo, text = 'Hora de entrada ', font = 'Helvetica 14')


    now = datetime.now()
    horasalida = now.strftime("%H:%M %d/%m/%Y ")
    global lbl_hora_salida
    lbl_hora_salida = tk.Label(ventana_cajeroParqueo, text = 'Hora de salida   '+horasalida,font = 'Helvetica 14')


    global lbl_tiempo_cobrado
    lbl_tiempo_cobrado = tk.Label(ventana_cajeroParqueo, text = 'Tiempo cobrado',font = 'Helvetica 14')

    lbl_paso2 = tk.Label(ventana_cajeroParqueo, text = 'Paso 2:  SU PAGO EN:  MONEDAS    BILLETES   TARJETA DE CRÉDITO',font = 'Helvetica 14' )
    lbl_paso2.place(x =10, y= 180)

    btn_moneda1 = tk.Button(ventana_cajeroParqueo, text = '50', font='Helvetica 12' ,bg= 'skyblue')
    btn_moneda1.place(x = 250, y = 220)
    btn_moneda2 = tk. Button(ventana_cajeroParqueo, text = '70', font='Helvetica 12' ,bg= 'skyblue')
    btn_moneda2.place(x = 250, y = 270)

    btn_billete1 = tk.Button(ventana_cajeroParqueo, text = '1000', font='Helvetica 12' ,bg= 'skyblue')
    btn_billete1.place(x = 356, y = 220)
    btn_billete2 = tk. Button(ventana_cajeroParqueo, text = '1000', font='Helvetica 12' ,bg= 'skyblue')
    btn_billete2.place(x = 356, y = 270)

    ent_tarj_cred = tk.Entry(ventana_cajeroParqueo, width=10, font = 'Helvetica 14', bd = 5)
    ent_tarj_cred.place(x = 490, y = 220 )

    lbl_paso3 = tk.Label(ventana_cajeroParqueo, text = 'Paso 3:  SU CAMBIO EN:  MONEDAS    BILLETES',font = 'Helvetica 14' )
    lbl_paso3.place(x =10, y= 350)

    lbl_moneda1 = tk.Label(ventana_cajeroParqueo, text = '0 de 50', font = 'Helvetica 14')
    lbl_moneda1.place(x =240, y= 380)
    lbl_moneda2 = tk.Label(ventana_cajeroParqueo, text = '0 de 100', font = 'Helvetica 14')
    lbl_moneda2.place(x =240, y= 410)

    lbl_billete1 = tk.Label(ventana_cajeroParqueo, text = '0 de 1000', font = 'Helvetica 14')
    lbl_billete1.place(x =355, y= 380)
    lbl_billete2 = tk.Label(ventana_cajeroParqueo, text = '0 de 1000', font = 'Helvetica 14')
    lbl_billete2.place(x =355, y= 410)

    lbl_titu_aPagar = tk.Label(ventana_cajeroParqueo, text = 'A pagar', font = 'Helvetica 15')
    lbl_titu_aPagar.place(x = 700, y = 180)

    global lbl_aPagar
    lbl_aPagar = tk.Label(ventana_cajeroParqueo, text = 'xxxx', bg ='#ff5252', font = 'Helvetica 16', width=7, height=2)

    lbl_titu_pagado = tk.Label(ventana_cajeroParqueo, text = 'Pagado', font = 'Helvetica 15')
    lbl_titu_pagado.place(x = 700, y = 290)
    lbl_pagado = tk.Label(ventana_cajeroParqueo, text = '0', bg ='#8efa9d', font = 'Helvetica 16', width=7, height=1)
    lbl_pagado.place(x = 695, y = 325)

    lbl_titu_cambio = tk.Label(ventana_cajeroParqueo, text = 'Cambio', font = 'Helvetica 15')
    lbl_titu_cambio.place(x = 700, y = 380)
    lbl_cambio = tk.Label(ventana_cajeroParqueo, text = '0', bg ='#8efa9d', font = 'Helvetica 16', width=7, height=1)
    lbl_cambio.place(x = 695, y = 415)



    btn_anular_pago = tk.Button(ventana_cajeroParqueo, text = 'Anular Pago', font = 'Helvetica 14', bg= '#fa7d7d')
    btn_anular_pago.place(x =20, y= 478)


    ventana_cajeroParqueo.mainloop()
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
activebackground=fondo,command = saldocajero)
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
activebackground=fondo,command = cajeroParqueo)
btn_cajeroparqueo.pack(pady= 6)

img7 = PhotoImage(file="images\img7.png")
btn_salidavehiculo = tk.Button(frameder,image =img7,bd = 0,bg = fondo,
activebackground=fondo,command = salidaVehiculo)
btn_salidavehiculo.pack(pady= 6)

img8 = PhotoImage(file="images\img8.png")
btn_ayuda = tk.Button(frameder,image =img8,bd = 0,bg = fondo,
activebackground=fondo,command = ayuda)
btn_ayuda.pack(pady= 6)

menubar = tk.Menu(window_main)
window_main.configure(menu = menubar)

menu = tk.Menu(menubar, tearoff = 0)
menubar.add_command(label ='Acerca de', command = lambda: showmensaje('Acerca de',
                        'Nombre del Programa: Parqueo\n''Fecha de creación: 21 de Junio 2022\n'
                        'Autor: Dominic José Casares Aguirre\n'
                        'Version 1.0')) #Opcion de acerca de
menubar.add_command(label ='Salir', command = window_main.destroy) #Salir


window_main.protocol("WM_DELETE_WINDOW",salir)#protocolo a la hora de salir del programa

window_main.mainloop()