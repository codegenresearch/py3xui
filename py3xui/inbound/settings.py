from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module defines the Settings class for parsing inbound connection settings from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields used for parsing the XUI API response."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents the inbound connection settings parsed from the XUI API.

    Attributes:
        clients (list[Client]): List of clients for the inbound connection (optional).
        decryption (str): Decryption method for the inbound connection (optional).
        fallbacks (list): List of fallback configurations for the inbound connection (optional).
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []