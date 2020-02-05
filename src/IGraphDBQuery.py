from abc import ABC, abstractmethod


class IGraphDBQuery(ABC):
    @abstractmethod
    def run_query(self):
        pass

    @abstractmethod
    def set_query(self, query):
        pass