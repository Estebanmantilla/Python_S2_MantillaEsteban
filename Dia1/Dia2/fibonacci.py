#fibonacci
#empezar serie
num1=0
num2=1
cantidad=int(input("cuantos numeros de la serie de fibonacci desea: "))
#serie
print(0)
print(1)
for i in range(cantidad-2):
    resultado=num1 + num2
    print(resultado)
    num1=num2
    num2=resultado
   
# Desarrollado por: Esteban Mantilla -C.C:1.097.098.669