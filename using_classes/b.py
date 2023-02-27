# we will write a 'Person' class

class Person(object): # here we explicitly inherit from object
    '''This class encapsulates a name, age and email fro a person'''
    def __init__(self, n, a, e): # every function in a class MUST take 'self' as an argument
        # here we can set inital values on our class
        self.name  = n # here we actually call setName method
        self.age   = a
        self.email = e
    @property # this is the getter
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name): # this is the setter
        if type(new_name)==str and new_name != '':
        # if new_name.isinstance(str):
            self.__name = new_name
        else:
            self.__name='default'
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, newAge):
        if type(newAge)==int and newAge >0:
            self.__age = newAge
        else:
            self.__age = 42
    # we can override Python built-ins
    def __str__(self):
        return (f'{self.__name} is {self.__age} years old') # we return what will be printed


if __name__ == '__main__':
    p = Person('Ada', -98, 'ada@babbage.ie')
    print(f'Name: {p.name} Age: {p.age}')
    # print('Name: {0} Age: {1}'.format(p.name, p.age))
    # we CANNOT access the mangled properties of this class
    # print(p.__name)
    # but be careful
    p.__name='oops' # here we add an arbitrary property to the object called p
    print(p.__name, p.name)
    print(p) # this calles the __str__ method
