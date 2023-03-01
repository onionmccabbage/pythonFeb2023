# Python uses @ as 'decorator' syntax

# we will decorate our function by adding additonal functionality
def show_args(func): # any function can be passed in as an argument to this function
    ''' this decorator will reveal all the arguments passed in 
    to any function I choose to decorate'''
    def new_function(*args, **kwargs):
        print(f'Running function called {func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')
        # we may choose ot execute the original function
        result = func(*args, **kwargs)
        return result
    # we then return this new function
    return new_function # we return our new function, which gets called and has its OWN return

# here are some simple utility functions
@show_args
def add_ints(x, y):
    return int(x)+int(y)

@show_args
def sub_ints(x, y):
    return int(x)-int(y)

if __name__ == '__main__':
    print( add_ints(3, 4) ) # 7
    print( add_ints(x=3, y=4) ) # 7
    print( sub_ints(4, 3) ) # 1
    print( sub_ints(y=4, x=3) ) # 1
    print( sub_ints(4, y=3) ) # 1