
def main():
 opcion = 0

 while opcion <= 4:

  print("elije una opcion")
  print("(1)sumar")
  print("(2)restar")
  print("(3)multiplicar")
  print("(4)dividir")
  print("(5)Salir")

  opcion = int(input("Introduce que operacion quieres hacer"))

  if (opcion == 5 or opcion > 4):
    break

  num1 = int(input("Introduce el primer numero: "))
  num2 = int(input("Introduce el segundo numero: "))

  if (opcion == 1):
    suma(num1,num2)
  elif (opcion == 2):
    restar(num1,num2)
  elif(opcion == 3):
      multiplicar(num1,num2)
  elif (opcion == 4):
        dividir(num1,num2)

def suma(num1,num2):
    r = num1+num2
    print("el resultado de la suma es ",r)

def restar(num1,num2):
    r = num1-num2
    print("el resultado de la resta es ",r)

def multiplicar(num1,num2):
    r = num1*num2
    print("el resultado de la multi es ",r)

def dividir(num1,num2):
    r = num1/num2
    print("el resultado de la division es ",r)



if __name__=="__main__":
    main()
 