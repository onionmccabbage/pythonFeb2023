# we will write a 'Person' class

class Person:
    '''This class encapsulates a name, age and email fro a person'''
    def __init__(self, n='Grace', a=82, e='default'): # every function in a class MUST take 'self' as an argument
        # here we can set inital values on our class
        self.name  = n # here we actually call setName method
        self.age   = a
        self.email = e
    def setName(self, new_name):
        if type(new_name)==str and new_name != '':
        # if new_name.isinstance(str):
            self.__name = new_name
        else:
            self.__name='default'
    def getName(self):
        return self.__name
    def setAge(self, newAge):
        if type(newAge)==int and newAge >0:
            self.__age = newAge
        else:
            self.__age = 42
    def getAge(self):
        return self.__age
    # we can override Python built-ins
    def __str__(self):
        return (f'{self.__name} is {self.__age} years old') # we return what will be printed
    # we can declare some of our functions to act as get/set methods
    name = property(getName, setName)
    age  = property(getAge, setAge)

if __name__ == '__main__':
    p = Person('Ada', -98, 'ada@babbage.ie')
    g = Person() # this uses the defaults
    print(g)
    print(f'Name: {p.name} Age: {p.age}')
    # print('Name: {0} Age: {1}'.format(p.name, p.age))
    # we CANNOT access the mangled properties of this class
    # print(p.__name)
    # but be careful
    p.__name='oops' # here we add an arbitrary property to the object called p
    print(p.__name, p.name)
    print(p) # this calles the __str__ method
