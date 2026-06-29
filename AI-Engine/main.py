from graph.graph import graph

result = graph.invoke(
    {
        "user_question":
            "Show top five customers"
    }

)


print(result["generated_sql"])