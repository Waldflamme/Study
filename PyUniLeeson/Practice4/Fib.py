num = int(input('Enter a number^ '))
fib = [0,1]
for i in range(1,num):
    fib.append(0)
for i in range(2,num+1):
        fib[i] = fib[i-1] + fib[i-2]
print(fib[i])
print(sum(fib))
