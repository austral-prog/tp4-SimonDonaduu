def leap_year():
    año = int(input("Ingrese un año: "))
    cent = año % 400
    año1 = año % 4
    if año1 == 0 and cent == 0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
#leap_year()

    




