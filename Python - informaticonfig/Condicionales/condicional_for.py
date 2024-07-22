

'''for i in range(10):
    print('valor de i: ', i)
    
# Ejemplo del bucle while

f= 0

while f<10:
    print('valor de f: ', f)
    
    f += 1
    
    
for f in range(20,30,2):
    print('Valor de f es: ', f)
print('fin del ciclo')

suma = 0

for f in range(2):
    valor=int(input('Ingrese valor: '))
    suma += valor
print('La suma es: ',suma)

promedio = suma / 2

print('El promedio es: ', promedio)

for i in "Python":
    print(i, end="")'''
    
# control del signo @
    
'''arroba = "@"

cantidad = 0

mail = input('Ingrese su mail: ')

for f in mail:
    if f == arroba:
        cantidad += 1

if cantidad >= 1:
    print('Mail correcto')
else:
    print("Mail incorrecto")'''
    
    
    
valor = int(input('Elije una table: '))
print('elijio ver la tabla del: ', valor)

for i in range(1,12):
    resultado = valor * i
    print(f'{valor} X {i} = {resultado}') 