sum = 0
for i in xrange(1, 101):
    sum += i
print sum

lst = xrange(1, 101)
def add(x, y):
    return x + y
print reduce(add, lst)

print reduce((lambda x, y: x + y), xrange(1, 101))
