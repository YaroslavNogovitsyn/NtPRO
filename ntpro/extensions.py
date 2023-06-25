class MissedCommandName(Exception):
    """No entered the command name."""


class UnknownCommand(Exception):
    """Entered unknown command."""


class DepositAmountMustBeNumber(Exception):
    """Amount must be a positive integer number."""


class MissedClientName(Exception):
    """Didn't enter a client name."""


class InsufficientFunds(Exception):
    """Insufficient funds to withdraw"""


class InvalidDateFormat(Exception):
    """Entered invalid date format."""


class MissedOperations(Exception):
    def __init__(self, since, till):
        self.since = since
        self.till = till

    def __str__(self):
        return f"""For this period(since {self.since} - till {self.till}) this client did not have any transactions'"""
