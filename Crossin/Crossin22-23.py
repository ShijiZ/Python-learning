def Equal(num1,num2):
    if num1<num2:
        print'too small'
        return False
    if num1>num2:
        print'too Big'
        return False
    if num1==num2:
        print 'bingo'
        return True

from random import randint
num=randint(1,101)
print'Guess what I think'
a=False
while a==False:
    answer=input()
    a=Equal(answer,num)

def isEqual(a,b):
    if a<b:
        print'too small'
        return False
    elif a>b:
        print'too big'
        return False
    else:
        print'bingo'
        return True

from random import randint
num=randint(1,101)
print"Again!35
"
a=False
while a==False:
    ans=input()
    a=isEqual(ans,num)
