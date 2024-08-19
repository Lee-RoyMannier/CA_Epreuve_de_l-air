# Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste.


# Exemples d’utilisation :
# $> ruby exo.rb 1 2 3 4 5 “+2”
# 3 4 5 6 7

# $> ruby exo.rb 10 11 12 20 “-5”
# 5 6 7 15


# L’opération à appliquer sera toujours le dernier élément.


# Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

def get_argv():
    return sys.argv[1:]

def is_valid_argv(args: list):
    if len(args) < 2:
        return False
    return True

def get_symbole(args: str):
    return args[0]

def get_number_op(args: str):
    return args[1:]

def operation(numbers: list, op: str, by: int):
    if op == "+":
        nl = [int(x)+by for x in numbers]
    elif op == "-":
        nl = [int(x)-by for x in numbers]
    else:
        return  "ERROR OPERATION"
    return nl

def display_new_liste(numbers):
    for i in numbers:
        print(i, end=" ")

args = get_argv()
if is_valid_argv(args):
    op = get_symbole(args[-1])
    by = int(get_number_op(args[-1]))
    nb_list = args[:-1]
    numbers = operation(nb_list, op, by)
    display_new_liste(numbers)
else:
    print('erroe')