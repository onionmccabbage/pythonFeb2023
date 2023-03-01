from threading import Thread
import time
def standardThread():
    print('starting standard thread')
    time.sleep(5)
    print('ending standard thread')

def daemonThread():
    while True: # careful  -this is an endless loop
        print('heartbeat....')
        time.sleep(0.25)

if __name__ == '__main__':
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread) # daemon=True
    # a daemon can chew through a queue of tasks
    d.setDaemon(True) # we now have a daemon thread - it will terminate when the other threads are done (inc main thread)
    s.start()
    d.start()