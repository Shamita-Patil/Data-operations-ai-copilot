from fastapi import APIRouter

from backend.app.schemas.agent import AgentRequest
from backend.app.services.agent_service import run_agent


router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)


@router.post("/chat")
def chat(request: AgentRequest):

    response = run_agent(
        request.message
    )

    return response