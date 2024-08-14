from tkinter import *

ventana = Tk()
ventana.geometry('300x400')
labae1= Label(ventana, text='Indique su lenguaje favorito: ', font=('Arial',14))
labae1.place(x=10,y=20)
label2 = Label(ventana, font=('Arial', 16))
label2.place(x=10,y=150)

def lenguajes():
    if seleccion.get()==1:
        label2.config(text='Seleccionaste Python')
    elif seleccion.get()==2:
        label2.config(text='Selecionaste Java ')
    elif seleccion.get()==3:
        label2.config(text='Selecionaste C#')

seleccion = IntVar()
seleccion.set(3)

img= PhotoImage(file=r'C:\Users\adminsimag\Documents\GitHub\python\Python - informaticonfig\pythonProject\Interfaces graficas\piton.png')
img2= PhotoImage(file=r'C:\Users\adminsimag\Documents\GitHub\python\Python - informaticonfig\pythonProject\Interfaces graficas\java.png')
img3= PhotoImage(file=r'C:\Users\adminsimag\Documents\GitHub\python\Python - informaticonfig\pythonProject\Interfaces graficas\c#.png')

radio1 = Radiobutton(ventana, text='Python', variable=seleccion, value=1, command=lenguajes,image=img)
radio1.place(x=10, y=60)

radio2 = Radiobutton(ventana, text='JAVA', variable=seleccion, value=2, command=lenguajes,image=img2)
radio2.place(x=10,y=90)

radio3 = Radiobutton(ventana, text='C#', variable=seleccion,value=3, command=lenguajes,image=img3)
radio3.place(x=10, y=120)






ventana.mainloop()