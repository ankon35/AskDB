def sql_validation_router(state):

    if state["is_sql_valid"]:

        return "execute_sql"

    return END