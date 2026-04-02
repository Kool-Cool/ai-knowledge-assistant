from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    RELOAD: bool = True

    class Config:
        env_file = "config.env"

    def __post_init__(self):
        if self.ENV == "production":
            self.RELOAD = False
        else:
            self.HOST = "localhost"
            self.RELOAD = True

settings = Settings()
