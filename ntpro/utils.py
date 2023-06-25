from ntpro.client import Client
from ntpro.constants import CommandList
from ntpro.extensions import MissedClientName
from ntpro.statement_table import BankStatementTable
from ntpro.validators import validate_date


def get_client(name: str, clients: dict[str, Client]) -> Client:
    if not name:
        raise MissedClientName

    if name not in clients:
        clients[name] = Client(name=name)

    return clients[name]


def do_command(client: Client, command: str, args: dict) -> str | None:
    if command == CommandList.deposit:
        client.deposit(**args)
        return 'Deposit operation was successful!'

    if command == CommandList.withdraw:
        client.withdraw(**args)
        return 'Withdrawal operation was successful!'

    if command == CommandList.show_bank_statement:
        kwargs = {key: validate_date(args.pop(key, '')) for key in ('since', 'till')}
        statement_table = BankStatementTable(client.operations)
        print(statement_table.get(**kwargs))
