from tkinter import *

ventana= Tk()
ventana.geometry('300x500')

nombre_label = Label(ventana, text='Ingrese nombre', font=('Arial',16)).place(x=10,y=55)
campo_nombre = Entry(ventana, bg='yellow',bd=8, cursor='Arrow', font=('Consolas',14), fg='Brown')
campo_nombre.place(x=10,y=90)

clave_label =Label(ventana, text='Ingrese contraseña', font=('Arial',16)).place(x=10,y=140)
campo_clave = Entry(ventana,show='*',bg='yellow',bd=8, cursor='Arrow', font=('Consolas',14), fg='Brown')
campo_clave.place(x=10,y=175)
ventana.mainloop()