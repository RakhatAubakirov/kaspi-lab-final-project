from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID


class CurrencyError(ValueError):
    pass


@dataclass
class UserAccount:
    id_: Optional[UUID]
    currency: str
    balance: Decimal

    def __lt__(self, other: "Account") -> bool:
        assert isinstance(other, UserAccount)
        if self.currency != other.currency:
            raise CurrencyError
        return self.balance < other.balance

    def print_accounts(self, id_: int, currency: str, balance: Decimal):
        print("Personal Details")
        print("")
        print("Identifier", self.id_)
        print("Currency", self.currency)
        print("Balance", self.balance)



