# Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.

# Votre programme devra intégrer une fonction prototypée comme ceci :
# ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
# 	# votre algorithme
# 	return (tableau)
# }


# Exemples d’utilisation :
# $> python exo.py “Crevette magique dans la mer des étoiles” “la”
# Crevette magique dans 
#  mer des étoiles

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def len(tab) -> int:
    length: int = 0

    try:
        i: int = 0
        while True:
            _ = tab[i]
            length += 1
            i += 1
    except IndexError:
        pass
    
    return length



def split_by_sep(string: str, sep: str) -> list:
    i: int = 0
    index_sep: int = 0
    tab: list = []

    while i < len(string):
        print(string[i:3])
        if string[i: i+len(sep)] == sep:
            tab.append(string[index_sep:i])
            index_sep = i + len(sep)
        i += 1
    
    tab.append(string[index_sep:])
    
    return tab



if len(sys.argv) != 3:
    print("error")
    sys.exit()

string: str = sys.argv[1]
sep: str = sys.argv[2]
for s in split_by_sep(string, sep):
    print(s)