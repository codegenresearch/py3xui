"""
Module for handling settings related to inbound connections in the XUI API.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SettingsFields:
    """
    Fields returned by the XUI API for parsing.

    Attributes:
        CLIENTS (str): Key for the clients list.
        DECRYPTION (str): Key for the decryption method.
        FALLBACKS (str): Key for the fallbacks list.
    """

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Settings for an inbound connection parsed from the XUI API.

    Attributes:
        clients (list[Client], optional): List of client configurations.
        decryption (str, optional): Decryption method used.
        fallbacks (list, optional): List of fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []