"""
This module defines classes for handling settings related to the XUI API.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SettingsFields:
    """
    Stores the fields returned by the XUI API for parsing.

    Attributes:
        CLIENTS (str): The key for the clients list in the settings.
        DECRYPTION (str): The key for the decryption method in the settings.
        FALLBACKS (str): The key for the fallbacks list in the settings.
    """

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents the settings configuration for the XUI API.

    Attributes:
        clients (list[Client]): A list of client configurations.
        decryption (str): The decryption method used.
        fallbacks (list): A list of fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []