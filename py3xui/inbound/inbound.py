"""
Module for handling inbound configurations in the XUI API.

This module defines the `Inbound` class, which represents an inbound connection
with various settings and statistics. It also includes a helper class `InboundFields`
for storing field names used in the XUI API.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from py3xui.client.client import Client
from py3xui.inbound.settings import Settings
from py3xui.inbound.sniffing import Sniffing
from py3xui.inbound.stream_settings import StreamSettings

# pylint: disable=too-few-public-methods
class InboundFields:
    """Stores the fields returned by the XUI API for parsing."""

    ENABLE = "enable"
    PORT = "port"
    PROTOCOL = "protocol"
    SETTINGS = "settings"
    STREAM_SETTINGS = "streamSettings"
    SNIFFING = "sniffing"

    ID = "id"
    UP = "up"
    DOWN = "down"
    TOTAL = "total"
    REMARK = "remark"

    EXPIRY_TIME = "expiryTime"
    CLIENT_STATS = "clientStats"
    LISTEN = "listen"

    TAG = "tag"


class Inbound(BaseModel):
    """
    Represents an inbound connection in the XUI API.

    Attributes:
        enable (bool): Whether the inbound is enabled. Required.
        port (int): The port number for the inbound. Required.
        protocol (str): The protocol used by the inbound. Required.
        settings (Settings): The settings specific to the protocol. Required.
        stream_settings (StreamSettings): The stream settings for the inbound. Required.
        sniffing (Sniffing): The sniffing settings for the inbound. Required.
        listen (str): The address to listen on. Optional. Defaults to an empty string.
        remark (str): A remark or description for the inbound. Optional. Defaults to an empty string.
        id (int): The unique identifier for the inbound. Optional. Defaults to 0.
        up (int): The total upload traffic. Optional. Defaults to 0.
        down (int): The total download traffic. Optional. Defaults to 0.
        total (int): The total traffic. Optional. Defaults to 0.
        expiry_time (int): The expiry time for the inbound. Optional. Defaults to 0.
        client_stats (list[Client]): The statistics for each client. Optional. Defaults to an empty list.
        tag (str): A tag for the inbound. Optional. Defaults to an empty string.
    """

    enable: bool
    port: int
    protocol: str
    settings: Settings
    stream_settings: StreamSettings = Field(alias=InboundFields.STREAM_SETTINGS)  # type: ignore
    sniffing: Sniffing

    listen: str = ""
    remark: str = ""
    id: int = 0

    up: int = 0
    down: int = 0

    total: int = 0

    expiry_time: int = Field(default=0, alias=InboundFields.EXPIRY_TIME)  # type: ignore
    client_stats: list[Client] = Field(default=[], alias=InboundFields.CLIENT_STATS)  # type: ignore

    tag: str = ""

    model_config = ConfigDict(
        populate_by_name=True,
    )

    def to_json(self) -> dict[str, Any]:
        """
        Converts the `Inbound` instance to a JSON-compatible dictionary for the XUI API.

        Returns:
            dict[str, Any]: A dictionary representation of the inbound configuration.
        """
        include = {
            InboundFields.REMARK,
            InboundFields.ENABLE,
            InboundFields.LISTEN,
            InboundFields.PORT,
            InboundFields.PROTOCOL,
            InboundFields.EXPIRY_TIME,
        }

        result = super().model_dump(by_alias=True)
        result = {k: v for k, v in result.items() if k in include}
        result.update(
            {
                InboundFields.SETTINGS: self.settings.model_dump_json(by_alias=True),
                InboundFields.STREAM_SETTINGS: self.stream_settings.model_dump_json(  # pylint: disable=no-member
                    by_alias=True
                ),
                InboundFields.SNIFFING: self.sniffing.model_dump_json(by_alias=True),
            }
        )

        return result