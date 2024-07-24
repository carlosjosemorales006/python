import time, calendar

tiempo = time.localtime()

print('El año es : ', tiempo.tm_year)

print('El mes es : ', tiempo.tm_mon)

print('El dia es: ', tiempo.tm_mday)

print('La hora es: ', tiempo.tm_hour,tiempo.tm_min, tiempo.tm_sec)

# ver la fecha actual 
fecha_hora = time.asctime(time.localtime(time.time()))
print('Tiempo local: ', fecha_hora)

calendario = calendar.month(2024,7)


print(calendario)

