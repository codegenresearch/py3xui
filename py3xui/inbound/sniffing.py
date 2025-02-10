"""This module contains the Sniffing class, which represents the sniffing settings for an inbound connection in the XUI API."""

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
    """Represents the sniffing settings for an inbound connection in the XUI API.

    Attributes:
        enabled (bool): Whether sniffing is enabled. Required.
        dest_override (list[str]): List of destination overrides. Optional.
        metadata_only (bool): Capture only metadata. Optional.
        route_only (bool): Capture only routing information. Optional.
    """

    enabled: bool

    dest_override: list[str] = Field(
        default=[], alias=SniffingFields.DEST_OVERRIDE
    )  # type: ignore

    metadata_only: bool = Field(
        default=False, alias=SniffingFields.METADATA_ONLY
    )  # type: ignore

    route_only: bool = Field(
        default=False, alias=SniffingFields.ROUTE_ONLY
    )  # type: ignore