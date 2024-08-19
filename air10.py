# # Créez un programme qui affiche le contenu d’un fichier donné en argument.


# Exemples d’utilisation :
# $> cat a.txt
# Je danse le mia
# $> ruby exo.rb “a.txt”
# Je danse le mia


# Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible.

import sys

def read_file(file: str):
    file_op = open(file,"r")
    print(file_op.read())
    file_op.close()

read_file(sys.argv[1])