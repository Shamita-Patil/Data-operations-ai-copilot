from typing import TypedDict
from langgraph.graph import StateGraph

# -----------------------------------
# State
# -----------------------------------
class GraphState(TypedDict):
    number1: int
    number2: int
    result: int

# -----------------------------------
# Nodes
# -----------------------------------

def add_numbers(a: int, b: int):

    print("calculator tool executed")

    return a + b


def calculator_node(state: GraphState):

    answer = add_numbers(
        state["number1"],
        state["number2"],
    )

    return{
        "result": answer
    }

graph = StateGraph(GraphState)

graph.add_node(
    "calculator",
    calculator_node,
)

graph.set_entry_point("calculator")
graph.set_finish_point("calculator")
app = graph.compile()

result = app.invoke(
    {
        "number1": 25,
        "number2": 17,
        "result": 0
    }
)

print(result)