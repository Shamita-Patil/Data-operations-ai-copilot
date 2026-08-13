from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.dependancies.auth import get_current_user
from backend.app.schemas.user import (
    UserCreate,
    UserResponse,
    UserWithAddresses,
)
from backend.app.services.user_service import UserService
from fastapi import APIRouter, Depends, BackgroundTasks
from backend.app.tasks.email_tasks import send_welcome_email

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

service = UserService()


# ---------------------------------------------------------
# Create User
# ---------------------------------------------------------

@router.post(
    "",
    response_model=UserResponse,
    status_code=201,
    summary="Create a new user",
    description="Creates a new user and stores a securely hashed password.",
)
def create_user(
    user: UserCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    created_user = service.create_user(
        db,
        user,
    )

    #background_tasks.add_task(
    #    send_welcome_email,
    #    created_user.email,

    #send_welcome_email.delay(
    #    created_user.email,

    send_welcome_email.apply_async(
        args=[created_user.email],
        countdown=30,
    )


    return created_user

# ---------------------------------------------------------
# Get All Users
# ---------------------------------------------------------

@router.get(
    "",
    response_model=list[UserResponse],
)
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.get_all_users(db)


# ---------------------------------------------------------
# Filter Users
# ---------------------------------------------------------

@router.get(
    "/filter",
    response_model=list[UserResponse],
    summary="Filter users",
    description="Filter users by age and city.",
)
def filter_users(
    age: Optional[int] = None,
    city: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.filter_users(
        db,
        age,
        city,
    )


# ---------------------------------------------------------
# Search Users
# ---------------------------------------------------------

@router.get(
    "/search",
    response_model=list[UserResponse],
    summary="Search users",
    description="Search users by name or email.",
)
def search_users(
    keyword: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.search_users(
        db,
        keyword,
    )


# ---------------------------------------------------------
# Sort Users
# ---------------------------------------------------------

@router.get(
    "/sort",
    response_model=list[UserResponse],
    summary="Sort users",
    description="Returns users sorted by the specified field.",
)
def sort_users(
    sort_by: str = "name",
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.sort_users(
        db,
        sort_by,
    )


# ---------------------------------------------------------
# Paginate Users
# ---------------------------------------------------------

@router.get(
    "/paginate",
    response_model=list[UserResponse],
    summary="Paginate users",
    description="Returns users using page and page size.",
)
def paginate_users(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.paginate_users(
        db,
        page,
        page_size,
    )


# ---------------------------------------------------------
# Users by City (JOIN)
# ---------------------------------------------------------

@router.get(
    "/by-city",
    response_model=list[UserResponse],
    summary="Get users by city",
    description="Returns all users who have an address in the specified city.",
)
def get_users_by_city(
    city: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.get_users_by_city(
        db,
        city,
    )


# ---------------------------------------------------------
# Users with Addresses (joinedload)
# ---------------------------------------------------------

@router.get(
    "/with-addresses",
    response_model=list[UserWithAddresses],
    summary="Get users with addresses",
    description="Returns all users along with their associated addresses.",
)
def get_users_with_addresses(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.get_users_with_addresses(
        db,
    )

@router.get(
    "/with-optional-addresses",
    response_model=list[UserResponse],
)
def get_all_users_with_optional_addresses(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.get_all_users_with_optional_addresses(
        db,
    )


# ---------------------------------------------------------
# Get Single User
# ---------------------------------------------------------

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user by ID",
    description="Returns a single user based on the provided user ID.",
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return service.get_user(
        db,
        user_id,
    )


# ---------------------------------------------------------
# Update User
# ---------------------------------------------------------

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user",
    description="Updates an existing user's information.",
)
def update_user(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return service.update_user(
        db,
        user_id,
        user,
    )


# ---------------------------------------------------------
# Delete User
# ---------------------------------------------------------

@router.delete(
    "/{user_id}",
    status_code=204,
    summary="Delete user",
    description="Deletes a user from the database.",
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    service.delete_user(
        db,
        user_id,
    )

