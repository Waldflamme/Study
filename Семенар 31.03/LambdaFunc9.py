numbers_list = [1, 2, 3, 4]
numbers_tuple = (0, 1, 2, 3)

list_as_strings = list(map(lambda x: str(x), numbers_list))

tuple_as_strings = list(map(lambda x: str(x), numbers_tuple))

combined_result = list_as_strings + tuple_as_strings

print(combined_result)