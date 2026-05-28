codigo = input("escribir codigo en base a este formato [PROG-101]" )
if codigo.count('-') != 1:
    print("error: el codigo solo puede tener un (-)")
partes = codigo.split('-')
parte_izquierda = partes[0]
parte_derecha = partes[-1]
if not parte_derecha.isdigit():
    print("error: el codigo solo puede tener letras en la parte izquierda")

if not parte_izquierda.isalpha():
    print("error: el codigo solo puede tener numeros en la parte derecha")
else:
    print(f"codigo valido: {codigo}")   
    