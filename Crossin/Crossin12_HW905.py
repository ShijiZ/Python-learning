b=1
n=1
a=input()
while n<=10:
    print b
    b=b*a
    n=n+1

#or

a=input()
b=1
print b
for i in range(1,10):
    b=b*a
    print b
    
