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


def insert(tab: list, index: int, value: int) -> list:
    i: int = 0

    while i < len(tab):
        if i == index:
            next = tab[i]
            tab[i] = value
            tab[i+1] = next
            break
        i += 1
    
    return tab


def sorted_insert(tab: list, n: int) -> list:
    i: int = 0
    
    while i < len(tab):
        if n < tab[i]:
            insert(tab, i, n)
            break
        i += 1
    else:
        tab.append(n)

    return tab
    

if len(sys.argv) < 3:
    print("Error")
    sys.exit(1)

print(sorted_insert([int(sys.argv[i]) for i in range(1,len(sys.argv)-1)], int(sys.argv[-1])))