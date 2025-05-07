# Mayor de 3 numeros
# leer los tres numeritos
numero1= int(input("dame el primer numero: "))
numero2= int(input("dame el segundo numero: "))
numero3= int(input("dame el tercer numero: "))
#hacer los condicionales 
if (numero1>=numero2):
    if (numero1>=numero3):
        print ("el numero mayor es: "+str(numero1))
    else:
        print("el numero mayor es: "+str(numero3))
elif(numero2>=numero3):
    print("el numero mayor es: "+str(numero2))
else:
    print("el nunero mayor es: "+str(numero3))

# Desarrollado por: Esteban Mantilla -C.C:1.097.098.669