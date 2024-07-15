
cadena1 = 'Hola soy Carlos'
cadena2 = 'Bienvanidos parceros'
cadena3= '5'


#print(dir(cadena1))
#print(dir(4))
# Metodos de la funcion dir


# convertir un texto a mayucula
print(cadena1.upper())
#convertir un texto a minuscula
print(cadena1.lower())
#convertir la primera letra a mayuscula 
print(cadena1.capitalize())
#Buscar una cadena en otra cadena
busqueda_find = cadena1.find('s')
print(busqueda_find)

#busqueda_find = cadena1.index('s')
#print(busqueda_find)


# si es numerico dvuelve true
numero = 55
es_numerico = cadena3.isnumeric()

# nos dice que cantidad de veces aparece una cadena
print(cadena1.count('a'))

# nos cueenta las cantidad de caracteres en una cadena
print(len(cadena1))

# verifica si una cadena empieza con una letra en especifico

print(cadena1.startswith('Hola'))

# verificar si termina con una letra

print(cadena1.endswith('Carlos'))

# remplazar una cadena por otra

cadena_nueva = cadena1.replace(',','Hola mundo')

print(cadena_nueva)

# separar cadena con la cadena que le pasemos, ace una lista

print(cadena1.split(','))

