from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # SlowAPI
    rate_limit: str

    class Config:
        env_file = r"./.env"


settings = Settings()
