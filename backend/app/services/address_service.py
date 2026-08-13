from sqlalchemy.orm import Session

from backend.app.core.logger import logger
from backend.app.exceptions.custom_exceptions import (
    UserNotFoundException,
    AddressNotFoundException,
)
from backend.app.repositories.address_repository import AddressRepository
from backend.app.repositories.user_repository import UserRepository
from backend.app.schemas.address import AddressCreate


class AddressService:

    def __init__(self):
        self.address_repository = AddressRepository()
        self.user_repository = UserRepository()

    def create_address(
        self,
        db: Session,
        address: AddressCreate,
    ):
        # Check whether the user exists
        user = self.user_repository.get_user(
            db,
            address.user_id,
        )

        if not user:
            logger.warning(
                f"Address creation failed | user_id={address.user_id} not found"
            )
            raise UserNotFoundException()

        created_address = self.address_repository.create_address(
            db,
            address,
        )

        logger.info(
            f"Address created successfully | id={created_address.id} | user_id={created_address.user_id}"
        )

        return created_address

    def get_all_addresses(
        self,
        db: Session,
    ):
        addresses = self.address_repository.get_all_addresses(db)

        logger.info(
            f"Fetched all addresses | count={len(addresses)}"
        )

        return addresses

    def get_address(
        self,
        db: Session,
        address_id: int,
    ):
        address = self.address_repository.get_address(
            db,
            address_id,
        )

        if not address:
            logger.warning(
                f"Address not found | id={address_id}"
            )
            raise AddressNotFoundException()

        logger.info(
            f"Address fetched | id={address.id}"
        )

        return address

    def get_addresses_by_user(
        self,
        db: Session,
        user_id: int,
    ):
        # Verify the user exists
        user = self.user_repository.get_user(
            db,
            user_id,
        )

        if not user:
            logger.warning(
                f"User not found while fetching addresses | user_id={user_id}"
            )
            raise UserNotFoundException()

        addresses = self.address_repository.get_addresses_by_user(
            db,
            user_id,
        )

        logger.info(
            f"Fetched addresses for user | user_id={user_id} | count={len(addresses)}"
        )

        return addresses

    def update_address(
            self,
            db: Session,
            address_id: int,
            address: AddressCreate,
    ):
        existing_address = self.address_repository.get_address(
            db,
            address_id,
        )

        if not existing_address:
            logger.warning(
                f"Address not found during update | id={address_id}"
            )
            raise AddressNotFoundException()

        user = self.user_repository.get_user(
            db,
            address.user_id,
        )

        if not user:
            logger.warning(
                f"User not found during address update | user_id={address.user_id}"
            )
            raise UserNotFoundException()

        updated_address = self.address_repository.update_address(
            db,
            address_id,
            address,
        )

        logger.info(
            f"Address updated successfully | id={address_id}"
        )

        return updated_address

    def delete_address(
        self,
        db: Session,
        address_id: int,
    ):
        deleted = self.address_repository.delete_address(
            db,
            address_id,
        )

        if not deleted:
            logger.warning(
                f"Address not found during delete | id={address_id}"
            )
            raise AddressNotFoundException()

        logger.info(
            f"Address deleted successfully | id={address_id}"
        )

        return deleted

