# Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.


# Exemples d’utilisation :
# $> python exo.py 1 2 3 4 5 4 3 2 1
# 5

# $> python exo.py bonjour monsieur bonjour
# monsieur


# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def intruder(tab: list) -> list:
    value: dict = {}
    i: int = 0

    while i < len(tab):
        if tab[i] not in value.keys():
            value[tab[i]] = 1
        else:
            value[tab[i]] += 1
    
        i += 1

    lmb = lambda x,y : x if y == 1 else "No intruder"
    list_of_intruder: list =  list(map(lmb, value.keys(), value.values())) 

    return list(filter(lambda x: x != "No intruder", list_of_intruder) )

if len(sys.argv) < 2:
    print("error")
    sys.exit()

tab: list = sys.argv[1:]
for intru in intruder(tab):
    print(intru, end=" ")
