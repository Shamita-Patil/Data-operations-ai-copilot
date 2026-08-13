from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.dependancies.auth import get_current_user
from backend.app.schemas.address import (
    AddressCreate,
    AddressResponse,
)
from backend.app.services.address_service import AddressService

router = APIRouter(
    prefix="/addresses",
    tags=["Addresses"],
)

service = AddressService()


# ---------------------------------------------------------
# Create Address
# ---------------------------------------------------------

@router.post(
    "",
    response_model=AddressResponse,
    status_code=201,
    summary="Create Address",
    description="Creates a new address for a user.",
    operation_id="createAddress",
    responses={
        201: {
            "description": "Address created successfully"
        },
        404: {
            "description": "User not found"
        },
        422: {
            "description": "Validation Error"
        },
    },
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "example": {
                        "street": "123 MG Road",
                        "city": "Bangalore",
                        "state": "Karnataka",
                        "country": "India",
                        "postal_code": "560001",
                        "user_id": 1
                    }
                }
            }
        }
    },
)
def create_address(
    address: AddressCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.create_address(
        db,
        address,
    )


# ---------------------------------------------------------
# Get All Addresses
# ---------------------------------------------------------

@router.get(
    "",
    response_model=list[AddressResponse],
    summary="Get All Addresses",
    description="Returns every address stored in the system.",
    operation_id="getAllAddresses",
    responses={
        200: {
            "description": "Addresses retrieved successfully"
        },
        401: {
            "description": "Unauthorized"
        },
    },
)
def get_addresses(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.get_all_addresses(db)


# ---------------------------------------------------------
# Get Address by ID
# ---------------------------------------------------------

@router.get(
    "/{address_id}",
    response_model=AddressResponse,
    summary="Get Address",
    description="Returns an address by its ID.",
    operation_id="getAddressById",
    responses={
        200: {
            "description": "Address found"
        },
        404: {
            "description": "Address not found"
        },
    },
)
def get_address(
    address_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.get_address(
        db,
        address_id,
    )


# ---------------------------------------------------------
# Update Address
# ---------------------------------------------------------

@router.put(
    "/{address_id}",
    response_model=AddressResponse,
    summary="Update Address",
    description="Updates an existing address.",
    operation_id="updateAddress",
    responses={
        200: {
            "description": "Address updated successfully"
        },
        404: {
            "description": "Address not found"
        },
        422: {
            "description": "Validation Error"
        },
    },
)
def update_address(
    address_id: int,
    address: AddressCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.update_address(
        db,
        address_id,
        address,
    )


# ---------------------------------------------------------
# Delete Address
# ---------------------------------------------------------

@router.delete(
    "/{address_id}",
    status_code=204,
    summary="Delete Address",
    description="Deletes an address.",
    operation_id="deleteAddress",
    responses={
        204: {
            "description": "Address deleted successfully"
        },
        404: {
            "description": "Address not found"
        },
    },
)
def delete_address(
    address_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service.delete_address(
        db,
        address_id,
    )