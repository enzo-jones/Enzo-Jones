entrada = input("ingresar edad: ")

edad_ingresada = entrada.strip()
    
if edad_ingresada.isnumeric():
    edad = int(edad_ingresada)
    if edad > 0 and edad < 120:
        print(f"edad registrada: {edad}")
    else:
        print("error")

else:
    print("error")