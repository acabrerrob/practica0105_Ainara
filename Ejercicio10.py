payasos= int (input('¿Cuantos payasos hay en el pedido? '))
muñecas= int (input('¿Cuantas muñecas hay en el pedido? '))
contador=0

if(payasos>0):
    contador += payasos*112

if(muñecas>0):
    contador += muñecas*75

print('El peso total del paquete es de: ',contador,'g ')