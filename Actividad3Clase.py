

class opradores():
    num1=0
    num2=0
    res=0


    def suma(self):
        r = self.num1+self.num2
        print("el resultado de la suma es ",r)

    def restar(self):
         r = self.num1-self.num2
         print("el resultado de la resta es ",r)

    def multiplicar(self):
         r = self.num1*self.num2
         print("el resultado de la multi es ",r)

    def dividir(self):
        r = self.num1/self.num2
        print("el resultado de la division es ",r)


def menu():
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

        x = int(input("Introduce el primer numero: "))
        y = int(input("Introduce el segundo numero: "))

        obj = opradores()
        obj.num1=x
        obj.num2=y

        if (opcion == 1):
            obj.suma()
        elif (opcion == 2):
             obj.restar()
        elif(opcion == 3):
             obj.multiplicar()
        elif (opcion == 4):
             obj.dividir()

def main():
    menu()


if __name__=="__main__":
    main()