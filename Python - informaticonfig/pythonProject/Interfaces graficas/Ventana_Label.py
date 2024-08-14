from tkinter import *

ventana = Tk()

ventana.geometry('300x400')
etiqueta =Label(ventana,text='Linea de texto',fg='blue', font=('Verdana',18))
etiqueta.place(x=100, y=200)
img=PhotoImage(file='pajaro.jpg')
Label(ventana,image=img).place(x=10,y=0)

ventana.mainloop()