#1
numbers = [10,-10,5,9,8,55,-9,8]
numbers1 = list(numbers)
quant = []
for i in range(0,len(numbers)):
    if numbers[i]*(-1) in numbers:
        quant.append(1)
print(int(sum(quant)/2))