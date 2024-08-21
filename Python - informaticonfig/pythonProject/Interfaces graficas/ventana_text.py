from tkinter import *

ventana = Tk()
ventana.geometry('550x550')
label_coment=Label(ventana,text='Comentarios',font=('Arial',14))
label_coment.grid(row=0,column=0)

text_coment = Text(ventana, font=('Consola',16))
text_coment.grid(row=1,column=0, padx=20,pady=15)
text_coment.config(width=30, height=20)
scrollvertical = Scrollbar(ventana,command=text_coment.yview())
scrollvertical.grid(row=1,column=1, sticky='nsew')
text_coment.config(yscrollcommand=scrollvertical.set)


ventana.mainloop()