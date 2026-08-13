from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from backend.app.schemas.address import AddressResponse


# ---------------------------------------------------------
# Create User Schema
# ---------------------------------------------------------

class UserCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Full name of the user",
        examples=["Shamita Patil"],
    )

    email: EmailStr = Field(
        ...,
        description="Unique email address",
        examples=["shamita@gmail.com"],
    )

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age of the user",
        examples=[25],
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="User password",
        examples=["Password@123"],
    )


# ---------------------------------------------------------
# User Response Schema
# ---------------------------------------------------------

class UserResponse(BaseModel):

    id: int = Field(
        ...,
        description="Unique user ID",
        examples=[1],
    )

    name: str = Field(
        ...,
        description="Full name",
        examples=["Shamita Patil"],
    )

    email: EmailStr = Field(
        ...,
        description="Registered email",
        examples=["shamita@gmail.com"],
    )

    age: int = Field(
        ...,
        description="User age",
        examples=[25],
    )

    role: str = Field(
        ...,
        description="Role assigned to the user",
        examples=["admin"],
    )

    created_at: datetime = Field(
        ...,
        description="User creation timestamp",
    )

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# Login Schema
# ---------------------------------------------------------

class UserLogin(BaseModel):

    email: EmailStr = Field(
        ...,
        description="Registered email",
        examples=["shamita@gmail.com"],
    )

    password: str = Field(
        ...,
        description="Account password",
        examples=["Password@123"],
    )


# ---------------------------------------------------------
# User with Addresses
# ---------------------------------------------------------

class UserWithAddresses(UserResponse):

    addresses: list[AddressResponse] = Field(
        default=[],
        description="Addresses associated with the user",
    )

    class Config:
        from_attributes = True