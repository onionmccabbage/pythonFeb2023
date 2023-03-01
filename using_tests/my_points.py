class Point():
    '''The Point class represents a point in 2-d space
    x and y are the coodinates as integers'''
    def __init__(self, x, y):
        self.x = x # this calls the x setter method
        self.y = y
    @property
    def x(self): # the 'getter' method
        return self.__x
    @x.setter
    def x(self, new_x): # the 'setter' method
        if type(new_x)==int:
            self.__x = new_x # the 'mangled' value of x
        else:
            raise TypeError # throw an exception - wrong data type
    @property
    def y(self): # the 'getter' method
        return self.__y
    @y.setter
    def y(self, new_y): # the 'setter' method
        if type(new_y)==int:
            self.__y = new_y # the 'mangled' value of x
        else:
            raise TypeError # throw an exception - wrong data type
    @staticmethod # only callable as Point.doStuff()
    def doStuff(): # this method belongs to the class not to any instance
        pass
    @classmethod # explicitly say this is a methos of the class
    def moveBy(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def display(self): # return a tuple of x and y
        return (self.x, self.y) # remember - this calls the 'getter' methods
    def hypot(self):
        h = (self.x**2+self.y**2)**0.5
        return h      