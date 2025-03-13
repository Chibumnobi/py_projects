#lists
listj = [1, 2, 3, 'Chibumnobi', 5]
# to bring out elements from a list and put it in a separate  variable
first = listj[0]
print(first)
# to add an element to the end a list
listj.append('Chichi')
print(listj)
# to insert an item to a specific index
listj.insert(0, 'Muna')
print(listj)
#to remove an item
listj.remove(2)
print(listj)
# same as remove
listj.pop(0)
print(listj)
# add another list to the end
lista = [1, 2, 3, 'Chibumnobi', 5]
listj.extend(lista)
print(listj)