# Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.

# Utilisez une fonction de ce genre (selon votre langage) :
# sorted_fusion(array1, array2) {
# 	# your algo
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> ruby exo.rb 10 20 30 fusion 15 25 35
# 10 15 20 25 30 35


# Afficher error et quitter le programme en cas de problèmes d’arguments.
import sys

def get_argv():
    return sys.argv[1:]

def is_valid_argv(argv: list):
    if len(argv) != 3 or argv[1] != "fusion":
        return False
    return True

def min_len(l_arra1, l_arr2):
    if len(l_arra1) > len(l_arr2):
        return len(l_arr2)
    return len(l_arra1)


def sorted_fusion(array1: list, array2: list):
    new_array = []
    max_len = min_len(array1, array2)

    for i in range(0, max_len):
        if array1[i] < array2[i]:
            new_array.extend([array1[i], array2[i]])
        else:
            new_array.extend([array2[i], array1[i]])
    new_array.extend(array2[max_len:])
    print(new_array)



array1 = [10, 28, 30]
array2 = [15, 25, 29,34,40]
sorted_fusion(array1, array2)