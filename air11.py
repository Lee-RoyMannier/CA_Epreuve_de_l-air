# Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.


# Exemples d’utilisation :
# $> ruby exo.rb O 5
#     O
#    OOO
#   OOOOO
#  OOOOOOO
# OOOOOOOOO


# Afficher error et quitter le programme en cas de problèmes d’arguments.
hauteur = 10
style = "0"
row = ""
for i in range(1, hauteur+1):
    for r in range(i, i+i):
        row = f"{' '* (hauteur-i)} {style*r}"
    print(row)