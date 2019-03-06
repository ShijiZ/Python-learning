def print_max(x, y):
    '''
    Prints the maximum of two numbers.

    The two values ust be integers.
    '''
    #convert to integers, if possible
    x = int(x)
    y = int(y)

    if x>y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print_max(2, 3)
print print_max.__doc__
help(print_max)
