from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Base Address Schema
# ---------------------------------------------------------

class AddressBase(BaseModel):

    street: str = Field(
        ...,
        description="Street address",
        examples=["123 MG Road"],
    )

    city: str = Field(
        ...,
        description="City name",
        examples=["Bangalore"],
    )

    state: str = Field(
        ...,
        description="State name",
        examples=["Karnataka"],
    )

    country: str = Field(
        ...,
        description="Country name",
        examples=["India"],
    )

    postal_code: str = Field(
        ...,
        description="Postal or ZIP code",
        examples=["560001"],
    )


# ---------------------------------------------------------
# Create Address
# ---------------------------------------------------------

class AddressCreate(AddressBase):

    user_id: int = Field(
        ...,
        description="ID of the user who owns this address",
        examples=[1],
    )


# ---------------------------------------------------------
# Address Response
# ---------------------------------------------------------

class AddressResponse(AddressBase):

    id: int = Field(
        ...,
        description="Unique address ID",
        examples=[101],
    )

    user_id: int = Field(
        ...,
        description="Owner user ID",
        examples=[1],
    )

    class Config:
        from_attributes = True