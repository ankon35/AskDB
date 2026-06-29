from graph.graph import graph


class SQLAgentService:

    def __init__(self):

        self.graph = graph

    def run(self, question):

        initial_state = {

            "user_question": question,

            "database_schema": None,

            "generated_sql": None,

            "query_result": None,

            "final_answer": None,

            "error": None,

            "retry_count": 0,
        }

        return self.graph.invoke(
            initial_state
        )