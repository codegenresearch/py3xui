"""This module contains the Sniffing class, which parses the sniffing settings for an inbound connection in the XUI API."""

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
    """Parses the sniffing settings for an inbound connection in the XUI API.

    Attributes:
        enabled (bool): Whether sniffing is enabled. Required.
        dest_override (list[str]): The destination override. Optional.
        metadata_only (bool): Whether to only use metadata for sniffing. Optional.
        route_only (bool): Whether to only use routing information for sniffing. Optional.
    """

    enabled: bool
    dest_override: list[str] = Field(default=[], alias=SniffingFields.DEST_OVERRIDE)  # type: ignore
    metadata_only: bool = Field(default=False, alias=SniffingFields.METADATA_ONLY)  # type: ignore
    route_only: bool = Field(default=False, alias=SniffingFields.ROUTE_ONLY)  # type: ignore