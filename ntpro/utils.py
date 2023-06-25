from ntpro.client import Client
from ntpro.constants import CommandList
from ntpro.extensions import MissedClientName


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

    # здесь будет логика вызова show_bank_statement
