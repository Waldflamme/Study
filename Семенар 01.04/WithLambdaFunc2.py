ls = ['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']

result = set(map(lambda x: (x.upper(), x.lower()), ls))

print(result)
