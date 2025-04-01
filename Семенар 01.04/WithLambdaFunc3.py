from functools import reduce

n = int(input('Enter n: '))

fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])


print(fibonacci(n))
fib_numbers = fibonacci(n)

fib_squares = list(map(lambda x: x**2, fib_numbers))

print(fib_squares)
