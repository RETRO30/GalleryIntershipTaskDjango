from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass(frozen=True, slots=True)
class DatabaseData:
    host: str
    port: str
    username: str
    password: str
    name: str
    
    
@dataclass(frozen=True, slots=True)
class DjangoSettingsData:
    secret_key: str
    

@dataclass(frozen=True, slots=True)
class ConfigData:
    database: DatabaseData
    django_settings: DjangoSettingsData
    
    
def load_config() -> ConfigData:
    if not os.getenv("DOCKER"):
        print("i'm here")
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        print(env_path)
        load_dotenv(dotenv_path=env_path)
    
    
    return ConfigData(
        database=DatabaseData(
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT"),
            username=os.getenv("DATABASE_USERNAME"),
            password=os.getenv("DATABASE_PASSWORD"),
            name=os.getenv("DATABASE_NAME")
        ),
        django_settings=DjangoSettingsData(
            secret_key=os.getenv("DJANGO_SECRET_KEY")
        )
    )
    
Config = load_config()