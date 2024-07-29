from dotenv import dotenv_values
from typing import *


class Config:
    def __init__(self, env_file=".env_files/app.env"):
        self._config = dotenv_values(
            env_file
        )
        self._config.update(
            {
                "AUTHORITY": f'https://login.microsoftonline.com/{self._config.get("TENANT_ID", "")}',
                "SCOPE": ["https://graph.microsoft.com/Notes.Read.All"],
                "PAGES_ENDPOINT": "/pages",
            }
        )

    def add_property(self, property_name: str, property_value: str) -> None:
        self._config.update({property_name: property_value})

    def get_property(self, property_name: str) -> str:
        return self._config[property_name]
