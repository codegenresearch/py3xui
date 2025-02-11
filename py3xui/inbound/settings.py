from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module defines classes for handling inbound connection settings data from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields returned by the XUI API for parsing inbound connection settings."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents the inbound connection settings data model with fields parsed from the XUI API.

    Attributes:
        clients (list[Client], optional): A list of Client objects representing the clients configured in the settings.
        decryption (str, optional): A string representing the decryption method used.
        fallbacks (list, optional): A list containing fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []