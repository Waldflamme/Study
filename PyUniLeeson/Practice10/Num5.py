bn = input('Enter a binary number: ')
def BinaryToDecimal(bn):
    ls = []
    for i in range(len(bn)):
        ls.append(bn[i])
    dec = 0
    for i in range(len(ls)):
        dec += int(ls[i])*(2**(len(ls)-i-1))
    return dec
print(BinaryToDecimal(bn))