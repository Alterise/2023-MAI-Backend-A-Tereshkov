class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.__size = 0
        self.__capacity = capacity
        self.__data = dict()

    def get(self, key: str) -> str:
        return self.__data[key] if key in self.__data else ''

    def set(self, key: str, value: str) -> None:
        if key in self.__data:
            del self.__data[key]
        elif self.__size < self.__capacity:
            self.__size += 1
        else:
            for k in self.__data.keys():
                del self.__data[k]
                break
        self.__data[key] = value

    def rem(self, key: str) -> None:
        if key in self.__data:
            del self.__data[key]
            self.__size -= 1
