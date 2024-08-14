

class auto:
    def __init__(self,marca,color,ruedas) -> None:
        self.marca = marca
        self.color =color
        self.ruedas = ruedas
        


class caracteristicas:
    def __init__(self) -> None:
        self.vehiculo = auto('Toyota','Azul',4)
        print("Datos del vehiculo")
        print('Marca: ', self.vehiculo.marca, '\nColor ', self.vehiculo.color,
              '\nRuedas ', self.vehiculo.ruedas)
        if self.vehiculo.ruedas == 1:
            print('El vehiculo es un monociclo')
        elif self.vehiculo.ruedas == 2:
            print("El vehiculo es una moto")
        elif self.vehiculo == 3:
            print("El vehiculo es un triciclo")
        elif self.vehiculo.ruedas == 4:
            print('El vehiculo es un auto')
        elif self.vehiculo.ruedas >= 4:
            print("El vehiculo es un camion")
            
            
objeto = caracteristicas() 