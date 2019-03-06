from random import randint
num=randint(1,100)
print 'Guess what I think?'
answer=input()

result=answer<num
print 'too small?'
print result

result=answer>num
print 'too big?'
print result

result=answer==num
print 'equal?'
print result
