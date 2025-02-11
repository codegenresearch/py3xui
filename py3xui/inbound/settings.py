"""
Module for parsing the JSON response from the XUI API to handle inbound connection settings.
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
        clients (list[Client]): List of client configurations. Optional.
        decryption (str): Decryption method used. Optional.
        fallbacks (list): List of fallback configurations. Optional.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []