"""
This module provides a high-level interface to interact with the XUI API.

The `Api` class provides methods to interact with the XUI API, including logging in and managing sessions for different API components.

Classes:
- `Api`: A class to manage interactions with the XUI API, including login and session management.
"""

from __future__ import annotations
from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """
    A high-level interface to interact with the XUI API.

    The `Api` class provides methods to interact with the XUI API, including logging in and managing sessions for different API components.

    Args:
    - xui_host (str): The XUI host URL.
    - xui_username (str): The username for authentication.
    - xui_password (str): The password for authentication.
    - skip_login (bool, optional): If True, skips the login process. Defaults to False.

    Attributes:
    - client (ClientApi): An instance of ClientApi for handling client-related API calls.
    - inbound (InboundApi): An instance of InboundApi for handling inbound-related API calls.
    - database (DatabaseApi): An instance of DatabaseApi for handling database-related API calls.

    Methods:
    - `from_env(skip_login: bool = False) -> Api`: Class method to create an instance of Api using environment variables.
    - `login() -> None`: Logs in to the XUI API and sets the session for client, inbound, and database API calls.

    Examples:
    
    # Import the Api class
    from py3xui.api.api import Api

    # Initialize the Api class directly
    api = Api(xui_host="https://api.example.com", xui_username="user", xui_password="pass")

    # Initialize the Api class using environment variables
    api = Api.from_env()

    # Log in to the API
    api.login()
    
    """

    def __init__(self, xui_host: str, xui_username: str, xui_password: str, skip_login: bool = False):
        """
        Initializes the Api class.

        Args:
        - xui_host (str): The XUI host URL.
        - xui_username (str): The username for authentication.
        - xui_password (str): The password for authentication.
        - skip_login (bool, optional): If True, skips the login process. Defaults to False.
        """
        self.client = ClientApi(xui_host, xui_username, xui_password)
        self.inbound = InboundApi(xui_host, xui_username, xui_password)
        self.database = DatabaseApi(xui_host, xui_username, xui_password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False) -> Api:
        """
        Creates an instance of Api using environment variables.

        The required environment variables are:
        - `XUI_HOST`: The XUI host URL.
        - `XUI_USERNAME`: The username for authentication.
        - `XUI_PASSWORD`: The password for authentication.

        Args:
        - skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Returns:
        - Api: An instance of the Api class.

        Examples:
        
        # Initialize the Api class using environment variables
        api = Api.from_env()
        
        """
        xui_host = env.xui_host()
        xui_username = env.xui_username()
        xui_password = env.xui_password()
        return cls(xui_host, xui_username, xui_password, skip_login)

    def login(self) -> None:
        """
        Logs in to the XUI API and sets the session for client, inbound, and database API calls.

        This method logs in to the XUI API using the provided credentials and sets the session cookie for the client, inbound, and database APIs.

        Examples:
        
        # Log in to the API
        api.login()
        
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")