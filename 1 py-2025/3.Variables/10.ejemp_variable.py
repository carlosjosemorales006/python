# Declaracion de variables

edad = 32
altura = 5.6
pais = 'Republica Dominicana'

# Aceder a la varibales
print("Valores iniciales: ")
print(f'mi edad es: {edad} ')
print ('Mi altura es:', altura, 'pie')
print('mi pais de nacimineto es:', pais)

# Modificar el valor de una variable
edad = 33
altura = 5.7

print("------------------------------------------")
print("Valores modificados ")
print(f'mi edad es: {edad} ')
print ('Mi altura es:', altura, 'pie')
print('mi pais de nacimineto es:', pais)

# En Pytho el tipo es dinamico 

edad = "Treinta y dos"

print(f'mi edad es: {edad} ')

# No podemos acceder a una variable no declarada, presenta un error en Python
telefono = '809-550-4510'
print('Telefono:', telefono)