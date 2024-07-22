
diccionarios = {
   "nombre" : 'Carlos',
   "apellido" : 'Morales' ,
   "sub"  :  '1000000'  
}

#nos devuelve un objeto 
claves =  diccionarios.keys()

print(claves)

# Obteniendo un elemento con get(no encuentra nada el programa continua)
valor = diccionarios.get('sub')

print(valor)

# elimina los elementos de un diccionario

#diccionarios.clear()
print(diccionarios.keys())

# eliminando un elemento del diccionario

diccionarios.pop('nombre')

print(diccionarios.keys())

#obteniendo un elemento cn item

diccionarip_iterable = diccionarios.items()

print(diccionarip_iterable)


