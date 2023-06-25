from datetime import datetime


class BankStatementTable:
    def __init__(self, operations):
        self.__operations = operations
        self.__field_names = ['Date', 'Description', 'Withdrawals', 'Deposits', 'Balance']

    def get(self, since: datetime, till: datetime) -> str:
        pass
