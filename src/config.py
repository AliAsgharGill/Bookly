from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# Load the .env file explicitly
load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore"
    )


# Debug: Print DATABASE_URL to check if it’s loaded
# print("DATABASE_URL from os:", os.getenv("DATABASE_URL"))
Config = Settings()
# print("DATABASE_URL from Pydantic:", Config.DATABASE_URL)
