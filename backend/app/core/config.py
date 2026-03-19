from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Shqip"
    DEBUG: bool = False

    # CORS — which frontend URLs are allowed to call this API
    # In development: localhost. In production: your CloudFront domain.
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]

    # Database — filled in from .env file
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/shqip"

    # AWS — filled in from .env file
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""

    # Amazon Cognito — for user auth (Month 2)
    COGNITO_USER_POOL_ID: str = ""
    COGNITO_CLIENT_ID: str = ""

    # Amazon Bedrock — for AI tutor (Month 3)
    BEDROCK_MODEL_ID: str = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Amazon Polly — for text-to-speech (Month 3)
    POLLY_VOICE_GHEG: str = "Joanna"    # Placeholder — swap when Albanian voice available
    POLLY_VOICE_TOSK: str = "Joanna"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
