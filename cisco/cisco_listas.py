import os
os.system ('cls')

"""lista= [1,2,3,4,5,6,7]
lista[0]=10
print(lista)

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

my_list = [1, 1, 1, 1, 1]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

beatle=[]
beatle.append("john l.")
beatle.append("paul m")
beatle.append("geoge h")
print("estos son los ", beatle)

cantidad=int(input("ingrese la cantidad: "))

for i in range(cantidad):
    cantantes=input("ingrese los nombres:\n")
    beatle.append(cantantes)
print(beatle)

del beatle[4], beatle[3]
print(beatle)

beatle.insert(0,"ringo star")
print(beatle)

my_list = [8, 10, 6, 2, 4]  # lista a ordenar

my_list.sort()

noentiendo = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

print (my_list)

while noentiendo:
    noentiendo = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            noentiendo = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = []
coincidencia = 0
for number in bets:
    if number in drawn:
        hits.append(number)
        coincidencia+=1

print(hits)
print(coincidencia)
"""
def perdido():
    return 

perdido()
print(perdido())