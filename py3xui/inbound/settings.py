"""
Module for parsing inbound connection settings from the XUI API using the Settings class.
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
    Represents inbound connection settings parsed from the XUI API.

    Attributes:
        clients (list[Client], optional): List of client configurations.
        decryption (str, optional): Decryption method used.
        fallbacks (list, optional): List of fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []