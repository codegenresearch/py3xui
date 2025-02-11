"""
Module containing the Settings class for parsing inbound connection settings from the XUI API.
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
    Represents the settings for an inbound connection parsed from the XUI API.

    Attributes:
        clients (list[Client], optional): List of client configurations for the inbound connection.
        decryption (str, optional): Decryption method used for the inbound connection.
        fallbacks (list, optional): List of fallback configurations for the inbound connection.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []