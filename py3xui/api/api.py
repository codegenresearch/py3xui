from __future__ import annotations
from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """
    A class to interact with the XUI API.

    This class provides methods to initialize the API with credentials, log in to the API,
    and create instances using environment variables. It manages sessions for client, inbound,
    and database API interactions.

    Attributes:
        client (ClientApi): An instance of ClientApi for handling client-related API calls.
        inbound (InboundApi): An instance of InboundApi for handling inbound-related API calls.
        database (DatabaseApi): An instance of DatabaseApi for handling database-related API calls.

    Methods:
        login(): Logs in to the XUI API and sets the session for inbound and database API instances.
        from_env(skip_login=False): Creates an instance of Api using environment variables for credentials.

    Example:
        Directly using credentials:
        >>> api = Api(host="https://api.example.com", username="user", password="pass")
        >>> api.login()
        Logged in successfully.

        Using environment variables:
        >>> api = Api.from_env()
        Logged in successfully.
    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """
        Initializes the Api class with the provided credentials and optionally logs in.

        Args:
            host (str): The XUI host URL.
            username (str): The username for authentication.
            password (str): The password for authentication.
            skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Example:
            >>> api = Api(host="https://api.example.com", username="user", password="pass")
        """
        self.client = ClientApi(host, username, password)
        self.inbound = InboundApi(host, username, password)
        self.database = DatabaseApi(host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False) -> Api:
        """
        Creates an instance of Api using environment variables for credentials.

        This method reads the XUI host URL, username, and password from environment variables:
        - XUI_HOST
        - XUI_USERNAME
        - XUI_PASSWORD

        Args:
            skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class initialized with credentials from environment variables.

        Example:
            >>> api = Api.from_env()
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """
        Logs in to the XUI API and sets the session for inbound and database API instances.

        This method authenticates the user with the provided credentials and shares the session
        across the client, inbound, and database API instances to maintain a consistent session state.

        Example:
            >>> api.login()
            Logged in successfully.
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")