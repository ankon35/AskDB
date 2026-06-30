class SchemaTool:

    def schema_tool(state):

    schema = state[
        "database_service"
    ].get_schema()

    return {

        "database_schema": schema
    }