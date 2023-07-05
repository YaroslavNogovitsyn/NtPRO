from datetime import datetime

from ntpro.extensions import InvalidDateFormat, DepositAmountMustBeNumber


def validate_amount(amount: str) -> float:
    """Функция проверки вводимого числа"""
    try:
        return float(amount)
    except (TypeError, ValueError):
        raise DepositAmountMustBeNumber


def validate_date(date: str) -> datetime:
    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise InvalidDateFormat

    if not date:
        raise InvalidDateFormat
    return date
