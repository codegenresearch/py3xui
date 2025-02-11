# pylint: disable=missing-module-docstring
from __future__ import annotations

"""This module provides a high-level interface to interact with the XUI API."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """A high-level interface to interact with the XUI API.

    This class provides access to the client, inbound, and database APIs through a single interface.

    Args:
        host (str): The XUI host URL.
        username (str): The username for authentication.
        password (str): The password for authentication.
        skip_login (bool): Whether to skip the login process. Defaults to False.

    Attributes and Properties:
        client (ClientApi): An instance of the ClientApi class.
        inbound (InboundApi): An instance of the InboundApi class.
        database (DatabaseApi): An instance of the DatabaseApi class.

    Public Methods:
        from_env(skip_login: bool = False): Initializes the API using environment variables.
        login(): Logs into the XUI API and sets the session cookie for the client, inbound, and database APIs.

    Examples:
        
        
        # Initialize the API with direct credentials
        api = Api(host='https://api.example.com', username='user', password='pass')

        # Initialize the API using environment variables
        # Ensure the following environment variables are set:
        # XUI_HOST=https://api.example.com
        # XUI_USERNAME=user
        # XUI_PASSWORD=pass
        api = Api.from_env()

        # Log into the API
        api.login()
        

    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """Initialize the API with the given credentials.

        Args:
            host (str): The XUI host URL.
            username (str): The username for authentication.
            password (str): The password for authentication.
            skip_login (bool): Whether to skip the login process. Defaults to False.
        """
        self.client = ClientApi(host, username, password)
        self.inbound = InboundApi(host, username, password)
        self.database = DatabaseApi(host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False) -> Api:
        """Initializes the API using environment variables.

        Required environment variables:
            XUI_HOST: The XUI host URL.
            XUI_USERNAME: The username for authentication.
            XUI_PASSWORD: The password for authentication.

        Args:
            skip_login (bool): Whether to skip the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class.

        Examples:
            
            
            # Ensure the following environment variables are set:
            # XUI_HOST=https://api.example.com
            # XUI_USERNAME=user
            # XUI_PASSWORD=pass
            api = Api.from_env()
            
            
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """Logs into the XUI API and sets the session cookie for the client, inbound, and database APIs.

        Examples:
            
            
            # Log into the API
            api.login()
            
            
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")