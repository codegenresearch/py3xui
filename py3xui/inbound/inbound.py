from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from py3xui.client.client import Client
from py3xui.inbound.settings import Settings
from py3xui.inbound.sniffing import Sniffing
from py3xui.inbound.stream_settings import StreamSettings

# Module-level docstring for clarity
# This module defines the Inbound class, which represents an inbound connection configuration for the XUI API.

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
    """Represents an inbound connection configuration for the XUI API.

    Attributes:
        enable (bool): Required. Indicates whether the inbound connection is enabled.
        port (int): Required. The port number on which the inbound connection listens.
        protocol (str): Required. The protocol used by the inbound connection (e.g., vmess, vless).
        settings (Settings): Required. The settings specific to the protocol.
        stream_settings (StreamSettings): Required. Stream settings for the inbound connection.
        sniffing (Sniffing): Required. Sniffing settings for the inbound connection.
        listen (str): Optional. The address on which the inbound connection listens. Defaults to an empty string.
        remark (str): Optional. Any remarks or notes about the inbound connection. Defaults to an empty string.
        id (int): Optional. The unique identifier for the inbound connection. Defaults to 0.
        up (int): Optional. The upload traffic of the inbound connection. Defaults to 0.
        down (int): Optional. The download traffic of the inbound connection. Defaults to 0.
        total (int): Optional. The total traffic of the inbound connection. Defaults to 0.
        expiry_time (int): Optional. The expiry time of the inbound connection. Defaults to 0.
        client_stats (list[Client]): Optional. List of client statistics for the inbound connection. Defaults to an empty list.
        tag (str): Optional. The tag associated with the inbound connection. Defaults to an empty string.
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
        """Converts the inbound connection configuration to a JSON-compatible dictionary for the XUI API.

        Returns:
            dict[str, Any]: A dictionary representing the inbound connection configuration in JSON format.
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
                InboundFields.STREAM_SETTINGS: self.stream_settings.model_dump_json(by_alias=True),  # type: ignore
                InboundFields.SNIFFING: self.sniffing.model_dump_json(by_alias=True),  # pylint: disable=no-member  # type: ignore
            }
        )

        return result