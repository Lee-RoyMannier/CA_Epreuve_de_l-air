# Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).

# Votre programme devra utiliser une fonction prototypée comme ceci :
# ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
# 	# votre algorithme
# 	return (tableau)
# }


# Exemples d’utilisation :
# $> python exo.py “Bonjour les gars”
# Bonjour
# les
# gars

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



def split(string: str) -> list:
    i: int = 0
    tab: list = []
    iterrator_string: int = 0

    while i < len(string):
        if ord(string[i]) == 32 or i == len(string) - 1:
            tab.append(string[iterrator_string:i]) if i != len(string) -1 else tab.append(string[iterrator_string:i + 1])
            iterrator_string = i + 1 
        i += 1
    
    return tab


if len(sys.argv) != 2:
    print("error")
    sys.exit()

print(split(sys.argv[1]))