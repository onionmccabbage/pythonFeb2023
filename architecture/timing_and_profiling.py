# here are two ways to calculate the fibonacci series
# 1 2 3 5 8 13 21 ...

# we can get a 'profile' of our code using cProfile
# invoke as follows:
#                    -o means Pythopn will apply some code optimizations
# python -m cProfile -o profile_output timing_and_profiling.py
# THEN write a file to read the generated profile output
# in this case, see 'using_pstats.py'


# we can time our code
import timeit
from functools import reduce

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def fib2(n):
    sequence = (0,1)
    for _ in range(2, n+1):
        sequence += (reduce (lambda a,b: a+b, sequence[-2:]), ) # we need a tuple
    return sequence[n]

if __name__ == '__main__':
    s = timeit.default_timer()
    # f = fib(39) # about 15 seconds
    f = fib2(39) # a fraction of a second
    e = timeit.default_timer()
    print(f, e-s)
