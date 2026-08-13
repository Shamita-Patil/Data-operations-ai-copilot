from pydantic import BaseModel, Field


# ---------------------------------------------------------
# JWT Token Response
# ---------------------------------------------------------

class Token(BaseModel):

    access_token: str = Field(
        ...,
        description="JWT access token used to authenticate API requests",
        examples=[
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        ],
    )

    token_type: str = Field(
        ...,
        description="Authentication scheme",
        examples=["bearer"],
    )