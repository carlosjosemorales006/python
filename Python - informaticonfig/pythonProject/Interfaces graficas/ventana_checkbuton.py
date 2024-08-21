from tkinter import *

ventana = Tk()
ventana.title('Menu')
ventana.geometry('400x600')
ventana.resizable(width=False, height=False)

img_menu = PhotoImage(file='comida.png')
Label(ventana,image=img_menu).place(x=140, y=25)

label1 = Label(ventana, text='Elije tu combo', font=('Arial',16)).place(x=135,y=200)

hamburguesa=IntVar()
papas=IntVar()
nuggets=IntVar()
sodas = IntVar()
helados = IntVar()

def combo():
    opciones=''
    if hamburguesa.get()==1:
        opciones+='hamburguesa\n'
    if papas.get()==1:
        opciones+='papas\n'
    if nuggets.get()==1:
        opciones+='nuggets\n'
    if sodas.get()==1:
        opciones+='sodas\n'
    if helados.get()==1:
        opciones+='helados\n'
    
    label2.config(text='Su ORDEN:\n' + opciones, font=('Verdana',14))
        


Checkbutton(ventana, text='HAMBURGUESA', variable=hamburguesa, onvalue=1, command=combo).place(x=10, y=250)
Checkbutton(ventana, text='PAPAS', variable=papas, onvalue=1, command=combo).place(x=10,y=275)
Checkbutton(ventana,text='NUGGETS',variable=nuggets, onvalue=1, command=combo).place(x=10,y=300)
Checkbutton(ventana, text='SODA',variable=sodas, onvalue=1, command=combo).place(x=10, y=325)
Checkbutton(ventana,text='Helados',variable=helados, onvalue=1, command=combo).place(x=10, y=350)

label2 = Label(ventana)
label2.place(x=130,y=390)





ventana.mainloop()