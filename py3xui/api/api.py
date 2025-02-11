# pylint: disable=missing-module-docstring
from __future__ import annotations

"""Provides a high-level interface to interact with the XUI API."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """High-level interface to interact with the XUI API.

    This class initializes the API with the given credentials and provides methods to log in and perform
    operations through the client, database, and inbound interfaces.

    Args:
        xui_host (str): The XUI host URL.
        username (str): The username for authentication.
        password (str): The password for authentication.
        skip_login (bool): Whether to skip the login process.

    Attributes:
        client (ClientApi): An instance of the ClientApi class.
        inbound (InboundApi): An instance of the InboundApi class.
        database (DatabaseApi): An instance of the DatabaseApi class.

    Methods:
        from_env(skip_login: bool = False) -> Api: Initializes the API using environment variables.
        login() -> None: Logs into the XUI API and sets the session for other API components.

    Examples:
    
    # Initialize the API with explicit credentials and log in
    api = Api(xui_host='https://api.example.com', username='user', password='pass')
    api.login()
    # Logged in successfully.
    

    
    # Initialize the API using environment variables and log in
    import os
    os.environ['XUI_HOST'] = 'https://api.example.com'
    os.environ['XUI_USERNAME'] = 'user'
    os.environ['XUI_PASSWORD'] = 'pass'
    api = Api.from_env()
    api.login()
    # Logged in successfully.
    
    """

    def __init__(self, xui_host: str, username: str, password: str, skip_login: bool = False):
        """Initialize the API with the given credentials.

        Args:
            xui_host (str): The XUI host URL.
            username (str): The username for authentication.
            password (str): The password for authentication.
            skip_login (bool): Whether to skip the login process.
        """
        self.client = ClientApi(xui_host, username, password)
        self.inbound = InboundApi(xui_host, username, password)
        self.database = DatabaseApi(xui_host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False) -> Api:
        """Initialize the API using environment variables.

        Args:
            skip_login (bool): Whether to skip the login process.

        Returns:
            Api: An instance of the Api class.

        Example:
        
        import os
        os.environ['XUI_HOST'] = 'https://api.example.com'
        os.environ['XUI_USERNAME'] = 'user'
        os.environ['XUI_PASSWORD'] = 'pass'
        api = Api.from_env()
        api.login()
        # Logged in successfully.
        
        """
        xui_host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(xui_host, username, password, skip_login)

    def login(self) -> None:
        """Log into the XUI API and set the session for other API components.

        Example:
        
        api = Api(xui_host='https://api.example.com', username='user', password='pass')
        api.login()
        # Logged in successfully.
        
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")