# Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.


# Exemples d’utilisation :
# $> python exo.py “Hello milady,   bien ou quoi ??”
# Helo milady, bien ou quoi ?


# Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

def get_args() -> list:
    return sys.argv

def is_valid_argv(args: list) -> bool:
    if len(args) != 2:
        return False
    return True

def del_doublon(text: str):
    nt = ""

    for indx in range(0,len(text)):
        if text[indx-1] == text[indx]:
            continue
        else:
            nt += text[indx]
    print(nt)

args = get_args()
if is_valid_argv(args):
    text = args[-1]
    del_doublon(text)