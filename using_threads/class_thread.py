from threading import Thread
import time
import random
import timeit # much more accurate timer for code performance

class MyClass(Thread): # here we inherit from Thread
    def __init__(self, n):
        Thread.__init__(self)
        self.nane = n # we shoyuld get/set validate this
    # to make this thrad runnable we overide the built in run method
    def run(self):
        for i in range(1,50):
            print(i)
            time.sleep(random.random()*0.1) # sleep for millisec

if __name__ == '__main__':
    m1 = MyClass('m1')
    m2 = MyClass('m2')
    s = timeit.default_timer()
    m1.start() # this invokes our 'run' method
    m2.start()
    m1.join()
    m2.join()
    e = timeit.default_timer()
    print(e-s)