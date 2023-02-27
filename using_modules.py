import using_function

# the range object
r = range(100, 0, -3)
print(r, type(r))
for i in r:
    print(i, end=', ')

odds = tuple(range(1, 100, 2))
print(odds)

if __name__ == '__main__':
    print(using_function.hypot(-3, -4))