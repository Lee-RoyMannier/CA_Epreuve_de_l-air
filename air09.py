# Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.

# Utilisez une fonction de ce genre (selon votre langage) :
# ma_rotation(array) {
# 	# votre algorithme
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py “Michel” “Albert” “Thérèse” “Benoit”
# Albert, Thérèse, Benoit, Michel
import sys

def rotation(array: list, steps: int):
    new_array = []

    steps = steps % len(array) if array else 0

    for _ in range(steps):
        first_elem = array.pop(0)
        array.append(first_elem)
    print(array)

argv = sys.argv[1:]
rotation(argv, 2)


# Afficher error et quitter le programme en cas de problèmes d’arguments.
