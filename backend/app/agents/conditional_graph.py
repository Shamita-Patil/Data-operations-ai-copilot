from typing import TypedDict
from langgraph.graph import StateGraph

# -----------------------------------
# State
# -----------------------------------
class GraphState(TypedDict):
    message: str

# -----------------------------------
# Nodes
# -----------------------------------


def greeting_node(state: GraphState):

    print("Greeting Node")

    return{
        "message": f"Hello {state['message']}"
    }

def normal_node(state: GraphState):

    print("Normal Node")

    return state

def uppercase_node(state: GraphState):

    print("Uppercase Node")

    return{
        "message": state['message'].upper()
    }

def decide_route(state: GraphState):

    if len(state['message']) > 15:
        return "uppercase"

    return "normal"

graph = StateGraph(GraphState)

graph.add_node(
    "greeting",
    greeting_node,
)

graph.add_node(
    "normal",
    normal_node,
)

graph.add_node(
    "uppercase",
    uppercase_node,
)

graph.set_entry_point("greeting")

graph.add_conditional_edges(
    "greeting",
           decide_route,
)

graph.set_finish_point("normal")
graph.set_finish_point("uppercase")

app = graph.compile()

result = app.invoke(
    {
        "message": "ShriHarishchandra"
    }
)

print(result)





