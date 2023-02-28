import sys
sys.path.append('c:/Users/Student06/Documents/py/mod/other') # we can add a location for imports
print (sys.path)
import stuff

def hypot(x, y):
    '''document your code with DOCSTRING
    x is one side
    y is the other side
    return the hypotenuse
    '''
    return ((x**2)+(y**2))**0.5

# exercise the code
if __name__ == '__main__':
    print(__name__)
    print(hypot(3, 4))