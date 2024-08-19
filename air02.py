# Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme.

# Utilisez une fonction de ce genre (selon votre langage) :
# ma_fonction(array_de_strings, separateur) {
# 	# votre algorithme
# 	return (string)
# }


# Exemples d’utilisation :
# $> python exo.py “je” “teste” “des” “trucs” “ “
# Je teste des trucs


# Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

def get_arguments() -> list:
    return sys.argv

def is_valid_args(args: list) -> bool:
    if len(args) < 3 :
        return False
    return True

def join(list_txt: list, sep: str):
    nt = ""

    for indx in range(0,len(list_txt)):
        if indx != len(list_txt) -1:
            nt += list_txt[indx] + sep
        else:
            nt += list_txt[indx]

    return nt

args = get_arguments()[1:]
if is_valid_args(args):
    sep = args[-1]
    text = args[:-1]
    print(join(text, sep))
else:
    print("Error")

