def multiplication(nombre):
    try:      # si conversion error
        nombreint = int(nombre)
    except ValueError:
        nombre = input("Vous devez entre un nombre  : ")  # demande nombre
        return multiplication(nombre)
    for i in range(1, 11):
        print(f"{nombreint} * {i} = {nombreint*i}")


nombre = input("un nombre en multiplier : ")  #demande nombre
multiplication(nombre) #appel de fonction