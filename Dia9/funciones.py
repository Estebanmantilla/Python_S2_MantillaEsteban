import json

def abrirJSON():
    dicFinal=[]
    with open("./Jaim.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Jaim.json",'w') as outFile:
        json.dump(dic,outFile)




def mostrarlista(diccionariooo):
    for i in range(len(diccionariooo)):
        print("Artista #",i+1)
        print("ID: ",diccionariooo[i]["id"])
        print("Artist name: ",diccionariooo[i]["Artist name"])
        print("Country: ",diccionariooo[i]["Country"])
        print("Active years: ",diccionariooo[i]["Active years"])
        print("Release year of first charted record: ",diccionariooo[i]["Release year of first charted record"])
        print("Genre: ",diccionariooo[i]["Genre"])
        print("Total certified units: ",diccionariooo[i]["Total certified units"])
        print("Claimed sales: ",diccionariooo[i]["Claimed sales"])

def mostrarporpais(diccionariooo,opcionUsuario):
    print("Artistas de ",opcionUsuario)
    for i in range(len(diccionariooo)):
        if (diccionariooo[i]["Country"]) == opcionUsuario:
            print("Artista #",i+1)
            print("ID: ",diccionariooo[i]["id"])
            print("Artist name: ",diccionariooo[i]["Artist name"])
            print("Country: ",diccionariooo[i]["Country"])
            print("Active years: ",diccionariooo[i]["Active years"])
            print("Release year of first charted record: ",diccionariooo[i]["Release year of first charted record"])
            print("Genre: ",diccionariooo[i]["Genre"])
            print("Total certified units: ",diccionariooo[i]["Total certified units"])
            print("Claimed sales: ",diccionariooo[i]["Claimed sales"])
            
def informesV(diccionariooo,opcionUsuario):
    print("informe de ventas de artista #",opcionUsuario)  
    print("Total certified units: ",diccionariooo[opcionUsuario-1]["Total certified units"])
    print("Claimed sales: ",diccionariooo[opcionUsuario-1]["Claimed sales"])

def UnitedKINGdom(diccionariooo):
    print("Artistas de UK (1960-1971)")
    start= 1960
    end= 1970
    for i in range (len(diccionariooo)):
        if (diccionariooo[i]["Country"]=="United Kingdom"and start < diccionariooo[i]["Release year of first charted record"] < end):
            print("Artista #",i+1)
            print("ID: ",diccionariooo[i]["id"])
            print("Artist name: ",diccionariooo[i]["Artist name"])
            print("Country: ",diccionariooo[i]["Country"])
            print("Active years: ",diccionariooo[i]["Active years"])
            print("Release year of first charted record: ",diccionariooo[i]["Release year of first charted record"])
            print("Genre: ",diccionariooo[i]["Genre"])
            print("Total certified units: ",diccionariooo[i]["Total certified units"])
            print("Claimed sales: ",diccionariooo[i]["Claimed sales"])

def rockPop(diccionariooo):
    print("Artistas ROCK/POP")
    for i in range(len(diccionariooo)):
        if (diccionariooo[i]["Genre"]) == "rock" or "pop" or "Rock" or "Pop":
            print("Artista #",i+1)
            print("ID: ",diccionariooo[i]["id"])
            print("Artist name: ",diccionariooo[i]["Artist name"])
            print("Country: ",diccionariooo[i]["Country"])
            print("Active years: ",diccionariooo[i]["Active years"])
            print("Release year of first charted record: ",diccionariooo[i]["Release year of first charted record"])
            print("Genre: ",diccionariooo[i]["Genre"])
            print("Total certified units: ",diccionariooo[i]["Total certified units"])
            print("Claimed sales: ",diccionariooo[i]["Claimed sales"])





    
        

