from typing import Annotated

from typing_extensions import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from backend.app.core.config import settings
from backend.app.agents.schemas import AgentResponse
from backend.app.rag.rag_tool import search_enterprise_knowledge


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    response: AgentResponse | None


# ============================================================
# TOOLS
# ============================================================

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


# ============================================================
# LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.gemini_api_key,
)


# ============================================================
# STRUCTURED OUTPUT LLM
# ============================================================

structured_llm = llm.with_structured_output(
    AgentResponse
)


# ============================================================
# TOOL REGISTRATION
# ============================================================

tools = [
    add_numbers,
    multiply_numbers,
    get_user_name,
    search_enterprise_knowledge,
]


llm_with_tools = llm.bind_tools(
    tools
)


tool_node = ToolNode(
    tools
)


# ============================================================
# OPTIONAL PIPELINE ANALYSIS FUNCTION
# ============================================================

def analyze_pipeline(message: str) -> AgentResponse:

    response = structured_llm.invoke(
        message
    )

    return response


# ============================================================
# CHATBOT NODE
# ============================================================

def chatbot_node(state: AgentState):

    system_message = """
You are an enterprise Data Operations AI assistant.

Use the search_enterprise_knowledge tool when:
- the user asks about internal documents,
- SOPs,
- runbooks,
- internal processes,
- incident procedures,
- XML/data pipeline documentation,
- or other enterprise knowledge.

Do not use the tool for simple calculations,
general conversation, or questions that do not require
enterprise documents.

When the retrieval tool is used, base the answer on
the retrieved information and do not invent facts.
"""

    messages = [
        {
            "role": "system",
            "content": system_message,
        },
        *state["messages"],
    ]

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages": [response]
    }


# ============================================================
# STRUCTURED RESPONSE NODE
# ============================================================

def structured_response_node(
    state: AgentState,
):

    messages = state["messages"]

    last_message = messages[-1]

    response = structured_llm.invoke(
        [
            {
                "role": "system",
                "content": """
You are the final response formatter for an
enterprise Data Operations AI assistant.

When retrieved enterprise documents are present:

1. Answer using only the retrieved information.
2. Do not invent facts.
3. Include source references when available.
4. Use the page number provided by the retrieval tool.
5. If the retrieved context does not contain the answer,
   clearly state that the available documents do not
   provide enough information.

Return a concise, accurate response.
""",
            },
            {
                "role": "user",
                "content": str(last_message.content),
            },
        ]
    )

    return {
        "response": response
    }


# ============================================================
# ROUTING
# ============================================================

def route_after_chatbot(
    state: AgentState,
):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "structured_response"


# ============================================================
# GRAPH
# ============================================================

graph = StateGraph(
    AgentState
)


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


graph.set_entry_point(
    "chatbot"
)


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


# ============================================================
# LOCAL TEST
# ============================================================

if __name__ == "__main__":

    result = app.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "According to the document, what is discussed about RAG and LangChain?",
                }
            ],
            "response": None,
        }
    )

    print("\n==============================")
    print("FINAL RESULT")
    print("==============================")

    print(result)

    print("\n==============================")
    print("MESSAGES")
    print("==============================")

    for message in result["messages"]:

        print("\n---")
        print(message)