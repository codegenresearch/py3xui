from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module defines classes related to handling settings data from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields returned by the XUI API for parsing.

    Attributes:
        CLIENTS (str): The key for accessing the list of clients in the settings.
        DECRYPTION (str): The key for accessing the decryption method in the settings.
        FALLBACKS (str): The key for accessing the fallback configurations in the settings.
    """

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents the settings data model with fields parsed from the XUI API.

    Attributes:
        clients (list[Client]): A list of Client objects representing the clients configured in the settings.
        decryption (str): A string representing the decryption method used.
        fallbacks (list): A list containing fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []