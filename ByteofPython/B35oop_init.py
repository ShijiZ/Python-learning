class Person:
    def __init__(self, name):
        self.name = name
        # The orange "name" is a local variable
        # The "name" in self.name is an object field

    def say_hi(self):
        print 'Hello, my name is', self.name

p = Person('Shiji')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Shiji').say_hi()
