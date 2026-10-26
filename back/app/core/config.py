from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    app_name: str = "Corporate portal"

    database_url: PostgresDsn = Field(
        'postgresql+psycopg://portal_user:portal_pass@localhost:5432/portal_db'
    )
    secret_key: str 
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 60
    refresh_token_expire_minutes: int = 600
     
settings = Settings()








