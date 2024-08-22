import psycopg2

try:
    conexion = psycopg2.connect(database='Base_prueba',user='postgres', password='carlenys@123')
    cursor01 = conexion.cursor()
    cursor01.execute('select version()')
    version= cursor01.fetchone()
except Exception as err:
    print('Error al conectar a la base',err)
else   :
    print(version)

# try:
#     cursor01.execute("insert into usuarios values(1,'Carlos Morales','admin123')")
# except Exception as err:
#     print('Error al insertar datos',err)
# else:
#     print('Datos ingresados correctamente')
#
# conexion.commit()
cursor01.execute('select * from usuarios')
consulta = cursor01.fetchone()

print(consulta)
conexion.close()