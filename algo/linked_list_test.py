from ds.linked_list import UnorderedList

my_list = UnorderedList()
my_list.add(23)
my_list.add(3)
my_list.add(12)
my_list.add(32)
my_list.add(113)
my_list.add(222)
print(my_list)

my_list.append(209)
print(my_list)

my_list.remove(32)
print(my_list)

index = my_list.index(3)
print(index)
