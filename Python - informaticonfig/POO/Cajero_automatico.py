
class Cajero:
    monto = 5000
    print('Bienvenido a su cajero automatico')
    
    def operaciones(self):
        self.opciones = int(input('''
        -------------------------------------------------
        POR FAVOR INDIQUE QUE OPERACION DESEA REALIZAR
        -------------------------------------------------
        1. CONSULTAR BALACE
        2. DEPOSITO A CUENTA
        3. RETIRO DE EFECTIVO
        4. SALIR '''))
        
        self.control = 0
        while self.control == 0:
            if self.opciones == 1:
                self.consultabalance()
            elif self.opciones == 2:
                self.depositar()
            elif self.opciones == 3:
                self.retirar()
            elif  self.opciones == 4:
                self.salir()
            else:
                print('LO SENTIMOS OPCION NO VLIDA, INTENTE DE NUEVO: ')
                self.operaciones()    
            
    
        
    def consultabalance(self):
        print('Su balance disponible es: ', self.monto)
        print('DESEA REALIZAR OTRO OPERACION: ')
        self.operaciones()
    
    def depositar(self):
        self.deposito = int(input('INDIQUE LA CANTIDAD A DEPOSITAR: '))
        self.monto += self.deposito
        self.consultabalance()
       
    def retirar(self):
        self.retiro = int(input('INDIQUE EL MONTO QUE DESEA RETIRAR: '))
        self.control = 0
        while self.control == 0:
            if self.retiro > self.monto:
                print('''USTED NO CUENTA CON FONDOS SUFICIENTES
                      POR FAVOR INTENTE DE NUEVO
                      ------------------------------------------''')
                self.retirar()
            elif self.retiro <= self.monto:
                self.monto -= self.retiro
                self.control =1
                print('CANTIDAD RETIRADA: ', self.retiro) 
                self.consultabalance()

        
        
        
    
    def salir(self):
        print('GRACIAS POR PREFERIRNOS...')
        self.control = 1
        
          
ejecucion = Cajero() 

ejecucion.operaciones()