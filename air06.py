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



def len(tab) -> int:
    length: int = 0

    try:
        i: int = 0
        while True:
            _ = tab[i]
            length += 1
            i += 1
    except IndexError:
        pass
    
    return length



def pop(tab: list, index: int) -> list:
    n_l: list = []
    i: int = 0

    while i < len(tab):
        if i != index:
            n_l.append(tab[i])
        i += 1

    return n_l



def lower(string: str) -> str:
    n_s: str = ""
    i: int = 0

    while i < len(string):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            n_s += chr(ord(string[i]) + 32)
        else:
            n_s += string[i]
        i += 1

    return n_s


def in_string(tab: list, str_in: str) -> list:
    n_l: list = []
    i: int = 0

    while i < len(tab):
        j: int = 0
       
        while j < len(tab[i]):
            if lower(tab[i][j: j + len(str_in)]) == lower(str_in):
                tab.pop(i)
                i -= 1
                break

            j += 1
        i += 1
    
    return tab




if len(sys.argv) < 3:
    print("error")
    sys.exit()

tab: list = sys.argv[1:-1]
str_in: str = sys.argv[-1]
passed = in_string(tab, str_in)
i: int = 0 

while i < len(passed):
    print(passed[i], end="")
    if i < len(passed) - 1:
        print(", ", end="")
    i += 1
print()