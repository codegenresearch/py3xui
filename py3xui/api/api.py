"""
Provides a high-level interface to interact with the XUI API, offering access to client, inbound, and database APIs.
"""

from py3xui.api import ClientApi, DatabaseApi, InboundApi
from py3xui.utils import Logger, env

logger = Logger(__name__)


class Api:
    """
    High-level interface to interact with the XUI API.

    Args:
        host (str): The host URL of the XUI API.
        username (str): The username for authentication.
        password (str): The password for authentication.
        skip_login (bool, optional): If True, skips the login process. Defaults to False.

    Attributes and Properties:
        client (ClientApi): An instance of the ClientApi class for handling client-related operations.
        inbound (InboundApi): An instance of the InboundApi class for handling inbound-related operations.
        database (DatabaseApi): An instance of the DatabaseApi class for handling database-related operations.

    Public Methods:
        from_env: Create an instance of Api using environment variables.
        login: Log into the XUI API and set the session.

    Examples:

    
    # Create an instance of Api using direct parameters
    from py3xui.api.api import Api
    api = Api(host='https://api.example.com', username='user', password='pass')
    api.login()
    

    
    # Create an instance of Api using environment variables
    import os
    os.environ['XUI_HOST'] = 'https://api.example.com'
    os.environ['XUI_USERNAME'] = 'user'
    os.environ['XUI_PASSWORD'] = 'pass'
    api_from_env = Api.from_env()
    api_from_env.login()
    

    """

    def __init__(self, host: str, username: str, password: str, skip_login: bool = False):
        """
        Initialize the Api class.

        Args:
            host (str): The host URL of the XUI API.
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
    def from_env(cls, skip_login: bool = False) -> Api:
        """
        Create an instance of Api using environment variables.

        Args:
            skip_login (bool, optional): If True, skips the login process. Defaults to False.

        Returns:
            Api: An instance of the Api class.

        Environment Variables:
            XUI_HOST: The host URL of the XUI API.
            XUI_USERNAME: The username for authentication.
            XUI_PASSWORD: The password for authentication.

        Examples:

        
        import os
        os.environ['XUI_HOST'] = 'https://api.example.com'
        os.environ['XUI_USERNAME'] = 'user'
        os.environ['XUI_PASSWORD'] = 'pass'
        api_from_env = Api.from_env()
        api_from_env.login()
        

        """
        host = env.xui_host()
        username = env.xui_username()
        password = env.xui_password()
        return cls(host, username, password, skip_login)

    def login(self) -> None:
        """
        Log into the XUI API and set the session.

        This method logs into the XUI API and sets the session for the client, inbound, and database APIs.

        Examples:

        
        api = Api(host='https://api.example.com', username='user', password='pass')
        api.login()
        

        """
        self.client.login()
        self.inbound.session = self.client.session
        self.database.session = self.client.session
        logger.info("Logged in successfully.")