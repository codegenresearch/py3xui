from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Stores the fields returned by the XUI API for parsing.
class SettingsFields:
    """Stores the fields returned by the XUI API for parsing."""

    # Key for accessing the list of clients in the settings.
    CLIENTS = "clients"
    # Key for accessing the decryption method in the settings.
    DECRYPTION = "decryption"
    # Key for accessing the fallback configurations in the settings.
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """
    Represents the settings configuration for the XUI application, inheriting from JsonStringModel.
    This class is used to parse and store settings data in a structured format.
    """

    # List of Client objects representing the clients configured in the settings.
    clients: list[Client] = []
    # String representing the decryption method used in the settings.
    decryption: str = ""
    # List of fallback configurations used in the settings.
    fallbacks: list = []