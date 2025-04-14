from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL : str
    JWT_SECRET : str
    JWT_ALGORITHM : str

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"
    )

Config = Settings()

if __name__=="__main__":
    Config = Settings()
    print(Config.DATABASE_URL)