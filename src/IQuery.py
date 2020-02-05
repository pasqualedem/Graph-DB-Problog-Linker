from abc import ABC, abstractmethod


class IQuery(ABC):
    @abstractmethod
    def run_query(self):
        pass

    @abstractmethod
    def set_query(self):
        pass