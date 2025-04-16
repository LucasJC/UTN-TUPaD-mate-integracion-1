#Se define la funcion de conversion a hexadecimal
def decimal_a_hexadecimal(numero_decimal):
    # definimos un string con todos los dígitos en su índice correspondiente
    caracteres_hexa = "0123456789ABCDEF"
    # si se ingresa 0 ya retornamos
    if numero_decimal == 0:
        return "0"
    numero_hexa = ""
    while numero_decimal > 0:
        # calculamos residuo de dividir por la base (16)
        residuo = numero_decimal % 16
        # determinamos el caracter hexa correspondiente al residuo que está en decimal
        caracter_hexa = caracteres_hexa[residuo] # el residuo es el índice del caracter hexa en el string 'hex_chars'
        # concatenamos el caracter al inicio del string de resultado
        numero_hexa = caracter_hexa + numero_hexa
        # reemplazamos el valor de decimal con el valor entero de la división por la base
        numero_decimal //= 16
    # retornamos el string resultante, ya en hexadecimal
    return numero_hexa

#Se le pide al usuario que ingrese el numero que desea convertir
numero = int(input("Ingrese un numero para convertir: "))
#Se ejecuta la funcion de conversion, utilizando el input del usuario
resultado = decimal_a_hexadecimal(numero)
#Se muestra en pantalla el resultado de la conversion. 
print(f"El resultado en Hexadecimal es: {resultado}")