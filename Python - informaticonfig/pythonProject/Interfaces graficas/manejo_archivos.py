#mi_archivo = open('archivo.txt','w')
#texto = '''
#Estamos aprendiendo a generar archivo de texto con Python,
#ultilizando la heramienta ptcharm.
#'''
#mi_archivo.write(texto)

leectura = open('archivo.txt', 'r')
textor= leectura.read()



#mi_archivo.close()
leectura.close()

print(textor)

