from datetime import datetime

from prettytable import PrettyTable, prettytable

from ntpro.client import Operation
from ntpro.constants import CommandList
from ntpro.extensions import MissedOperations


class BankStatementTable:
    def __init__(self, operations: list[Operation]):
        self.__operations = operations
        self.__field_names = ['Date', 'Description', 'Withdrawals', 'Deposits', 'Balance']
        self.__total_deposit = 0
        self.__total_withdraw = 0
        self.__current_operations = []

    @staticmethod
    def datetime_to_str(time: datetime) -> str:
        """Функция преобразования времени к строке"""
        return time.strftime('%Y-%m-%d %H:%M:%S')

    def __get_operation(self, operation: Operation):
        if operation.type == CommandList.deposit:
            self.__total_deposit += operation.amount
            self.__current_operations.append(
                [self.datetime_to_str(operation.date),
                 operation.description,
                 '',
                 operation.amount,
                 self.__total_deposit - self.__total_withdraw
                 ]
            )
        elif operation.type == CommandList.withdraw:
            self.__total_withdraw += operation.amount
            self.__current_operations.append(
                [self.datetime_to_str(operation.date),
                 operation.description,
                 operation.amount,
                 '',
                 self.__total_deposit - self.__total_withdraw
                 ]
            )

    def get(self, since: datetime, till: datetime) -> prettytable:
        table = PrettyTable()
        table.field_names = self.__field_names

        for elem in self.__operations:
            if since <= elem.date <= till:
                self.__get_operation(elem)

        if not self.__current_operations:
            raise MissedOperations(self.datetime_to_str(since), self.datetime_to_str(till))

        *transactions, last = self.__current_operations
        table.add_rows(transactions)
        table.add_row(last, divider=True)
        table.add_row(['', 'Totals', self.__total_withdraw, self.__total_deposit,
                       self.__total_deposit - self.__total_withdraw])
        return table
