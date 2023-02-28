# basic data types
a = 7   # integer
b = 3.4 # float

print(type(a*b))

# c = input('type something ') # everything entered by users will be a string
# d = int(float(c)) # safe bit of type casting
# print (type(d))
e = True # or False for boolean
f = "is it coffee yet" # all strings are immutable collections of characters
print(f[6:14:2]) # always indexed from zero [start:stop-before:step]

# list and tuple
g = [4, 'hello', a, b, f ] # a mutable indexed collection of any data types
g[1] = 'Hello'
print(g)
# caution - a single member tuple MUST have a trailing comma
h = (1, 5.5, 'words', g, e) # an immutable indexed collection of any data type (tuple)
h[3][0] = 'changed'
print(type(h), h) # we CAN mutate the list inside the tuple

# dictionary - NOT indexed by number
j = {'item':'Pot', 'price':3.99} # key:value
print(j['item'])

# math operators + - * / // % **
print(4.5**2)
