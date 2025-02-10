"""
Module containing the Settings class for parsing inbound connection settings from JSON responses.
"""

# pylint: disable=too-few-public-methods
from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


class SettingsFields:
    """Stores the fields returned by the XUI API for parsing."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents the settings for an inbound connection parsed from JSON responses.

    Attributes:
        clients (list[Client], optional): List of client configurations.
        decryption (str, optional): Decryption method used.
        fallbacks (list, optional): List of fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []