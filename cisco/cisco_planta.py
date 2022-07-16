import os
os.system ("cls")
a=2
a=str(input('ingresa una flor: '))
b='ESPATAFILIO'
c= 'espatafilio'

if (a!=b and a!=c) :
    print('¡ESTAPAFILIO!, ¡NO',a,'!')
elif(a!=b or a==c):
    print ('NO, ¡quiero un gran ESTAPAFILIO!')
else:
    print('Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!')

