class MissedCommandName(Exception):
    """No entered the command name."""


class UnknownCommand(Exception):
    """Entered unknown command."""


class DepositAmountMustBeNumber(Exception):
    """Amount must be a positive integer number."""
