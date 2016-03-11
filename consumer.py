from threading import Thread
from time import sleep


class Consumer(Thread):

    __monitor = None
    __cycles = None

    def __init__(self, monitor, cycles):
        Thread.__init__(self)  # needed for inheritance
        self.__monitor = monitor
        self.__cycles = cycles

    def run(self):
        number = 0

        while number >= 0:

            'read from the monitor'
            number = self.__monitor.pull_from_list()

            if number != -2:
                'print what you found'
                print("Consumer - Fetched From Monitor : " + str(number))
