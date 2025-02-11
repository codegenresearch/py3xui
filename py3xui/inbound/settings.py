from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Module-level docstring for clarity
# This module defines classes for handling inbound connection settings from the XUI API.

# pylint: disable=too-few-public-methods
class SettingsFields:
    """Stores the fields returned by the XUI API for parsing inbound connection settings."""

    CLIENTS = "clients"
    DECRYPTION = "decryption"
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """Represents inbound connection settings parsed from the XUI API.

    Attributes:
        clients (list[Client]): Optional list of Client objects representing the clients configured in the settings.
        decryption (str): Optional string representing the decryption method used.
        fallbacks (list): Optional list containing fallback configurations.
    """

    clients: list[Client] = []
    decryption: str = ""
    fallbacks: list = []