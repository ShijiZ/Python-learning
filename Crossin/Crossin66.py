list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
print list_2

list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i for i in list_1 if i % 2 == 0]
print list_2

list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i/2 for i in list_1 if i % 2 == 0]
print list_2

print ';'.join([str(i) for i in range(1,101) if i % 2==0 or  i % 3==0 or  i % 5==0])
