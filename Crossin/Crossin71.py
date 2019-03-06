def func0(x):
    print 'X in the beginning of func0(x): ', x
    x = 2
    print 'X in the end of func0(x): ', x

x = 50
func0(x)
print 'X after calling func0(x): ', x

def func1(x):
    print 'X in the beginning of func1(x): ', x
    x = 2
    print 'X in the end of func1(x): ', x
    return x

x = func1(x)
print 'X after calling func1(x): ', x

def func2():
    global x
    print 'X in the beginning of func2(x): ', x
    x = 2
    print 'X in the end of func2(x): ', x

x = 50
func2()
print 'X after calling func2(x): ', x

def func3():
    print 'X in the beginning of func3(x): ', x
    # x = 2
    print 'X in the end of func3(x): ', x

x = 50
func3()
print 'X after calling func3(x): ', x
