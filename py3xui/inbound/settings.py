from py3xui.client.client import Client
from py3xui.inbound.bases import JsonStringModel

# Stores the fields returned by the XUI API for parsing.
class SettingsFields:
    """This class contains constants representing the fields returned by the XUI API for parsing."""

    # Represents the 'clients' field in the API response.
    CLIENTS = "clients"
    # Represents the 'decryption' field in the API response.
    DECRYPTION = "decryption"
    # Represents the 'fallbacks' field in the API response.
    FALLBACKS = "fallbacks"


class Settings(JsonStringModel):
    """A model representing the settings configuration, inheriting from JsonStringModel."""

    # A list of Client objects representing the clients in the settings.
    clients: list[Client] = []
    # A string representing the decryption method used.
    decryption: str = ""
    # A list representing the fallback configurations.
    fallbacks: list = []