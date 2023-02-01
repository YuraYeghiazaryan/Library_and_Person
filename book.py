class Book:
    __DICT_FOR_KEYS = {}
    __COUNTER_ID = 0
    __COUNTER_KEY = 1000

    def __init__(self, author: str, title: str):
        self.__author = author
        self.__title = title
        self.__id = None
        self.__set_id()
        self.__key = None
        self.__set_key()

    def __set_id(self) -> None:
        self.__id = self.__COUNTER_ID
        Book.__COUNTER_ID += 1

    def __set_key(self) -> None:
        if '{0}_{1}'.format(self.__author, self.__title) not in Book.__DICT_FOR_KEYS:
            Book.__DICT_FOR_KEYS['{0}_{1}'.format(self.__author, self.__title)] = Book.__COUNTER_KEY
            self.__key = Book.__COUNTER_KEY
            Book.__COUNTER_KEY += 1
        else:
            self.__key = Book.__DICT_FOR_KEYS['{0}_{1}'.format(self.__author, self.__title)]

    def get_id(self) -> int:
        return self.__id

    def get_key(self) -> int:
        return self.__key

    def get_author(self) -> str:
        return self.__author

    def get_title(self) -> str:
        return self.__title
