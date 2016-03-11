
from threading import Lock


class Monitor:

    __data = list()
    __lock = Lock()

    def add_to_list(self, item):
        self.__lock.acquire()

        self.__data.insert(0, item)

        self.__lock.release()

    def pull_from_list(self):
        self.__lock.acquire()

        item = -2
        if len(self.__data) > 0:
            item = self.__data.pop()

        self.__lock.release()

        return item
