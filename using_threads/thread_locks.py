import threading
import time
import random
import timeit

# here is a global variable
counter = 1
lock = threading.Lock() # we now have a lock we can use

def workerA():
    global counter # we now have access to the counter in the global scope
    lock.acquire() # we have exclusive use of teh locked assets
    try:
        while counter < 10:
            counter += 1 # increment the counter
            print(f'A increments counter to {counter}')
            time.sleep(random.randint(0,1))
    # we typically handle specific exceptions, then more generic ones
    except Exception as err:
        print(err)
    finally:
        lock.release()
def workerB():
    global counter # we now have access to the counter in the global scope
    lock.acquire() # we have exclusive use of teh locked assets
    try:
        while counter >-10:
            counter -= 1 # decrement the counter
            print(f'B decrements counter to {counter}')
            time.sleep(random.randint(0,1))
    # we typically handle specific exceptions, then more generic ones
    except Exception as err:
        print(err)
    finally:
        lock.release()

def main():
    t0 = timeit.default_timer()
    tA = threading.Thread(target=workerA)
    tB = threading.Thread(target=workerB)
    tB.start()
    tA.start()
    tA.join()
    tB.join()
    
    t1 = timeit.default_timer()
    print(f'Execution took {t1-t0}')

    


if __name__ == '__main__':
    main()