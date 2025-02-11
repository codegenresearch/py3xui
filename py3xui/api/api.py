# pylint: disable=missing-module-docstring
from __future__ import annotations

"""Provides a high-level interface to interact with the XUI API."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """High-level interface to interact with the XUI API.

    This class provides methods to log in and perform operations through the client, database, and inbound interfaces.

    Args:
        host (str): The XUI host URL.
        xui_username (str): The XUI username for authentication.
        xui_password (str): The XUI password for authentication.
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
    from py3xui.api.api import Api
    api = Api(host='https://api.example.com', xui_username='user', xui_password='pass')
    api.login()
    # Logged in successfully.
    

    
    # Initialize the API using environment variables and log in
    import os
    from py3xui.api.api import Api
    os.environ['XUI_HOST'] = 'https://api.example.com'
    os.environ['XUI_USERNAME'] = 'user'
    os.environ['XUI_PASSWORD'] = 'pass'
    api = Api.from_env()
    api.login()
    # Logged in successfully.
    

    """

    def __init__(self, host: str, xui_username: str, xui_password: str, skip_login: bool = False):
        """Initialize the API with the given credentials.

        Args:
            host (str): The XUI host URL.
            xui_username (str): The XUI username for authentication.
            xui_password (str): The XUI password for authentication.
            skip_login (bool): Whether to skip the login process.
        """
        self.client = ClientApi(host, xui_username, xui_password)
        self.inbound = InboundApi(host, xui_username, xui_password)
        self.database = DatabaseApi(host, xui_username, xui_password)
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
        from py3xui.api.api import Api
        os.environ['XUI_HOST'] = 'https://api.example.com'
        os.environ['XUI_USERNAME'] = 'user'
        os.environ['XUI_PASSWORD'] = 'pass'
        api = Api.from_env()
        api.login()
        # Logged in successfully.
        
        
        """
        host = env.xui_host()
        xui_username = env.xui_username()
        xui_password = env.xui_password()
        return cls(host, xui_username, xui_password, skip_login)

    def login(self) -> None:
        """Log into the XUI API and set the session for other API components.

        This method logs into the XUI API using the provided credentials and sets the session for the client,
        inbound, and database components.

        Example:
        
        
        from py3xui.api.api import Api
        api = Api(host='https://api.example.com', xui_username='user', xui_password='pass')
        api.login()
        # Logged in successfully.
        
        
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")