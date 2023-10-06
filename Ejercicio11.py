deposito= float (input('Introduzca el dinero a depositar '))

primerAño= round(deposito + deposito*0.04,2)
segundoAño= round(primerAño + primerAño * 0.04,2)
tercerAño= round(segundoAño + segundoAño * 0.04,2)

print('El depósito tras el primer año es: ',primerAño,'€')
print('El depósito tras el segundo año es: ',segundoAño,'€')
print('El depósito tras el tercer año es: ',tercerAño,'€')