from pydantic import Field

from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class SniffingFields:
    """Stores the fields returned by the XUI API for parsing."""

    ENABLED = "enabled"
    DEST_OVERRIDE = "destOverride"
    METADATA_ONLY = "metadataOnly"
    ROUTE_ONLY = "routeOnly"


class Sniffing(JsonStringModel):
    """\n    Represents the sniffing settings for an inbound connection in the XUI API.\n\n    Attributes:\n        enabled (bool): Whether sniffing is enabled. Required.\n        dest_override (list[str]): The list of destination overrides. Defaults to an empty list.\n        metadata_only (bool): Whether to use metadata only for sniffing. Defaults to False.\n        route_only (bool): Whether to use routing only for sniffing. Defaults to False.\n    """

    enabled: bool
    dest_override: list[str] = Field(default=[], alias=SniffingFields.DEST_OVERRIDE)
    metadata_only: bool = Field(default=False, alias=SniffingFields.METADATA_ONLY)
    route_only: bool = Field(default=False, alias=SniffingFields.ROUTE_ONLY)