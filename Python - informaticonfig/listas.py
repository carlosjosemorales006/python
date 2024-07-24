

lista_enteros = [1,2,3,4,5]

lista_letras = ['a','c','d','e']

materias = ['Fisica','Matematicas','edu']

precios = [50,20,10,30,100,50,40,10]

'''print(lista_enteros[0])
print(lista_letras[1:5])
print(materias[:2])
print(precios[-3:])'''

# agregar un elemento al final de la lista
lista_letras.append('h')
print(lista_letras)

# Eliminar elementos por indixe
del lista_letras[2]
print(lista_letras)

# unir dos listas
print([1,2,3] + [2,3,4] )

# multiplicacion de lista 

print(['hola'] * 4)
print([1,2,3] * 4)

# validar si hay un elemento de una lista

print('a' in ['a', 'b'])

# cuenta los elements en la lista
print(len(lista_letras))

# nos dice cual es el mayor valor de una lista
print(max(precios))

# nos dice cual es el menor valor de una lista
print(min(precios))

# nos dice cuantas veces esta un elemento en una lista
print(precios.count(10))

# agrega elementos separados por coma
materias.extend('Ingles')
print(materias)

# elimina un elemento por indixe
precios.pop(2)
print(precios)

# elimina un elemento por valor
precios.remove(10)
print(precios)

lista_letras.reverse()


for f in lista_enteros:
    print(f, end=',')





