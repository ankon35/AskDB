from abc import ABC, abstractmethod


class BaseDatabaseService(ABC):

    @abstractmethod
    def execute_query(self, sql: str):
        pass

    @abstractmethod
    def get_schema(self):
        pass

    @abstractmethod
    def test_connection(self):
        pass