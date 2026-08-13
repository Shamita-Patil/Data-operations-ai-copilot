from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.auth import Token
from backend.app.services.auth_service import AuthService

router = APIRouter(
    tags=["Authentication"],
)

service = AuthService()


@router.post(
    "/login",
    response_model=Token,
    summary="User Login",
    description="""
Authenticate a registered user using email and password.

On successful authentication, a JWT access token is returned.

The token must be supplied in the Authorization header as:

Bearer <access_token>
""",
    operation_id="loginUser",
    responses={
        200: {
            "description": "Login successful",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "token_type": "bearer"
                    }
                }
            }
        },
        401: {
            "description": "Invalid email or password"
        },
        422: {
            "description": "Validation Error"
        }
    },
    openapi_extra={
        "requestBody": {
            "content": {
                "application/x-www-form-urlencoded": {
                    "example": {
                        "username": "shamita@gmail.com",
                        "password": "Password@123"
                    }
                }
            }
        }
    }
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return service.login(
        db,
        form_data.username,
        form_data.password,
    )