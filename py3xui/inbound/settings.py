# pylint: disable=too-few-public-methods
"""
Module for handling XUI settings configuration.

This module defines the `Settings` class, which is used to parse and store settings data
for the XUI application. The class inherits from `JsonStringModel` and includes attributes
for clients, decryption methods, and fallback configurations.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


class SettingsFields:
    """Stores the fields returned by the XUI API for parsing."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents the settings configuration for the XUI application.

    Attributes:
        clients (list[Client]): List of Client objects representing the clients configured in the settings.
        decryption (str): String representing the decryption method used in the settings.
        fallbacks (list): List of fallback configurations used in the settings.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []