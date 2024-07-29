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



def concat(tab: list, sep: str) -> str:
    i: int = 0
    n_s: str = ""

    while i < len(tab):
        n_s += str(tab[i])
        
        if i < len(tab) -1 :
            n_s += sep
        
        i += 1 
    
    return n_s


if len(sys.argv) < 3:
    print("error")
    sys.exit()

tab: list = sys.argv[1:-1]
sep: str = sys.argv[-1]
print(concat(tab, sep))