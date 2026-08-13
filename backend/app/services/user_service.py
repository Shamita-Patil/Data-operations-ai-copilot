from sqlalchemy.orm import Session

from backend.app.core.logger import logger
from backend.app.exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
)
from backend.app.repositories.user_repository import UserRepository
from backend.app.schemas.user import UserCreate
from backend.app.utils.security import hash_password
from backend.app.cache.cache_service import CacheService
from typing import Optional
from backend.app.core.logger import logger

class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        user: UserCreate,
    ):
        # Check if email already exists
        existing_user = self.repository.get_user_by_email(
            db,
            user.email,
        )

        if existing_user:
            logger.warning(
                f"Duplicate registration attempt | email={user.email}"
            )
            raise UserAlreadyExistsException()

        # Hash password before saving
        user.password = hash_password(user.password)

        created_user = self.repository.create_user(
            db,
            user,
        )

        logger.info(
            f"User created successfully | id={created_user.id} | email={created_user.email}"
        )

        return created_user

    def get_all_users(
        self,
        db: Session,
    ):
        users = self.repository.get_all_users(db)

        logger.info(
            f"Fetched all users | count={len(users)}"
        )

        return users

    def get_user(
            self,
            db: Session,
            user_id: int,
    ):
        cache_key = f"user:{user_id}"

        # Check Redis Cache
        cached_user = CacheService.get(
            cache_key,
        )

        if cached_user:
            logger.info(
                f"Cache HIT | user_id={user_id}"
            )
            return cached_user

        logger.info(
            f"Cache MISS | user_id={user_id}"
        )

        # Fetch from Database
        user = self.repository.get_user(
            db,
            user_id,
        )

        if not user:
            logger.warning(
                f"User not found | id={user_id}"
            )
            raise UserNotFoundException()

        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age,
            "role": user.role,
            "phone_number": user.phone_number,
            "created_at": user.created_at.isoformat(),
        }

        CacheService.set(
            cache_key,
            user_data,
        )

        logger.info(
            f"User cached successfully | id={user.id}"
        )

        logger.info(
            f"User fetched from database | id={user.id}"
        )

        return user

    def update_user(
            self,
            db: Session,
            user_id: int,
            user: UserCreate,
    ):
        updated = self.repository.update_user(
            db,
            user_id,
            user,
        )

        if not updated:
            logger.warning(
                f"User not found during update | id={user_id}"
            )
            raise UserNotFoundException()

        # Invalidate Redis Cache
        CacheService.delete(
            f"user:{user_id}"
        )

        logger.info(
            f"Cache invalidated | user_id={user_id}"
        )

        logger.info(
            f"User updated successfully | id={updated.id}"
        )

        return updated

    def delete_user(
            self,
            db: Session,
            user_id: int,
    ):
        deleted = self.repository.delete_user(
            db,
            user_id,
        )

        if not deleted:
            logger.warning(
                f"User not found during delete | id={user_id}"
            )
            raise UserNotFoundException()

        # Remove from Redis cache
        CacheService.delete(
            f"user:{user_id}"
        )

        logger.info(
            f"Cache invalidated | user_id={user_id}"
        )

        logger.info(
            f"User deleted successfully | id={user_id}"
        )

        return deleted

    def get_users_by_age(
            self,
            db: Session,
            age: int,
    ):
        return self.repository.get_users_by_age(
            db,
            age,
        )

    def filter_users(
            self,
            db: Session,
            age: Optional[int] = None,
            city: Optional[str] = None,
    ):
        return self.repository.filter_users(
            db,
            age,
            city,
        )

    def search_users(
            self,
            db: Session,
            keyword: str,
    ):
        return self.repository.search_users(
            db,
            keyword,
        )

    def sort_users(
            self,
            db: Session,
            sort_by: str,
    ):
        return self.repository.sort_users(
            db,
            sort_by,
        )

    def paginate_users(
            self,
            db: Session,
            page: int,
            page_size: int,
    ):
        return self.repository.paginate_users(
            db,
            page,
            page_size,
        )

    def get_users_by_city(
            self,
            db: Session,
            city: str,
    ):
        return self.repository.get_users_by_city(
            db,
            city,
        )

    def get_users_with_addresses(
            self,
            db: Session,
    ):
        return self.repository.get_users_with_addresses(
            db,
        )

    def get_all_users_with_optional_addresses(
            self,
            db: Session,
    ):
        return self.repository.get_all_users_with_optional_addresses(
            db,
        )