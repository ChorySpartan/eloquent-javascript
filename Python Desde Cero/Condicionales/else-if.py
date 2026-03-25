ingreso_mensual = 12000
gasto_mensual = 120000
result = ingreso_mensual - gasto_mensual

# if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 7000:
        print("Estás bien económicamente en cualquier parte del mundo")
    elif ingreso_mensual - gasto_mensual < 0:
        print(f"Estás en déficit {result}")
    else:
        print("Estás malgastando tu dinero")

elif ingreso_mensual > 1000:
    print("Estás bien económicamente en latinoamérica")

else:
    print("Sos pobre")