from __future__ import annotations

"""
This module provides a high-level interface to interact with the XUI API, offering access to client, inbound, and database APIs.

Classes:
- `Api`: A class to manage interactions with the XUI API, including login and session management.
"""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """
    A class to manage interactions with the XUI API, providing a high-level interface to the client, inbound, and database APIs.

    Args:
    - host (str): The host URL of the XUI API.
    - username (str): The username for authentication.
    - password (str): The password for authentication.
    - skip_login (bool, optional): If True, skips the login process. Defaults to False.

    Attributes and Properties:
    - client (ClientApi): An instance of ClientApi for handling client-related API calls.
    - inbound (InboundApi): An instance of InboundApi for handling inbound-related API calls.
    - database (DatabaseApi): An instance of DatabaseApi for handling database-related API calls.

    Public Methods:
    - `from_env(cls, skip_login: bool = False) -> Api`: Class method to create an instance of Api using environment variables.
    - `login(self) -> None`: Logs into the XUI API and sets the session for inbound and database API calls.

    Examples:
    
    # Import necessary modules
    from py3xui.api.api import Api

    # Create an instance of Api using direct parameters
    api = Api(host='https://api.example.com', username='user', password='pass')
    api.login()

    # Set environment variables (example using os module)
    import os
    os.environ['XUI_HOST'] = 'https://api.example.com'
    os.environ['XUI_USERNAME'] = 'user'
    os.environ['XUI_PASSWORD'] = 'pass'

    # Create an instance of Api using environment variables
    api_from_env = Api.from_env()
    api_from_env.login()
    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """
        Initializes the Api class.

        Args:
        - host (str): The host URL of the XUI API.
        - username (str): The username for authentication.
        - password (str): The password for authentication.
        - skip_login (bool, optional): If True, skips the login process. Defaults to False.
        """
        self.client = ClientApi(host, username, password)
        self.inbound = InboundApi(host, username, password)
        self.database = DatabaseApi(host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False) -> Api:
        """
        Creates an instance of Api using environment variables.

        Args:
        - skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Returns:
        - Api: An instance of the Api class.
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """
        Logs into the XUI API and sets the session for inbound and database API calls.

        This method logs into the XUI API using the provided credentials and sets the session
        cookie for the `client`, `inbound`, and `database` API instances. This is necessary for
        making authenticated API calls.
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged into the XUI API successfully.")