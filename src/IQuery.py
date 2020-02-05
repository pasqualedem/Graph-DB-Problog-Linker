from abc import ABC, abstractmethod


class IQuery(ABC):
    @abstractmethod
    def run_query():
        pass

    @abstractmethod
    def set_query():
        pass