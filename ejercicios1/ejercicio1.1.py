

# promedio de duarciones

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5


# Duracion de crudo

crudo_promedio = 5
crudo_dalto = 3.5

# diferencias de duraciones

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min *100)
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max /10)
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio *100)

# Calculando el promedio de tiempo vacio

tiempo_vacio_primedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10


print(f'El curso de Dalto dura un {diferencia_con_min} % menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max} % menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio} % menos que el promedio')
