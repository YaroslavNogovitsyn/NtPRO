from datetime import datetime

from ntpro.extensions import InvalidDateFormat


def validate_amount(amount: str) -> bool:
    """Функция проверки вводимого числа"""
    return amount.isdigit() and int(amount) > 0


def validate_date(date: str) -> datetime:
    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        raise InvalidDateFormat

    if not date:
        raise InvalidDateFormat
    return date
