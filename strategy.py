from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class IteratorStrategy(Strategy):
    def execute(self) -> str:
        return "IteratorStrategy"


class FileStrategy(Strategy):
    def execute(self) -> str:
        return "FileStrategy"
