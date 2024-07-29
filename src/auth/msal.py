import msal
from typing import Optional, List


class MSALAuthenticator():
    def __init__(self, client_id: str, authority: str, scope: List[str]):
        self.client_id = client_id
        self.authority = authority
        self.scope = scope
        self.app = msal.PublicClientApplication(client_id=self.client_id, authority=self.authority)

    def get_access_token(self) -> Optional[str]:
        accounts = self.app.get_accounts()
        result = None
        if accounts:
            result = self.app.acquire_token_silent(self.scope, account=accounts[0])

        if not result:
            flow = self.app.initiate_device_flow(scopes=self.scope)
            if "user_code" in flow:
                print(flow["message"])
                result = self.app.acquire_token_by_device_flow(flow)
            else:
                raise Exception("Failed to create device flow")

        return result.get("access_token") if result else None
