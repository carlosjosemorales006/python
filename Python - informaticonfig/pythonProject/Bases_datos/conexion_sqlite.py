import sqlite3


conexion = sqlite3.connect('Base1')

cursor01 = conexion.cursor()
# cursor01.execute('''create table usuarios(
#     nombre varchar(20),
#     edad int,
#     direccion varchar(50),
#     telefono numerix(10))''')

#cursor01.execute("insert into usuarios values('Carlos Morales',32,'Calle 1ra Villa hermosa',3458767890)")


mas_usuarios =[
    ('Pedro',34,'Calle 2da No 55',82547896),
    ('Juan',42,'Calle 3da No 55',854547896),
    ('Luas',35,'Calle 4da No 55',215651221)
]

cursor01.executemany('insert into usuarios values(?,?,?,?)',mas_usuarios)
conexion.commit()
conexion.close()