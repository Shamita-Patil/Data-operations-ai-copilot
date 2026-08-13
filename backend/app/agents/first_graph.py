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

    print("Greeting Node Executed")

    return{
        "message":f"Hello {state['message']}"
    }

def uppercase_node(state: GraphState):
    print("Uppercase Node Executed")

    return{
        "message": state["message"].upper()
    }

# -----------------------------------
# Build Graph
# -----------------------------------

graph = StateGraph(GraphState)

graph.add_node(
    "greeting",
    greeting_node,
)

graph.add_node(
    "uppercase",
    uppercase_node,
)

graph.set_entry_point("greeting")

graph.add_edge(
    "greeting",
    "uppercase",
)

graph.set_finish_point("uppercase")

# -----------------------------------
# Compile Graph
# -----------------------------------

app = graph.compile()

# -----------------------------------
# Execute Graph
# -----------------------------------

result = app.invoke(
    {
        "message": "Shamita"
    }
)

print(result)

