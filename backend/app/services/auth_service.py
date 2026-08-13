from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.repositories.user_repository import UserRepository
from backend.app.utils.security import verify_password
from backend.app.utils.jwt import create_access_token


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):
        user = self.repository.get_user_by_email(
            db,
            email,
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

        if not verify_password(
            password,
            user.password,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

        access_token = create_access_token(
            data={
                "sub": user.email,
                "role": user.role,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }