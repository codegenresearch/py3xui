"""
This module defines classes for handling settings related to the XUI API, specifically for parsing the JSON response for inbound connections.
"""

from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SettingsFields:
    """
    Stores the fields returned by the XUI API for parsing.
    """


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