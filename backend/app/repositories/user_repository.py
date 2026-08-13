from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.models.address import Address
from backend.app.schemas.user import UserCreate
from typing import Optional
from sqlalchemy import asc, desc
from sqlalchemy.orm import joinedload

class UserRepository:

    def create_user(
        self,
        db: Session,
        user: UserCreate,
    ):

        db_user = User(
            name=user.name,
            email=user.email,
            age=user.age,
            password=user.password,
            role="user",
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    def get_all_users(
        self,
        db: Session,
    ):

        return db.query(User).all()

    def get_user(
        self,
        db: Session,
        user_id: int,
    ):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def update_user(
        self,
        db: Session,
        user_id: int,
        user: UserCreate,
    ):

        db_user = self.get_user(db, user_id)

        if not db_user:
            return None

        db_user.name = user.name
        db_user.email = user.email
        db_user.age = user.age
        db_user.password = user.password

        db.commit()
        db.refresh(db_user)

        return db_user

    def delete_user(
        self,
        db: Session,
        user_id: int,
    ):

        db_user = self.get_user(db, user_id)

        if not db_user:
            return False

        db.delete(db_user)
        db.commit()

        return True

    def get_user_by_email(
        self,
        db: Session,
        email: str,
    ):

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_users_by_age(
            self,
            db: Session,
            age: int,
    ):
        return (
            db.query(User)
            .filter(User.age == age)
            .all()
        )

    def filter_users(
            self,
            db: Session,
            age: Optional[int] = None,
            city: Optional[str] = None,
    ):
        query = db.query(User)

        if age is not None:
            query = query.filter(User.age == age)

        if city is not None:
            query = query.filter(User.city == city)

        return query.all()

    def search_users(
            self,
            db: Session,
            keyword: str,
    ):
        return (
            db.query(User)
            .filter(
                User.name.ilike(f"%{keyword}%")
            )
            .all()
        )

    def sort_users(
            self,
            db: Session,
            sort_by: str,
    ):
        query = db.query(User)

        descending = False

        if sort_by.startswith("-"):
            descending = True
            sort_by = sort_by[1:]

        allowed_columns = {
            "name": User.name,
            "age": User.age,
            #"city": User.city,
            "email": User.email,
            "role": User.role,
            "phone_number": User.phone_number,
            "created_at": User.created_at,
        }

        column = allowed_columns.get(sort_by)

        if column is None:
            return query.all()

        if descending:
            query = query.order_by(desc(column))
        else:
            query = query.order_by(asc(column))

        return query.all()

    def paginate_users(
            self,
            db: Session,
            page: int,
            page_size: int,
    ):
        offset = (page - 1) * page_size

        return (
            db.query(User)
            .offset(offset)
            .limit(page_size)
            .all()
        )

    def get_users_by_city(
            self,
            db: Session,
            city: str,
    ):
        return (
            db.query(User)
            .join(Address)
            .filter(Address.city == city)
            .all()
        )

    def get_users_with_addresses(
            self,
            db: Session,
    ):
        return (
            db.query(User)
            .options(
                joinedload(User.addresses)
            )
            .all()
        )

    def get_all_users_with_optional_addresses(
            self,
            db: Session,
    ):
        return (
            db.query(User)
            .outerjoin(Address)
            .all()
        )

