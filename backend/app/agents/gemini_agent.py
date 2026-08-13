from typing import Annotated

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI

from backend.app.core.config import settings

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from backend.app.agents.schemas import AgentResponse


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    response: AgentResponse | None



def add_numbers(a: int, b: int) -> int:
    """Add two numbers together and return the result."""

    print("Calculator Tool Executed")

    return a + b

def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together and return the result."""

    print("Multiplication Tool Executed")

    return a * b

def get_user_name() -> str:
    """Return the name of the current user."""

    print("User Lookup Tool Executed")

    return "Shamita"

def analyze_pipeline(message: str) -> AgentResponse:

    response = structured_llm.invoke(
        message
    )

    return response



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.gemini_api_key,
)

structured_llm = llm.with_structured_output(
    AgentResponse
)


llm_with_tools = llm.bind_tools(
    [
        add_numbers,
        multiply_numbers,
        get_user_name,
    ]
)

tool_node = ToolNode(
    [
        add_numbers,
        multiply_numbers,
        get_user_name,
    ]
)

def chatbot_node(state: AgentState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }

def structured_response_node(state: AgentState):

    last_message = state["messages"][-1]

    response = structured_llm.invoke(
        str(last_message.content)
    )

    return {
        "response": response
    }

def route_after_chatbot(state: AgentState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "structured_response"





graph = StateGraph(AgentState)

graph.add_node(
    "chatbot",
    chatbot_node,
)

graph.add_node(
    "tools",
    tool_node,
)

graph.add_node(
    "structured_response",
    structured_response_node,
)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
    "chatbot",
    route_after_chatbot,
    {
        "tools": "tools",
        "structured_response": "structured_response",
    },
)

graph.add_edge(
    "tools",
    "chatbot",
)

graph.add_edge(
    "structured_response",
    END,
)

app = graph.compile()




# if __name__ == "__main__":
#
#     result = app.invoke(
#         {
#             "messages": [
#                 (
#                     "human",
#                     "Explain what LangGraph is in one sentence."
#                 )
#             ]
#         }
#     )
#
#     for message in result["messages"]:
#         print("\n---")
#         print(message)


# if __name__ == "__main__":
#
#     response = analyze_pipeline(
#         "The supplier XML ingestion pipeline failed "
#         "because 3 records could not be processed."
#     )
#
#     print(response)
#     print(type(response))


if __name__ == "__main__":

    result = app.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is 25 + 17?"
                }
            ]
        }
    )

    print(result)