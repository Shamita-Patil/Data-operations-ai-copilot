from sqlalchemy.orm import Session

from backend.app.models.address import Address
from backend.app.schemas.address import AddressCreate


class AddressRepository:

    def create_address(
        self,
        db: Session,
        address: AddressCreate,
    ):
        db_address = Address(
            street=address.street,
            city=address.city,
            state=address.state,
            country=address.country,
            postal_code=address.postal_code,
            user_id=address.user_id,
        )

        db.add(db_address)
        db.commit()
        db.refresh(db_address)

        return db_address

    def get_all_addresses(
        self,
        db: Session,
    ):
        return db.query(Address).all()

    def get_address(
        self,
        db: Session,
        address_id: int,
    ):
        return (
            db.query(Address)
            .filter(Address.id == address_id)
            .first()
        )

    def update_address(
            self,
            db: Session,
            address_id: int,
            address_data: AddressCreate,
    ):
        address = (
            db.query(Address)
            .filter(Address.id == address_id)
            .first()
        )

        if not address:
            return None

        address.street = address_data.street
        address.city = address_data.city
        address.state = address_data.state
        address.country = address_data.country
        address.postal_code = address_data.postal_code
        address.user_id = address_data.user_id

        db.commit()
        db.refresh(address)

        return address

    def get_addresses_by_user(
        self,
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Address)
            .filter(Address.user_id == user_id)
            .all()
        )

    def delete_address(
        self,
        db: Session,
        address_id: int,
    ):
        address = (
            db.query(Address)
            .filter(Address.id == address_id)
            .first()
        )

        if not address:
            return None

        db.delete(address)
        db.commit()

        return address

