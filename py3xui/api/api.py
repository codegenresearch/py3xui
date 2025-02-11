# pylint: disable=missing-module-docstring
"""This module provides classes to interact with the XUI API."""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
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
    def from_env(cls, skip_login: bool = False):
        """Initialize the API using environment variables.

        Args:
            skip_login (bool): Whether to skip the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class.
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """Log in to the XUI API and set the session for inbound and database APIs."""
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")