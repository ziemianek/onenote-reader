import requests
from typing import Optional, Dict, Any

class OneNoteService:
    def __init__(self, base_api_url: str = "https://graph.microsoft.com/v1.0/me/onenote"):
        self.base_url = base_api_url

    def get_data(self, endpoint: str, access_token: str) -> Optional[Dict[str, Any]]:
        """Get data from OneNote API"""
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers)
        if not response.status_code == 200:
            err_msg = f"ERROR: {response.status_code} - {response.text}"
            raise requests.RequestException(err_msg)
        return response.json()
