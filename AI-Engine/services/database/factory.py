from .postgres import PostgreSQLService


class DatabaseFactory:

    @staticmethod
    def create(database_type, connection):

        if database_type == "postgres":

            return PostgreSQLService(connection)

        raise ValueError(
            "Unsupported database."
        )