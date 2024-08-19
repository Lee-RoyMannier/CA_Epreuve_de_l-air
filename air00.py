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

def valid_arg(args: list) -> bool:
    if len(args) > 2:
        return False
    return True

def get_args(args: list):
    if valid_arg(args):
        return args[1]
    return "Error"


def split(string: str) -> list:
    sep = [" ", "\n", "\t"]
    split_list = []
    text = ""

    for c in string:
        if c in sep:
            split_list.append(text)
            text = ""
        else:
            text += c

    split_list.append(text)

    return split_list

def display(l: list) -> None:
    for c in l:
        print(c)

my_args = get_args(sys.argv)
if my_args != "Error":
    split_list = split(my_args)
    display(split_list)
else:
    print("Error d'arguments")