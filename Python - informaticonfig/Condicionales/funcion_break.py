
# break, detiene la iteracion de un bucle
'''for letra in 'programacon':
    print(letra)
    if letra == 'm':
        break
    
print('Letra encontrada', letra, 'Fin del bucle')'''

'''conteo = 10

while conteo > 0:
    print('Conteo en: ', conteo)
    conteo -= 1
    if conteo == 5:
        break #aqui sale del bucle
    
print('Fin del conteo')'''

# continue salta una iteracion

for letra in 'prograemacion':
    if letra == 'e':
        print('Letra erronea!')
        continue #continua hasta el fin del bucle
    print(letra)
print('Fin del bucle')
    