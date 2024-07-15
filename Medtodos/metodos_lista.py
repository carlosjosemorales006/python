


#creando una lista con List
lista = list([38,31])

cadena = 'hola'
#devuelve la cantidad de elementos en una lista
resultado = len(lista)

print(resultado)

# agregando un elementos a la lista con appen

lista.append(50)

print(lista)

# agregando un elementos a la lista con insert en un indixe especifico

lista.insert(0,'croot')

print(lista)

# agregando varios elementos a la lista

lista.extend([35,80])

print(lista)

# eliminando un elemento de la lista por su indice

lista.pop(0)

print(lista)

# elimina un elemento por su valor

lista.remove(31)

print(lista)

#eleimina todos los elements de la lista 

#lista.clear()
print(lista)

# ordenar la lista asendentemente

lista.sort()
print(lista)

# ordenando en reversa

lista.sort(reverse=True)

print(lista)

# invirtiendo los elemento con reverse

lista.reverse()
print()

print(dir(lista))

