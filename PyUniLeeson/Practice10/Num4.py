A = int(input('Enter A: '))
B = int(input('Enter B: '))
OP = int(input('Enter operation num: '))
def Calc(A,B,OP):
    if A!=0 and B!=0:
        if OP==1:
            print(A-B)
        elif OP==2:
            print(A*B)
        elif OP==3:
            print(A/B)
        else:
            print(A+B)
Calc(A,B,OP)