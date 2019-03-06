a=1
b=1
n=2
x=input()
print a
print b
while n<x:
    c=a+b
    print c
    a=b
    b=c
    n=n+1

#or

a=1
b=1
x=input()
print a
print b
for i in range(1,x-1):
    c=a+b
    print c
    a=b
    b=c
