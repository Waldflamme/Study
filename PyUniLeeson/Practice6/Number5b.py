#5b
numbers_t = (1,2,3,4,5)
term_ind = 2
print(numbers_t)
print(numbers_t[:numbers_t.index(term_ind):]+numbers_t[numbers_t.index(term_ind)+1::])
