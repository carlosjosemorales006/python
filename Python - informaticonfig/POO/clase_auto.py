
class auto:
    #El metodo principal de una clase (metodo constructor)
    def __init__(self):
        #la variable en una clases inician con self (se les llama atributo)
        self.marca = 'BMW'
        self.puertas = 4
        self.color = 'color'
        self.peso = 800
    #los metodos deben llevar el argumento self 
    def funciones(self):
        self.enciende = True
        self.arranca = True
        self.acelera = True
        self.frena = True 
    
    def datos(self):
        print('Marca del aunto: ', self.marca, '\nPuertas: ',self.puertas,
              '\nColor: ',self.color,'\nPesos: ',self.peso,'kg')
  
#creacion de objeto      
mi_auto = auto()

mi_auto.datos()