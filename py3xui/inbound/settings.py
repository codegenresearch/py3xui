"""
Handles settings related to the XUI API for parsing inbound connection configurations.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SettingsFields:
    """
    Stores the fields returned by the XUI API for parsing.

    Constants:
        CLIENTS (str): The key for the clients list in the settings.
        DECRYPTION (str): The key for the decryption method in the settings.
        FALLBACKS (str): The key for the fallbacks list in the settings.
    """

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents the settings for an inbound connection in the XUI API.

    Attributes:
        clients (list[Client], optional): A list of client configurations.
        decryption (str, optional): The decryption method used.
        fallbacks (list, optional): A list of fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []