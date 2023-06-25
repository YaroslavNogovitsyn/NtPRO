from ntpro.client import Client
from ntpro.extensions import MissedClientName


def get_client(name: str, clients: dict[str, Client]) -> Client:
    if not name:
        raise MissedClientName

    if name not in clients:
        clients[name] = Client(name=name)

    return clients[name]
