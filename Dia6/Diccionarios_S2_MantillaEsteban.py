# ##########################
# #### Clase Dia 6 ######
# ##########################
# Diccionarios
#Un DICccionario  es una colección de elementos , donde cada elementos insertado tiene una llave úntica, 
# la cual va acompañada de un valor 

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                 ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}

listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)

userCant = 2
booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(inut("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        nombre=input("por favor;ingrese nombre: " )
        apellido=input("por favor;ingrese apellido: " )
        edad=int(input("por favor;ingrese edad: " ))
        cantelefono=int(input("por favor;ingrese la cantidad de telefono:" ))
        diccionarioVacio={
            "id":userCant + 1,
            "nombre":nombre,
            "apellido":apellido,
            "edad":edad,
            "telefonos":[]
            
        }
        for i in range(cantelefono):
            codigo=int(input("por favor;ingrese codigo: " ))
            numero=int(input("por favor;ingrese numero: " ))
            tipo=input("por favor;ingrese tipo: " )
        data_numero={
            "Codigo": codigo,
            "numero": numero,
            "tipo": tipo
            
        }
        diccionarioVacio["telefonos"].append(data_numero)
        
    listaRobusta.append(diccionarioVacio)
    userCant += 1
    print(f"Persona {nombre} fue creada exitosamente." )
            
        

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")
    
    elif(opcionUsuario==3):
       print("Buscar persona individual")
       opcionindividual=int(input("Por favor ingrese el id de la persona"))
       print("Persona #",opcionindividual)
       print("#########################")
       print("ID:", listaRobusta[opcionindividual-1]["id"])
       print("Nombre:", listaRobusta[opcionindividual-1]["nombre"])
       print("Apellido:", listaRobusta[opcionindividual-1]["apellido"])
       print("Edad:", listaRobusta[opcionindividual-1]["edad"])          
            
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

    
    
    
#Desarrollado por Esteban Mantilla: C.C-1.097.098.666