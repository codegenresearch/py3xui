"""This module contains the Sniffing class, which represents the sniffing settings for an inbound connection."""

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
    """Represents the sniffing settings for an inbound connection.

    Attributes:
        enabled (bool): Whether sniffing is enabled. Required.
        dest_override (list[str]): Whether to override the destination. Optional.
        metadata_only (bool): Whether to use only metadata for sniffing. Optional.
        route_only (bool): Whether to use only routing information for sniffing. Optional.
    """

    enabled: bool
    dest_override: list[str] = Field(default=[], alias=SniffingFields.DEST_OVERRIDE)  # type: ignore
    metadata_only: bool = Field(default=False, alias=SniffingFields.METADATA_ONLY)  # type: ignore
    route_only: bool = Field(default=False, alias=SniffingFields.ROUTE_ONLY)  # type: ignore


I have made the following adjustments based on the feedback:

1. **Docstring Consistency**: Simplified the description of the `Sniffing` class to be more concise.
2. **Attribute Descriptions**: Updated the wording of the optional attributes to use "Whether to" for consistency.
3. **Formatting**: Ensured each attribute is defined on a new line with consistent spacing.
4. **Field Names**: Ensured each field in the `SniffingFields` class is defined on its own line for clarity and consistency.