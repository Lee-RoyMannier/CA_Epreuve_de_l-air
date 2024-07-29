# Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste.


# Exemples d’utilisation :
# $> ruby exo.rb 1 2 3 4 5 “+2”
# 3 4 5 6 7

# $> ruby exo.rb 10 11 12 20 “-5”
# 5 6 7 15


# L’opération à appliquer sera toujours le dernier élément.


# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys


def concat(tab: list, sep: str) -> str:
    i: int = 0
    n_s: str = ""

    while i < len(tab):
        n_s += str(tab[i])
        
        if i < len(tab) -1 :
            n_s += sep
        
        i += 1 
    
    return n_s

def operation(tab: list, op: str) -> list:
    sign: str = op[0]
    i: int = 0
    result: list = []

    while i < len(tab):
        if sign == "+":
            result.append(int(tab[i]) + int(op[1:]))
        elif sign == "-":
            result.append(int(tab[i]) - int(op[1:]))
        else:
            return "error" # type: ignore
        i += 1

    return result

if len(sys.argv) < 3:
    print("error")
    sys.exit()

op: str = sys.argv[-1]
tab: list = sys.argv[1:-1]
print(concat(operation(tab, op), " "))