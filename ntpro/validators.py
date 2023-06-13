def validate_amount(amount: str) -> bool:
    """Функция проверки вводимого числа"""
    return amount.isdigit() and int(amount) > 0
