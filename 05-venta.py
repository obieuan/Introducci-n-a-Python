#Hallar el IGV(18%) y el precio total de un producto

print('Hallar el IGV(18%) y el precio total de un producto')
#Entrada de datos
precio = float(input('Ingrese el precio del producto: '))
#Operacion
igv = precio * 0.18
precio_total = precio + igv
#salida de datos
print('='*50)
print('--- Factura ---')
print('='*50)
print('Precio del producto: ', precio)
print('IGV: ', igv)
print('Precio total: ', precio_total)
print('='*50)
print('Gracias por su compra')
print('='*50)
#


