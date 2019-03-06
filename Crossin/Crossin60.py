import random

a=random.randint(3,3)
print 'a is %d'%a

b=random.random()
print 'b is %.2f'%b

c=random.uniform(3,1.5)
print 'c is %.2f'%c

d=random.uniform(1.5,1.5)
print 'd is %.2f'%d

print random.choice([1, 2, 3, 5, 8, 13]) #list
print random.choice('hello') #string
print random.choice(['hello', 'world']) #list with strings as elements
print random.choice((1, 2, 3)) #tuple

print random.randrange(4) #[0, 1, 2, 3]
print random.randrange(1, 4) #[1, 2, 3]
print random.randrange(1, 9, 2) #[1,3,5,7]

population=[1,43,42,4214,124,214,42,5,34,5,4,456,57,5,869,87,9,787,5]
k=3
print random.sample(population, k)

print population
random.shuffle(population)
print population
