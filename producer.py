import random
from threading import Thread
from time import sleep


class Producer(Thread):

    __monitor = None
    __cycles = None

    def __init__(self, monitor, cycles):
        Thread.__init__(self)  # need for inheritance
        self.__monitor = monitor
        self.__cycles = cycles

    def run(self):
        index = 0

        print("Cycles is: " + str(self.__cycles))
        print("Index is: " + str(index))

        while index < self.__cycles:
            index = index +1
            'generate random number'
            number = random.randint(0, 1000000)

            'tell everyone about it'
            print("Producer - Placing Number Into Monitor : " + str(number))
            #print("Index Is: " + str(index))

            'add to the monitor list'
            self.__monitor.add_to_list(number)



        # add -1 to tell the consumer were done. since -1 is impossible to be added by simulator
        self.__monitor.add_to_list(-1)
