N = int(input('Enter N: '))

def PrimeFactors(N):
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)

PrimeFactors(N)