from backend.app.repositories.health_repository import HealthRepository


class HealthService:
    """
    Contains business logic related
    to application health.
    """

    def __init__(self):
        self.repository = HealthRepository()

    def get_application_health(self):
        """
        Returns application health.
        """

        return self.repository.get_health_status()
