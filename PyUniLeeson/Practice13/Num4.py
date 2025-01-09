file = open('num4.1text.txt')
fr = file.readlines()
file.close()

print(fr)

nums = []
for s in fr:
    nums.append(int(s[0]))

print(nums)

g = []
for s in nums:
    if s%3==0 and s%7!=0:
        g.append(str(s))

print(g)

file = open('num4.2text.txt', 'w+')

for s in g:
    file.write(f'{s} \n')

file.close()