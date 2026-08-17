from enum import Enum

from pydantic import BaseModel, Field


class AgentStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    UNKNOWN = "unknown"


class SourceReference(BaseModel):
    source: str
    page: int | str


class AgentResponse(BaseModel):
    status: AgentStatus
    summary: str
    action_required: bool
    sources: list[SourceReference] = Field(
        default_factory=list
    )