def calcSum(*args):
    sum = 0
    for i in args:
        sum += i
    print sum

calcSum(1,2,3)
calcSum(123,456)
calcSum()

def printAll(*args):
    print [i for i in args]

printAll(1,2,3)
printAll(3,2,1)
