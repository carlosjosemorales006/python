

class Software:
    def __init__(self) -> None:
        self.sistema_operativo = input('Indique su S.O:')
        self.arquitectura = int(input('Ingrese la arquitectura: '))
    def info(self):
        print(f'Sistema Operativo: {self.sistema_operativo}  ')
        print(f'Arquitectura: {self.arquitectura}  ')
        
class Base(Software):
    def __init__(self) -> None:
        super().__init__()
        self.procesador  = input('Indique el procesador: ')
        print('_____________________________________')
        
    def imprime(self):
        print('Proceador: ', self.procesador)
        
        
pc1 = Base()

pc1.info()
pc1.imprime()