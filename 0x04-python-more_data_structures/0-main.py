#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 6, 3, 4, 5, 4, 6, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)
lists = ['apple', 'banana', 'cherry']
new_list = search_replace(lists, 'banana', 'orange')

print(new_list)
print(my_list)
