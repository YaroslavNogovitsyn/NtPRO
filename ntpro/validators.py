from datetime import datetime

import dateparser

from ntpro.extensions import DepositAmountMustBeNumber, InvalidDateFormat


def validate_amount(amount: str) -> float:
    """Функция проверки вводимого числа"""
    try:
        return float(amount)
    except (TypeError, ValueError):
        raise DepositAmountMustBeNumber


def validate_date(date: str) -> datetime:
    try:
        date = dateparser.parse(date)
    except ValueError:
        raise InvalidDateFormat

    if not date:
        raise InvalidDateFormat
    return date
