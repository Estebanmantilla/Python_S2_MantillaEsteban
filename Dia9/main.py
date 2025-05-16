# DIA 9 ######
##############
#importar json y funciones para la persistencia
from funciones import *
diccionariooo = abrirJSON()

booleano = True

while (booleano):
    diccionariooo = abrirJSON()
    print("########################")
    print("1. crear datos de una artistas")
    print("2. ver artistas actuales")
    print("3. ver artistas de un pais especifico")
    print("4. informe de ventas de un artista")
    print("5. datos de artistas de 1960 a 1970 (United Kingdom)")
    print("6. datos artistas genero(rock/pop)")
    print("7. cerrar programa")
    print("########################")
    opcionUsuario = int(input("Eliga la opcion numerica: "))
    if (opcionUsuario == 1) :
     #obtener datos del artista
        print("Crear datos artista")
        nombre=input("ingrese el nombre del artista: ")
        pais=input("ingrese el pais del artista: ")
        actividad=input("ingrese los años activos del artista(con un - de separacion): ")
        añoLan=int(input("ingrese el año de lanzamiento del primer disco: "))
        genero=input("ingrese el genero musical del artista: ")
        unidadesCer=input("ingrese el nomero de unidades certificadas del artista: ")
        ventas=input("ingrese las ventas reclamadas del artista: ")
        diccionarioArtista = {
        "id": (diccionariooo[len(diccionariooo)-1]["id"])+1,
        "Artist name": nombre,
        "Country": pais,
        "Active years": actividad,
        "Release year of first charted record": añoLan,
        "Genre": genero,
        "Total certified units" : unidadesCer,
        "Claimed sales": ventas    
        }
        diccionariooo.append(diccionarioArtista)
        guardarJSON(diccionariooo)
        print(f"el artista {nombre} fue creado correctamente :)")
    if (opcionUsuario==2):
        mostrarlista(diccionariooo)
    if (opcionUsuario==3):
        print("artista por pais")
        opcionUsuario=input("de que pais quiere ver los artistas(Canada,Colombia,United States,United Kingdom,Barbados,ETC...)")
        mostrarporpais(diccionariooo,opcionUsuario)
    if (opcionUsuario==4):
        print("VENTAS")
        opcionUsuario=int(input("ingrese el numero del artista "))
        informesV(diccionariooo,opcionUsuario)
    if (opcionUsuario==5):
        UnitedKINGdom(diccionariooo)
    
    if (opcionUsuario==6):
        rockPop(diccionariooo)





    
    if (opcionUsuario==7):
        print("Cerrando programa")
        booleano= False





    









# Desarrollado por: Esteban Mantilla -C.C:1.097.098.669