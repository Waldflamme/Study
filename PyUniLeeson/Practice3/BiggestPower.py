n = int(input("Enter N: "))
l = [0]
for K in range(0,n):
    if 3**K<n:
        l.append(K)
print(max(l))