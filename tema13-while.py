
cont = 0

while cont<10:
    print(cont)
    cont+=1



numero =int(input("Introduce el numero a multiplicar: "))




def mult(num):
 cont = 1
 while cont<11:
    print("{} x {} = {}".format(num,cont,(num*cont)))
    cont+=1

mult(numero)