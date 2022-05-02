#Programa que invierte el orden de un numero de 5 dígitos
#Entrada de datos
numero = int(input('Ingrese un numero de 5 digitos: '))
#Operacion
invertido = numero % 10 * 10000 + numero % 100 // 10 * 1000 + numero % 1000 // 10 * 100 + numero % 10000 // 10 * 10 + numero // 10000
#salida de datos
print('El numero invertido es: ', invertido)
#
