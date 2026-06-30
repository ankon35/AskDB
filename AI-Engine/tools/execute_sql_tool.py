def execute_sql(state):

    result = state[
        "database_service"
    ].execute_query(

        state["generated_sql"]

    )

    return {

        "query_result": result
    }