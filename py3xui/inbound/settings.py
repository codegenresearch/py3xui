from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module contains the Settings class used for parsing the JSON response from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields used for parsing the JSON response from the XUI API."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents the inbound connection settings parsed from the XUI API.

    Attributes:
        clients (list[Client]): Optional list of clients for the inbound connection.
        decryption (str): Optional string representing the decryption method used.
        fallbacks (list): Optional list containing fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []