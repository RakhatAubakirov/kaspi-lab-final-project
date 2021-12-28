from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from uuid import UUID

from UserAccount import UserAccount


class ObjectNotFound(ValueError):
    ...


@dataclass
class AccountDatabase(ABC):  # <---- INTERFACE
    def save(self, account: UserAccount) -> None:
        print("I am going to save this:", account)
        return self._save(account=account)

    @abstractmethod
    def _save(self, account: UserAccount) -> None:
        ...

    @abstractmethod
    def clear_all(self) -> None:
        ...

    @abstractmethod
    def get_objects(self) -> List[UserAccount]:
        ...

    @abstractmethod
    def get_object(self, id_: UUID) -> UserAccount:
        ...

    @abstractmethod
    def delete_obj(self, id_: UUID) -> None:
        ...
