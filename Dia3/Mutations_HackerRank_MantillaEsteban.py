# DIA 3 ######
##############
def mutate_string(string, position, character):
    position=list(string)
    position[5] = "k"
    string= "".join(position)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# Desarrollado por: Esteban Mantilla -C.C:1.097.098.669  