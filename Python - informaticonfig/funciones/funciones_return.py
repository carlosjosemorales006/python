
# Funcion calacular area de un triangulo

'''def triangulo(base,altura):
    area = base * altura
    return area

base = int(input('Ingrese la Base: '))
altura = int(input("Ingrese la altura: "))

print('El area del triangulo es: ', triangulo(base,altura))'''


# Funcion calcular mayor valor
def mayor_valor(valor1,valor2):
    if valor1 > valor2:
        mayor= valor1
    else:
        mayor = valor2
    return mayor

# bloque principal

v1 = int(input('Ingresa el primer valor'))
v2 = int(input('Ingresa el segundo valor'))

print('El mayor valor es: ', mayor_valor(v1,v2))



