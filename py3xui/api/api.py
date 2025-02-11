from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """
    Provides a high-level interface to interact with the XUI API.

    This class initializes and manages interactions with the XUI API through
    client, inbound, and database APIs. It supports both direct initialization
    with credentials and initialization using environment variables.

    Attributes:
        client (ClientApi): Manages client-related API calls.
        inbound (InboundApi): Manages inbound-related API calls.
        database (DatabaseApi): Manages database-related API calls.

    Methods:
        login(): Authenticates with the XUI API and sets up sessions.
        from_env(skip_login=False): Initializes the API using environment variables.

    Examples:
        Directly using credentials:

        
        api = Api(host="https://api.example.com", username="user", password="pass")
        api.login()
        

        Using environment variables:

        
        import os
        os.environ['XUI_HOST'] = "https://api.example.com"
        os.environ['XUI_USERNAME'] = "user"
        os.environ['XUI_PASSWORD'] = "pass"
        api = Api.from_env()
        
    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """
        Initializes the Api class with the provided credentials.

        Args:
            host (str): The XUI host URL.
            username (str): The username for authentication.
            password (str): The password for authentication.
            skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Example:
            
            api = Api(host="https://api.example.com", username="user", password="pass")
            
        """
        self.client = ClientApi(host, username, password)
        self.inbound = InboundApi(host, username, password)
        self.database = DatabaseApi(host, username, password)
        if not skip_login:
            self.login()

    @classmethod
    def from_env(cls, skip_login: bool = False) -> Api:
        """
        Initializes the Api class using environment variables.

        Reads the XUI host URL, username, and password from environment variables:
        - XUI_HOST
        - XUI_USERNAME
        - XUI_PASSWORD

        Args:
            skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class initialized with credentials from environment variables.

        Example:
            
            import os
            os.environ['XUI_HOST'] = "https://api.example.com"
            os.environ['XUI_USERNAME'] = "user"
            os.environ['XUI_PASSWORD'] = "pass"
            api = Api.from_env()
            
        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """
        Logs in to the XUI API and sets up sessions for client, inbound, and database APIs.

        Example:
            
            api.login()
            
        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")