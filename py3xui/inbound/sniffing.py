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
        enabled (bool): Whether the sniffing is enabled.
        dest_override (list[str]): List of destination overrides.
        metadata_only (bool): Capture only metadata.
        route_only (bool): Capture only routing information.
    """

    enabled: bool
    dest_override: list[str] = Field(default=[], alias=SniffingFields.DEST_OVERRIDE)  # type: ignore
    metadata_only: bool = Field(default=False, alias=SniffingFields.METADATA_ONLY)  # type: ignore
    route_only: bool = Field(default=False, alias=SniffingFields.ROUTE_ONLY)  # type: ignore


Based on the feedback, I have made the following adjustments:

1. **Module-level Docstring**: Rephrased the module-level docstring to be more concise.
2. **Attribute Descriptions**: Refined the attribute descriptions to match the gold code's style.
3. **Formatting**: Ensured consistent spacing and line breaks between class attributes.
4. **Class Structure**: Reordered the attributes in the `Sniffing` class to match the gold code's structure.

This should align more closely with the gold code's style and structure.