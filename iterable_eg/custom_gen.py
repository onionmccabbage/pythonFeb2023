# we write a function as usual but in place of return we say yield
def myGen():
    count = 0
    while True:
        count += 1
        yield count

if __name__ == '__main__':
    g = myGen() # we need an intance of our custom generator
    # g.arbirary_property = 'ooh thats clever'
    print( g.__next__() ) # 1
    print( g.__next__() ) # 2
    for i in g:
        if i==10:
            break
        else:
            print(i) # keep yielding until exhausted