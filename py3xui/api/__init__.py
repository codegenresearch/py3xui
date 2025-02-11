from py3xui.api.api_client import ClientApi  # Provides methods to interact with the client-related functionalities of the XUI API.
from py3xui.api.api_database import DatabaseApi  # Provides methods to interact with the database-related functionalities of the XUI API.
from py3xui.api.api_inbound import InboundApi  # Provides methods to interact with the inbound-related functionalities of the XUI API.

# Example usage:
# api_client = ClientApi(host="https://xui.example.com", username="username", password="password")
# api_database = DatabaseApi(host="https://xui.example.com", username="username", password="password")
# api_inbound = InboundApi(host="https://xui.example.com", username="username", password="password")

# These instances can be used to perform operations specific to clients, database, and inbounds respectively.