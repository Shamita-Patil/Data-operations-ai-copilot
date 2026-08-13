class HealthRepository:
    """
    Repository responsible for retrieving
    application health information.
    """

    def get_health_status(self) -> dict:
        return {
            "status": "healthy",
            "database": "not_connected",
            "version": "v1"
        }
