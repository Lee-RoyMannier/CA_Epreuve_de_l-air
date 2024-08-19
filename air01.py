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

def valid_args(args: list) -> bool:
    if len(args) != 3:
        return False
    return True

def split(text:str, sep: str):
    nt = ""
    n = []
    i = 0

    while i <= len(text)-1:
        if text[i: i+len(sep)] == sep:
            n.append(nt)
            nt = ""
            i += len(sep)

        else:
            nt += text[i]
            i +=1
    n.append(nt)
    return n

def display_liste(l: list) -> None:
    for c in l:
        print(c)

args = sys.argv


if not valid_args(args):
    print("Error arguments")
else:
    sep = args[-1]
    text = args[1]
    n = split(text, sep)
    display_liste(n)

