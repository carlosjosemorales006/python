
# Listas

lista = ['Carlos Morales','crot',False,1.8]

lista[2] = 'Casado'

print(lista[2])


# Tuplas
 
tuplas=('Carlos Morales','crot',False,1.8)
 
#tuplas[2]='juan' las tuplas no se pueden modificar


# creando un conjunto (set)
# podimos redefinirlos, pero no modificar elementos

conjunto = {'Juan',5,'pedro'}
# no muestra elementos duplicados
#no se acede a los elementos por indixe
conjunto = {5,10,11,11}

print(conjunto)

# creando un diccionario

diccionario = {
    'nombre':'Carlos Morales',
    'edad' : 31,
    'casado' : True   
}

print(f'mi nombre es {diccionario['nombre']}')
 
 