# pylint: disable=missing-module-docstring
from __future__ import annotations

"""This module provides a class to interact with the XUI API, offering methods for initialization, login, and environment-based configuration."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """A class to interact with the XUI API.

    This class provides methods to initialize the API with either direct credentials or environment variables,
    and to log in to the API.

    Args:
        host (str): The host address of the XUI API.
        username (str): The username for authentication.
        password (str): The password for authentication.
        skip_login (bool): Whether to skip the login process. Defaults to False.

    Attributes:
        client (ClientApi): An instance of the ClientApi class.
        inbound (InboundApi): An instance of the InboundApi class.
        database (DatabaseApi): An instance of the DatabaseApi class.

    Methods:
        from_env(skip_login: bool = False) -> Api: Initialize the API using environment variables.
        login() -> None: Log in to the XUI API and set the session for inbound and database APIs.

    Examples:
        Initialize the API with direct credentials:
        >>> api = Api(host='https://api.example.com', username='user', password='pass')

        Initialize the API using environment variables:
        >>> api = Api.from_env()

        Log in to the API:
        >>> api.login()
    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """Initialize the API with the given credentials.

        Args:
            host (str): The host address of the XUI API.
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
        """Initialize the API using environment variables.

        Args:
            skip_login (bool): Whether to skip the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class.

        Examples:
            Initialize the API using environment variables:
            >>> api = Api.from_env()
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """Log in to the XUI API and set the session for inbound and database APIs.

        Examples:
            Log in to the API:
            >>> api.login()
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")