

ingreso_mensual = 110000
gastos_mensuales = 8000
if ingreso_mensual > 10000:
    if gastos_mensuales < 7000:
        print('Ahora estas bien')
    else:
        print("Estas gastando demasiado")
elif ingreso_mensual > 1000:
    print('Estas bien en latinoamerica')
elif ingreso_mensual > 500:
    print('Estas bien en Republica Dominicana')
else:
    print('Eres pobres')
