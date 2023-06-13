from ntpro.extensions import MissedCommandName, UnknownCommand


def parse(command_line: str) -> (str, list[str]):
    """Получить название операции и ключевые слова со значениями"""

    command_name, *command_args = commands = command_line.split(' -')

    if not command_name:
        raise MissedCommandName

    if commands[0] not in ('deposit', 'withdraw', 'show_bank_statement'):
        raise UnknownCommand

    return command_name, command_args


def print_help() -> None:
    """Функция вывода подсказок"""
    print('''
Commands:
• deposit - 
    required arguments: client (str), amount (float), description (str)
    example: 
    deposit --client="John Jones" --amount=100 --description="ATM Deposit"
• withdraw 
    required arguments: client (str), amount (float), description (str)
    example: 
    withdraw --client="John Jones" --amount=100 --description="ATM Withdrawal"
• show_bank_statement 
    required arguments: client (str), since (str, dateformat %Y-%m-%d %H:%M:%S), till (str, dateformat %Y-%m-%d %H:%M:%S)
    example: 
    show_bank_statement --client="John Jones" --since="2022-03-01 00:00:00" --till="2024-01-01 00:00:00"
• exit
''')


def main():
    print('Service started!')
    print_help()

    while True:
        command_line = input('> ').strip()
        command_name, command_args = parse(command_line)


if __name__ == '__main__':
    main()
