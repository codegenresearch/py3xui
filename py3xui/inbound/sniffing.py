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
        dest_override (list[str]): The destination override. Optional.
        metadata_only (bool): Use only metadata for sniffing. Optional.
        route_only (bool): Use only routing information for sniffing. Optional.
    """

    enabled: bool
    dest_override: list[str] = Field(default=[], alias=SniffingFields.DEST_OVERRIDE)  # type: ignore
    metadata_only: bool = Field(default=False, alias=SniffingFields.METADATA_ONLY)  # type: ignore
    route_only: bool = Field(default=False, alias=SniffingFields.ROUTE_ONLY)  # type: ignore


I have made the following adjustments based on the feedback:

1. **Docstring Consistency**: Simplified the description of the `Sniffing` class to be more concise and direct.
2. **Attribute Descriptions**: Ensured the attribute descriptions are phrased consistently, focusing on the wording used for optional attributes.
3. **Formatting**: Ensured each attribute is defined on a new line with consistent spacing.
4. **Field Names**: Ensured each field in the `SniffingFields` class is defined on its own line to match the style of the gold code.