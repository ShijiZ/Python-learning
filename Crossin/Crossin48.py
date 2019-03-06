class MyClass:
    name='Sam'

    def SayHi(self):
        print 'Hello %s'%self.name

mc=MyClass()
print mc.name
mc.name='Lily'
mc.SayHi()
