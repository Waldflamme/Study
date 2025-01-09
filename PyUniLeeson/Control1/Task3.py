num = input('Enter the number in russian: ')
num_ls = num.split(' ')
dic = {'два':2,'три':3,'четыре':4,'пять':5,'двадцать':20,'тридцать':30,'сорок':40,'пятьдесят':50}
print(num_ls)
sm = set()
for keys in dic:
    for i in range(0,2):
        if num_ls[i]==keys:
            sm.add(dic[keys])

print(sm)
print((sum(sm))**0.5)