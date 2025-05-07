# numero primo
#ingresar numerito
numero1= int(input("deme un numero porfavor: "))
verdadero=True
#usar ciclo for para comprobar
for i in range(2,numero1):
    if (numero1%i)==0:
        verdadero=False

if verdadero == False:
    print("no es primo bro")
else:
    print("si es primo que lo que")

      
    

# Desarrollado por: Esteban Mantilla -C.C:1.097.098.669