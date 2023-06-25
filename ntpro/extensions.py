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
