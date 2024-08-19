
from tkinter import *

ventana = Tk()
ventana.option_add('*Font','Verdana 14')

barramenu = Menu(ventana)
ventana.config(menu = barramenu, width=600, height=400)
#----------------------------------------------------

menuarchivo = Menu(barramenu, tearoff=0)
menuarchivo.add_command(label='Nuevo')
menuarchivo.add_command(label='Abrir')
menuarchivo.add_command(label='Guardar')
menuarchivo.add_command(label='Guardar como..')
menuarchivo.add_separator()
menuarchivo.add_command(label='Cerrar')
barramenu.add_cascade(label='Archivo', menu=menuarchivo)

#--------------------------------------------------------------

menuedit = Menu(barramenu,tearoff=0)
menuedit.add_command(label='Cortar')
menuedit.add_command(label='Pegar')
menuedit.add_command(label='Imprimir')
barramenu.add_cascade(label='Editar', menu=menuedit)

#---------------------------------------------------------------

menuayuda = Menu(barramenu,tearoff=0)
menuayuda.add_command(label='Soporte')
menuayuda.add_command(label='Actualizaciones')
menuayuda.add_command(label='Acerca de..')

barramenu.add_cascade(label='Ayuda',menu=menuayuda)


ventana.mainloop()

