# this is called tuple comprehension
odd_t  = (num for num in range(0, 101) if num%2 == 1) # odds
# and this is list comprehension
# in this case, the generated values DO persist in memory, in a List
even_l  = [num for num in range(0, 101) if num%2 == 0] # evens

# we have a generator object
print(type(odd_t))
# we can gra bthe next value from our generator
print(odd_t.__next__()) # 1 wecan grab the next available
print(odd_t.__next__()) # 3
# we can iterate over a generator until it is exhausted
for item in odd_t:
    print(item)
# print(odd_t.__next__()) # nope - it is exhausted
print(type(even_l))

# dictionary comprehension
# for example, we can count the occurences of letters in a string
s = 'dictionary comprehension will iterate over every member of a dictionary'
char_dict = {letter:s.count(letter) for letter in s}
print(char_dict)



