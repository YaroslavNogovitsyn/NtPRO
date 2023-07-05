import pytest

from ntpro.extensions import MissedCommandName, UnknownCommand, DepositAmountMustBeNumber, InvalidDateFormat
from ntpro.main import parse
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
        for arg in '', '36-45654654642-4234', '2053-66-44':
            with pytest.raises(InvalidDateFormat):
                validate_date(arg)

