# by convention we talk about 'args' as positional arguments to a function
# and 'kwargs' are the keyword arguments to a function

#        args gathers positional argument
#               x and y are KEYWORD arguments
# careful - positional arguments must all come before keyword arguments
def main(*args, **kwargs):
    # any positional argumetns are now in a tuple called 'args'
    # print(args, type(args))
    print(kwargs, type(kwargs))
    if len(args) == 0:
        # run the zero-argument version of this function
        return 'no args'
    if len(args) ==1:
        return 'one arg'
    if len(args) >1:
        return 'many args'

if __name__ == '__main__':
    # the positional arguments 5 and 3 match up to n and m
    print( main() )
    print( main(3))
    print(main(5, 3))
    # here we also have some KEYWORD arguments
    print(main(5, 3, y=8, x=9))