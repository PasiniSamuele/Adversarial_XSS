from pydantic import ValidationError
from pydantic_settings import BaseSettings

class Settings(BaseSettings, case_sensitive=True):
    api_prefix: str = "vuln_backend/1.0"

description = ""
