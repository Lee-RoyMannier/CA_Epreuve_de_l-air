# Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.


# Exemples d’utilisation :
# $> python exo.py “Hello milady,   bien ou quoi ??”
# Helo milady, bien ou quoi ?


# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def no_adjacent_identical_characters(string: str) -> str:
    i: int = 0
    n_s: str = ""

    while i < len(string):
        if string[i] != string[i - 1]:
            n_s += string[i]
        i+=1
    
    return n_s

if len(sys.argv) != 2:
    print("error")
    sys.exit()

string: str = sys.argv[1]
print(no_adjacent_identical_characters(string))