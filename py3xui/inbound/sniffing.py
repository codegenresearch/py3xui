from pydantic import Field

from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SniffingFields:
    """Stores the fields returned by the XUI API for parsing.

    Attributes:
        ENABLED (str): The key for the 'enabled' field in the XUI API.
        DEST_OVERRIDE (str): The key for the 'destOverride' field in the XUI API.
        METADATA_ONLY (str): The key for the 'metadataOnly' field in the XUI API.
        ROUTE_ONLY (str): The key for the 'routeOnly' field in the XUI API.
    """

    ENABLED = "enabled"
    DEST_OVERRIDE = "destOverride"
    METADATA_ONLY = "metadataOnly"
    ROUTE_ONLY = "routeOnly"


class Sniffing(JsonStringModel):
    """Represents the sniffing settings for an inbound connection in the XUI API.

    Attributes:
        enabled (bool): Indicates whether sniffing is enabled for the inbound connection.
        dest_override (list[str]): A list of destination overrides for the sniffing settings.
        metadata_only (bool): Indicates whether to capture only metadata during sniffing.
        route_only (bool): Indicates whether to capture only routing information during sniffing.
    """

    enabled: bool
    dest_override: list[str] = Field(default=[], alias=SniffingFields.DEST_OVERRIDE)  # type: ignore
    metadata_only: bool = Field(default=False, alias=SniffingFields.METADATA_ONLY)  # type: ignore
    route_only: bool = Field(default=False, alias=SniffingFields.ROUTE_ONLY)  # type: ignore