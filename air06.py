# Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.

# Utilisez une fonction de ce genre (selon votre langage) :
# ma_fonction(array_de_strings, string) {
# 	# votre algorithme
# 	return (nouvel_array_de_strings)
# }


# Exemples d’utilisation :
# $> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “t”
# Michel

# $> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “a”
# Michel, Thérèse, Benoit



# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def get_argv():
    return sys.argv[1:]

def is_valid_argv(args: list):
    if len(args) < 2:
        return False
    return True

def del_not_in_str(text_list: list, letter: str):
    nl = []

    for i in text_list:
        if letter.lower() in i.lower():
            continue
        else:
            nl.append(i)

    print(nl)

args = get_argv()
if is_valid_argv(args):
    del_not_in_str(args[:-1], args[-1])


