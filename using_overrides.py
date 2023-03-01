# we can override any and all of the operators in Python

class Word(): # implicitly inherit from Object
    ''' this class will ignore case when comparing equality'''
    def __init__(self, text):
        self.text = text # could use get/set methods
    # here we override the built in operator for 'equals'
    def __eq__(self, other_word): # we will pas in another instance of 'Word' for comparison
        return self.text.lower() == other_word.text.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object
  
if __name__ == '__main__':
    low = 'hello'
    hi  = 'HELLO'
    print(low == hi) # nope
    wlow = Word('hello')
    whi  = Word('HELLO')
    print(wlow == whi) # yes they are considered equal