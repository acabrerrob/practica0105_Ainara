cantidad= int (input('Introduzca la cantidad de capital a invertir'))
interes= int (input('Introduzca el porcentaje de interes anual'))
años= int (input('Introduzca el número de años que quiere que dure su inersión'))

while años>0  :
    capital=(cantidad+((interes*cantidad)/100))
    print('Su capital obtenido en el año',años,'es de:',capital)
    cantidad=capital
    años=años-1
    
