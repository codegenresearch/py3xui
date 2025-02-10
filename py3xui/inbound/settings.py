"""
Module for parsing inbound connection settings from JSON responses.

This module defines the `Settings` class, which is used to parse and store settings data
for inbound connections in the XUI application.
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
    Represents the settings for an inbound connection in the XUI application.

    Attributes:
        clients (list[Client], optional): List of Client objects representing the clients configured in the settings.
        decryption (str, optional): String representing the decryption method used in the settings.
        fallbacks (list, optional): List of fallback configurations used in the settings.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []