import os
from langchain_core.documents import Document
from typing import List
from langchain_community.document_loaders.onenote import OneNoteLoader
from common.config import Config
from services.onenote import OneNoteService
from typing import Optional, Dict, Any
from auth.msal import MSALAuthenticator

class OneNoteManager:
    def __init__(self, config: Config, authenticator: MSALAuthenticator):
        self.config = config
        self.access_token = authenticator.get_access_token()

        self._setup_env()

        self.onenote_service = OneNoteService()


    def _setup_env(self) -> None:
        # Set environment variables
        from dotenv import load_dotenv
        load_dotenv(".env_files/graph_api.env")

    def get_pages(self) -> Optional[Dict[str, Any]]:
        return self.onenote_service.get_data(
            self.config.get_property("PAGES_ENDPOINT"),
            self.access_token
        )

    def load_documents(self) -> List[List[Document]]:
        """Load the OneNote document using OneNoteLoader."""
        pages = self.get_pages()
        documents = []
        for page in pages['value']:
            if page['title'] not in ['Page1', 'Page2', 'Page3']: continue
            print(f"Page: {page['title']}, ID: {page['id']}")

            # bottleneck
            # this slows the code down A LOT
            loader = OneNoteLoader(
                page_title=page['title'],
                access_token=self.access_token
            )
            documents.append(loader.load())
        return documents

    def print_content(self) -> None:
        """Print the content of the loaded document."""
        documents = self.load_documents()
        print(documents)
