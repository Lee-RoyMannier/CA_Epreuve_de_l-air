# Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.

# Utilisez une fonction de ce genre (selon votre langage) :
# sorted_insert(array, new_element) {
# 	# your algo
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> ruby exo.rb 1 3 4 2
# 1 2 3 4

# $> ruby exo.rb 10 20 30 40 50 60 70 90 33
# 10 20 30 33 40 50 60 70 90


# Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

def get_argv():
    return sys.argv[1:]

def is_valid_argv(args: list):
    if len(args) < 2:
        return False
    return True

def insert(liste: list, index_element: int, element):
    return liste[:index_element] + [element] + liste[index_element:]

def sorted_insert(numbers: list, number: int):
    for inx in range(0, len(numbers)):
        if int(numbers[inx-1]) < number and int(numbers[inx]) > number:
            numbers = insert(numbers, inx, number)
    
    print(numbers)

args = get_argv()
if is_valid_argv(args):
    sorted_insert(args[:-1], int(args[-1]))
