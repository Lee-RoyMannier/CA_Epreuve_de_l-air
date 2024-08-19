# Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.


# Exemples d’utilisation :
# $> python exo.py 1 2 3 4 5 4 3 2 1
# 5

# $> python exo.py bonjour monsieur bonjour
# monsieur


# Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

def get_args() -> list:
    return sys.argv

def is_valid_args(args: list) -> bool:
    if len(args) < 3:
        return False
    return True

def find_pair(args: list) -> list:
    nb = {}

    for n in args:
        if not n in nb:
            nb[n] = 1
        else:
            nb[n] += 1

    not_in_pair = list(filter(lambda x: nb[x] == 1, nb))
    return not_in_pair

def display_not_pair(not_in_pair: list) -> None:
    for c in not_in_pair:
        print(c, end=" ")

args = get_args()[1:]
if is_valid_args(args):
    not_in_pair = find_pair(args)
    display_not_pair(not_in_pair)
else:
    print("Error")
