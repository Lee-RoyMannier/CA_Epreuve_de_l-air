# Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).

# Vous utiliserez une fonction de cette forme (selon votre langage) :
# my_quick_sort(array) {
# 	# votre algorithme
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py 6 5 4 3 2 1
# 1 2 3 4 5 6

def my_quick_sort(array):

    if len(array) <=1:
        return array

    pivot = array[0]

    greater = [x for x in array[1:] if x >= pivot]
    less = [x for x in array[1:] if x < pivot]
    print('LESS:', less)
    print("GREATER:", greater)
    return my_quick_sort(less) + [pivot] + my_quick_sort(greater)


x = my_quick_sort([6,1,3,44,21,10])
print(x)