import logging

from ntpro.extensions import (DepositAmountMustBeNumber, InsufficientFunds,
                              InvalidDateFormat, MissedClientName,
                              MissedCommandName, MissedOperations,
                              UnknownCommand)
from ntpro.utils import do_command, get_client
from ntpro.validators import validate_amount


def find_args(keywords: list) -> bool | dict:
    """Парсинг и сохранение значений"""

    dct = {}
    for elem in keywords:
        key, value = elem.strip('-').replace('"', '').split('=')
        if key == 'amount':
            value = validate_amount(value)
        dct[key] = value
    return dct


def parse(command_line: str) -> (str, list[str]):
    """Получить название операции и ключевые слова со значениями"""

    command_name, *command_args = commands = command_line.split(' --')

    if not command_name:
        raise MissedCommandName

    if commands[0] not in ('deposit', 'withdraw', 'show_bank_statement'):
        raise UnknownCommand

    return command_name, command_args


def print_help() -> None:
    """Функция вывода подсказок"""
    logging.info('''
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
    logging.info('Service started!')
    print_help()
    clients = {}

    while True:
        try:
            command_name, command_args = parse(input('> ').strip())
            if command_name.lower() == 'exit':
                break

            args = find_args(command_args)
            client = get_client(args.pop('client', None), clients)

            if info := do_command(client, command_name, args):
                logging.info(info)

        except MissedCommandName as ex:
            logging.error(ex.__doc__)
        except UnknownCommand as ex:
            logging.error(ex.__doc__)
        except DepositAmountMustBeNumber as ex:
            logging.error(ex.__doc__)
        except MissedClientName as ex:
            logging.error(ex.__doc__)
        except TypeError as ex:
            logging.error(ex.__doc__)
        except InsufficientFunds as ex:
            logging.error(ex.__doc__)
        except InvalidDateFormat as ex:
            logging.error(ex.__doc__)
        except MissedOperations as ex:
            logging.error(ex)
        except KeyboardInterrupt:
            logging.info('Finish')
            break


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    main()
