from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    app_name: str
    api_version: str
    debug: bool

    host: str
    port: int

    database_url: str
    redis_url: str
    jwt_secret: str

    gemini_api_key: str
    langsmith_tracing: bool
    langsmith_api_key: str
    langsmith_project: str

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
