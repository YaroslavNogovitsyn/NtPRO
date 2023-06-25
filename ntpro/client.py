from dataclasses import dataclass
from datetime import datetime

from ntpro.constants import CommandList
from ntpro.extensions import InsufficientFunds


@dataclass
class Operation:
    amount: float
    date: datetime
    description: str
    type: str


class Client:
    def __init__(self, name: str, balance: float = 0) -> None:
        self.__name: str = name
        self.__balance: float = balance
        self.__operations: list = []

    @property
    def operations(self):
        return self.__operations

    def __add_operation(self, operation_name: str, amount: float, description: str) -> None:
        self.__operations.append(Operation(
            amount=amount,
            description=description,
            date=datetime.now(),
            type=operation_name,
        ))

    def deposit(self, amount: float, description: str = '') -> None:
        self.__balance += amount
        self.__add_operation(CommandList.deposit, amount, description)

    def withdraw(self, amount: float, description: str = '') -> None:
        if self.__balance < amount:
            raise InsufficientFunds
        self.__balance -= amount
        self.__add_operation(CommandList.withdraw, amount, description)
