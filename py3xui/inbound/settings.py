from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module contains the Settings class for parsing inbound settings from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields used for parsing the XUI API response."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents the inbound settings parsed from the XUI API.

    Attributes:
        clients (list[Client]): The list of clients for the inbound connection (optional).
        decryption (str): The decryption method for the inbound connection (optional).
        fallbacks (list): The list of fallback configurations for the inbound connection (optional).
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []