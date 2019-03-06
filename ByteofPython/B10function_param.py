def print_max(a, b):
    if a > b:
        print a, 'is maximum'
    elif a < b:
        print b, 'is maximum'
    else:
        print a, 'is equal to', b

# directly pass literal values
print_max(3, 4)
x = 5
y = 7
# pass variables as arguments
print_max(x, y)
