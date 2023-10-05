from abc import abstractmethod, ABC


class Solution(ABC):
    _raw: dict = None

    def __init__(self, raw: dict):
        self._raw = raw

    def raw(self):
        return self._raw.copy()

    @abstractmethod
    def as_txt(self) -> str:
        ...


class Resolver(ABC):

    @staticmethod
    @abstractmethod
    def resolve(*args, **kwargs) -> Solution:
        ...
