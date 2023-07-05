from datetime import datetime

import pytest
from prettytable import PrettyTable

from ntpro.client import Client, Operation
from ntpro.constants import CommandList
from ntpro.extensions import (DepositAmountMustBeNumber, InsufficientFunds,
                              InvalidDateFormat, MissedClientName,
                              MissedCommandName, MissedOperations,
                              UnknownCommand)
from ntpro.main import parse
from ntpro.statement_table import BankStatementTable
from ntpro.utils import get_client
from ntpro.validators import validate_amount, validate_date


class TestRowCommandParser:
    def test_missed_command_name(self):
        with pytest.raises(MissedCommandName):
            parse('')

    def test_unknown_command_name(self):
        for arg in ' ', 'qwe', 'qwe ':
            with pytest.raises(UnknownCommand):
                parse(arg)

    def test_with_right_param(self):
        test_cases = [
            (
                'deposit --amount=100 --description="asd"',
                ('deposit', ['amount=100', 'description="asd"']),
            ),
            (
                'withdraw --amount=111.11',
                ('withdraw', ['amount=111.11']),
            )
        ]
        for row_command, result in test_cases:
            assert result == parse(row_command)


class TestAmountValidator:
    def test_worse(self):
        for arg in 'hh', None, '576er', '124.5435.234':
            with pytest.raises(DepositAmountMustBeNumber):
                validate_amount(arg)

    def test_right(self):
        for arg in 1, 32, -100, 43, 23.5, '1241.634', '34234.5435':
            validate_amount(arg)


class TestDataValidator:

    def test_worse(self):
        for arg in '', '543-654645654-32423', '2053-66-44', 'fdsgdsdsg':
            with pytest.raises(InvalidDateFormat):
                validate_date(arg)

    def test_right(self):
        for arg in '2023-07-05', '2023 07 05', '2023-07-05 17:00:00', '05.07.2023':
            validate_date(arg)


class TestGetClient:
    def test_no_client_in_args(self):
        with pytest.raises(MissedClientName):
            get_client('', {})

    def test_client(self):
        a = 'Some_name'
        clients = {}
        client = get_client({'client': a}.pop('client'), clients)
        print(client.name, type(client))
        assert isinstance(client, Client)
        assert client.name in clients
        assert client.name == a
        assert client.balance == 0

        assert get_client({'client': a}.pop('client'), clients) == client


class TestStatementTable:

    def test_table_worse(self):
        with pytest.raises(MissedOperations):
            BankStatementTable([]).get(
                datetime.now(),
                datetime.now()
            )

    def test_table_right(self):
        assert isinstance(
            BankStatementTable([Operation(amount=100.0,
                                          date=datetime(2023, 7, 5, 18, 35, 14, 364800),
                                          description='ATM Deposit',
                                          type='deposit')]
                               ).get(
                datetime(2023, 7, 4, 18, 35, 14, 364800),
                datetime(2023, 7, 6, 18, 35, 14, 364800),
            ), PrettyTable)


class TestClient:

    def test_create_client(self):
        name = 'some_name'
        client = Client(name)
        assert client.name == name
        assert client.balance == 0
        assert client.operations == []

    def test_create_deposit(self):
        client = Client('some_name')
        amount = 111
        description = 'test-desc'
        client.deposit(amount, description)
        assert client.balance == amount
        assert len(client.operations) == 1
        operation = client.operations[0]
        assert isinstance(operation, Operation)
        assert operation.amount == amount
        assert operation.description == description
        assert operation.type == CommandList.deposit

    def test_create_withdraw_worse(self):
        with pytest.raises(InsufficientFunds):
            client = Client('some_name')
            amount = 111
            description = 'test-desc'
            client.withdraw(amount, description)

    def test_create_withdraw_right(self):
        client = Client('some_name')
        amount = 111
        description = 'test-desc'
        client.deposit(amount, description)
        assert client.balance == amount
        client.withdraw(amount, description)
        assert client.balance == 0
        assert len(client.operations) == 2
        operation = client.operations[1]
        assert isinstance(operation, Operation)
        assert operation.amount == amount
        assert operation.description == description
        assert operation.type == CommandList.withdraw

    def test_do_many_operations(self):
        client = Client('some_name')
        amount = 123
        for _ in range(4):
            client.deposit(amount, '')
        for _ in range(2):
            client.withdraw(amount, '')
        assert client.balance == amount * 2
        assert len(client.operations) == 6
