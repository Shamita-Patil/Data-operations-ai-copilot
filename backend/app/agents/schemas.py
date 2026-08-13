from enum import Enum
from pydantic import BaseModel



class AgentStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    UNKNOWN = "unknown"


class AgentResponse(BaseModel):
    status: AgentStatus
    summary: str
    action_required: bool