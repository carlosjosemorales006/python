import sys
from tkinter import *

Ventana = Tk()

Ventana.geometry('500x500')

label_mensaje = Label(Ventana,text='Desea mostrar saludo?', font=('Verdana',18))
label_mensaje.place(x=10,y=20)

def saludos():
    label_mensaje.config(text='Hola a Todos')

boton_aceptar = Button(Ventana,text='ACEPTAR', command=saludos)
boton_aceptar.config(width=10, height=3)
boton_aceptar.place(x=10, y=70)

def cancelar():
    sys.exit()

boton_cancelar = Button(Ventana, text='CANCELAR', command=cancelar)
boton_cancelar.config(width=10, height=3)
boton_cancelar.place(x=110,y=70)



Ventana.mainloop()
