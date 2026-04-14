from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    ENV: str = "development"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    RELOAD: bool = True
    CORS_ORIGINS: List[str] = []

    class Config:
        env_file = "config.env"

    def model_post_init(self, __context):
        if self.ENV == "production":
            object.__setattr__(self, "RELOAD", False)
        else:
            object.__setattr__(self, "HOST", "localhost")
            object.__setattr__(self, "RELOAD", True)
settings = Settings()
