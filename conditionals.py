s = 'text'
s = 4

if (type(s)== str):
    print('we have a string')
elif type(s)==int:
    print('we have an integer')
elif type(s)==float:
    print('we have a float')
else:
    print("something other")

# check if a value is a square number
sq = {1, 4, 9, 16, 25} # this is a SET = an indexed collection of unique values
print(sq)
n = 4
if n in sq:
    print('it is a square number')

for i in range(0, 10): # start at 0 stop before 10
    print(i**i)

# there is no practicable limit to the size of numbers
print(10**1000)

while True:
    break