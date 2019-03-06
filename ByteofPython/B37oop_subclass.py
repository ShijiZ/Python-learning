class SchoolMember:
    '''Represents any school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized school member: {})'.format(self.name)

    def tell(self):
        '''Tell my details'''
        print 'Name: {}, Age: {}'.format(self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: {:d}'.format(self.salary)

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print '(Initialized student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Mark: {:d}'.format(self.mark)

t = Teacher('Swaroop', 30, 30000)
s = Student('Shiji', 22, 100)

# Print a blank line
print

members = [t, s]
for member in members:
    # Works for both teachers and students.
    member.tell()

