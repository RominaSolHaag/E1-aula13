import os
os.system('cls')
palabra_secreta= 777
print("Bienvenido al juego de adivinador")

def ingresa_numero():
    numero=int(input("Ingrese un numero: "))
while palabra_secreta != ingresa_numero():
    print("Estas en mi bucle maldito muggle")
    numero=int(input("Ingresa nuevamente un numero: "))
    print ("saliste")
    break

    
