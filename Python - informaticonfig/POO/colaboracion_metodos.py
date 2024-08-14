
class Operaciones:
    
    def __init__(self) -> None:
        self.valor1 = int(input('Ingrese el primer valor'))
        self.valor2 = int(input('Ingrese el segundo valor'))
        self.sumar()
        self.restar()
        self.multiplicar()
    
    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma es: ", suma)
        
    def restar(self):
        resta = self.valor1 - self.valor2
        print("La diferencia es: ", resta)
        
    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print("EL producto es: ", multi)
        
        
resultado = Operaciones()
