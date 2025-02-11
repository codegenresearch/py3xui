"""This module provides a class to interact with the XUI API, offering methods for initialization, login, and creating instances from environment variables."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """
    A class to interact with the XUI API.

    Attributes:
        client (ClientApi): An instance of ClientApi for handling client-related API calls.
        inbound (InboundApi): An instance of InboundApi for handling inbound-related API calls.
        database (DatabaseApi): An instance of DatabaseApi for handling database-related API calls.
    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """
        Initializes the Api class with the provided credentials and optionally logs in.

        Args:
            host (str): The host address of the XUI API.
            username (str): The username for authentication.
            password (str): The password for authentication.
            skip_login (bool, optional): If True, skips the login process. Defaults to False.
        """
        self.client = ClientApi(host, username, password)
        self.inbound = InboundApi(host, username, password)
        self.database = DatabaseApi(host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False):
        """
        Creates an instance of Api using environment variables for credentials.

        Args:
            skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class initialized with credentials from environment variables.
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """
        Logs in to the XUI API and sets the session for inbound and database API instances.
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")