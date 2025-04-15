#Se define la funcion de conversion a hexadecimal
def decimal_a_hexadecimal(decimal):
    hex_chars = "0123456789ABCDEF"
    if decimal == 0:
        return "0"
    hexadecimal = ""
    while decimal > 0:
        hexadecimal = hex_chars[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal
#Se le pide al usuario que ingrese el numero que desea convertir
numero = int(input("Ingrese un numero para convertir: "))
#Se ejecuta la funcion de conversion, utilizando el input del usuario
resultado = decimal_a_hexadecimal(numero)
#Se muestra en pantalla el resultado de la conversion. 
print(f"El resultado en Hexadecimal es: {resultado}")