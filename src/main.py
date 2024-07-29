from common.config import Config
from auth.msal import MSALAuthenticator
from managers.onenote_manager import OneNoteManager


def main():
    config = Config()
    authenticator = MSALAuthenticator(
        client_id=config.get_property("CLIENT_ID"),
        authority=config.get_property("AUTHORITY"),
        scope=config.get_property("SCOPE")
    )
    manager = OneNoteManager(config, authenticator)
    manager.print_content()

if __name__ == "__main__":
    main()
