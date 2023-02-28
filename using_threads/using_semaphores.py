from random import random
from time import time
from threading import Thread
from threading import Semaphore

class TicketSeller(Thread):
    ticketsSold = 0
    def __init__(self, sem):
        Thread.__init__(self)
        self.__sem = sem
        print('Ticket seller has started selling ticket')
    def run(self):
        global ticketsAvailable
        running = True
        while running:
            # time.sleep(random.randint(0,4)/4) # 0.25, 0.5, 0.75
            self.__sem.acquire()
            if ticketsAvailable <=0:
                running = False
            else:
                # sell some tickets
                self.ticketsSold += 1
                ticketsAvailable -=1
                print(f'Sold a ticket. {ticketsAvailable} tickets remaining')
            self.__sem.release() # added this line!!
        # all done
        print(f'Sold {self.ticketsSold}')

if __name__ == '__main__':
    ticketsAvailable = 1000
    sem = Semaphore(4) # how many concurrent access to the data source
    sellers = [] # an empty list
    for i in range(0, 8):
        seller = TicketSeller(sem)
        seller.start()
        sellers.append(seller) # grab each seller and store in our list
    for seller in sellers:
        seller.join() # make sure all get joined