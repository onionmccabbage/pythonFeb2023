# many built in data types are iterable by default
# list, set, tuple, string are all zero-based indexed and naturally iterable
# dict is iterable using 'in'

my_d = {'name':'Timnit', 'age':42, 'hero':True}
# we can iterate over a dictionary
for (k, v) in my_d.items(): # a tuple (k, v) for key-value pairs
    print(k, v)

# despite inherant iterability, we sometimes need to access '__next__' items from a collection
my_l = [1, 7, 3, 5, 9, 0]
my_l_iterable = iter(my_l) # we have made it an iterable (also for tuple, set and string)
print( type(my_l_iterable) )
# we can now access __next__ values
print(my_l_iterable.__next__() ) # 1
print(my_l_iterable.__next__() ) # 7
# NB you CANNOT go backwards through an iterable
print(my_l_iterable.__next__() ) # 3
print(my_l_iterable.__next__() ) 
print(my_l_iterable.__next__() )
print(my_l_iterable.__next__() )
my_l.append('additonal member') # we can mutate the list while in play
print(my_l_iterable.__next__() ) # stopiteration!

# when there are no more values the iterable is EXHAUSTED