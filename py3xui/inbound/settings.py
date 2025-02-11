"""
Module for handling settings related to the XUI API for parsing inbound connection configurations.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SettingsFields:
    """
    Stores the fields returned by the XUI API for parsing.
    """

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents the settings for an inbound connection in the XUI API.

    Attributes:
        clients (list[Client]): List of client configurations.
        decryption (str): Decryption method used.
        fallbacks (list): List of fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []