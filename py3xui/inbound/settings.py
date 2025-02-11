"""
Handles parsing of inbound connection settings from the XUI API.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SettingsFields:
    """
    Stores the keys for fields returned by the XUI API.

    Attributes:
        CLIENTS: Key for the clients list.
        DECRYPTION: Key for the decryption method.
        FALLBACKS: Key for the fallbacks list.
    """

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents inbound connection settings parsed from the XUI API.

    Attributes:
        clients: List of client configurations. Defaults to an empty list.
        decryption: Decryption method used. Defaults to an empty string.
        fallbacks: List of fallback configurations. Defaults to an empty list.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []