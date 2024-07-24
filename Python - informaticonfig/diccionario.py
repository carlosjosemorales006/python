# Creando diccionarios

''''paises = {
    'Republica Dominicana':'Santo Domingo', 
    'Argentina': 'Buenos Aires',
    'Colombia':'Bogota',
    'España': 'Madrid'}

print(paises)

def dic_paises(paises):
    for capital in paises:
        print(capital,':',paises[capital])

dic_paises(paises)'''

def carga_productos():
    productos={}
    for f in range(3):
        nombre=input('Ingrese el nombre del producto:')
        precio = int(input('Ingrese el precio del producto:'))
        productos[nombre]=precio
        
    return productos

def imprime(productos):
    print('Listado de productos')
    for nombre in productos:
        print(nombre, productos[nombre])
        
articulos = carga_productos()

imprime(articulos)