import sys
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile

ventana = Tk()
ventana.geometry('500x500+500+130')

def acercade():
    messagebox.showinfo('MI SOFTWARE','Sistema de procesos informaticos')

def abrir():
    filedialog.askopenfile(initialfile='',filetypes=(('Ficheros Excel','*.xlsx'),
                            ('Ficheros de texto','*.txt'   ),('Todos los archivos','*.*')))
def guardar():
    f = asksaveasfile(mode='w',defaultextension='.txt')
    f.close()
def actualiza():
    messagebox.showwarning('Actualzacion','''Actualizacion disponible
    debe actualizar el sistema
    visite: www.misistema.com''')

def salir():
    seleccionar = messagebox.askokcancel('Salir','Desea salir de la aplicacion?')
    if seleccionar == True:
        ventana.destroy()

def cierradoc():
    seleccion=messagebox.askretrycancel('Reintentar','Error en cierre de archivo')
    if seleccion == False:
        ventana.destroy()


barramenu = Menu(ventana)
ventana.config(menu = barramenu, width=600, height=400)
#----------------------------------------------------

menuarchivo = Menu(barramenu, tearoff=0)
menuarchivo.add_command(label='Nuevo')
menuarchivo.add_command(label='Abrir',command=abrir)
menuarchivo.add_command(label='Guardar', command=guardar)
menuarchivo.add_command(label='Guardar como..')
menuarchivo.add_separator()
menuarchivo.add_command(label='Cerrar',command=cierradoc)
menuarchivo.add_command(label='Cerrar todos',command=salir)
menuarchivo.add_command(label='Salir',command=salir)
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
menuayuda.add_command(label='Actualizaciones', command=actualiza)
menuayuda.add_command(label='Acerca de..',command=acercade)

barramenu.add_cascade(label='Ayuda',menu=menuayuda)


ventana.mainloop()

