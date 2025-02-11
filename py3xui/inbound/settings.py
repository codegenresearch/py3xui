from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module contains the Settings class for parsing inbound connection settings from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields used for parsing the inbound connection settings from the XUI API."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents the inbound connection settings parsed from the XUI API.

    Attributes:
        clients (list[Client]): Optional list of clients for the inbound connection.
        decryption (str): Optional decryption method for the inbound connection.
        fallbacks (list): Optional list of fallback configurations for the inbound connection.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []