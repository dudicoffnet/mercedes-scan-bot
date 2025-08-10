from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    BOT_TOKEN: str
    MASTER_USERNAME: str | None = None
    MASTER_ID: int | None = None
    CHANNEL_ID: int | None = None

settings = Settings(
    BOT_TOKEN=os.getenv('BOT_TOKEN', ''),
    MASTER_USERNAME=os.getenv('MASTER_USERNAME') or None,
    MASTER_ID=int(os.getenv('MASTER_ID')) if os.getenv('MASTER_ID') else None,
    CHANNEL_ID=int(os.getenv('CHANNEL_ID')) if os.getenv('CHANNEL_ID') else None,
)
