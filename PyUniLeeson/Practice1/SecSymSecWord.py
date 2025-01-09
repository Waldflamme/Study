ln1 = list(map(str, input('Enter a sentence: ').split()))
ln2=ln1[1:]
ln3=" ".join(ln2)
print(ln3[::2])

