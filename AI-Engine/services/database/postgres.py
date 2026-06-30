from .base import BaseDatabaseService


class PostgreSQLService(BaseDatabaseService):

    def __init__(self, connection):
        self.connection = connection

    def execute_query(self, sql: str):

        ...

    def get_schema(self):

        ...

    def test_connection(self):

        ...