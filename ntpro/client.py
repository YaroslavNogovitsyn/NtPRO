class Client:
    def __init__(self, name: str, balance: float = 0) -> None:
        self.__name: str = name
        self.__balance: float = balance
        self.__operations: list = []
