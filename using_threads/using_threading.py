import os
import time
import random

import threading # avoid using reserved terms for file names

def my_func(n):
    for i in range(1,50):
        print(n)
        time.sleep(random.random()*0.1) # sleep for millisec


if __name__ == '__main__':
    # print( os.cpu_count() )
    t1 = threading.Thread(target=my_func, args=("t1",)) # example of a single-member tuple
    t2 = threading.Thread(target=my_func, args=("t2",)) # example of a single-member tuple
    # get the threads running
    t1.start()
    print('when does this run? A')
    t2.start()
    print('when does this run? B')
    # it is best practice to
    t1.join()
    print('when does this run? C')
    t2.join()
    print('when does this run? D')
