"""Module for interacting with the XUI API, providing a unified interface for client, database, and inbound operations."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """\n    A class to interact with the XUI API, managing client, database, and inbound operations.\n\n    Attributes:\n        client (ClientApi): Instance of ClientApi for handling client-related API calls.\n        inbound (InboundApi): Instance of InboundApi for handling inbound-related API calls.\n        database (DatabaseApi): Instance of DatabaseApi for handling database-related API calls.\n    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """\n        Initializes the Api class.\n\n        Args:\n            host (str): The hostname or IP address of the XUI server.\n            username (str): The username for authentication.\n            password (str): The password for authentication.\n            skip_login (bool, optional): If True, skips the login process. Defaults to False.\n        """
        self.client = ClientApi(host, username, password)
        self.inbound = InboundApi(host, username, password)
        self.database = DatabaseApi(host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False):
        """\n        Creates an instance of Api using environment variables for configuration.\n\n        Args:\n            skip_login (bool, optional): If True, skips the login process. Defaults to False.\n\n        Returns:\n            Api: An instance of the Api class configured with environment variables.\n        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """\n        Logs in to the XUI API and shares the session across client, inbound, and database instances.\n\n        Logs a success message upon successful login.\n        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")