from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from py3xui.client.client import Client
from py3xui.inbound.settings import Settings
from py3xui.inbound.sniffing import Sniffing
from py3xui.inbound.stream_settings import StreamSettings

# Module-level docstring for clarity
# This module defines the Inbound class and InboundFields class used to parse and represent inbound configurations from the XUI API.

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
    """Represents an inbound configuration from the XUI API.

    Attributes:
        enable (bool): Indicates whether the inbound is enabled.
        port (int): The port number on which the inbound listens.
        protocol (str): The protocol used by the inbound (e.g., vmess, vless).
        settings (Settings): The settings specific to the protocol.
        stream_settings (StreamSettings): Stream settings for the inbound.
        sniffing (Sniffing): Sniffing settings for the inbound.
        listen (str): The address on which the inbound listens. Defaults to an empty string.
        remark (str): Any remarks or notes about the inbound. Defaults to an empty string.
        id (int): The unique identifier for the inbound. Defaults to 0.
        up (int): The upload traffic of the inbound. Defaults to 0.
        down (int): The download traffic of the inbound. Defaults to 0.
        total (int): The total traffic of the inbound. Defaults to 0.
        expiry_time (int): The expiry time of the inbound. Defaults to 0.
        client_stats (list[Client]): List of client statistics. Defaults to an empty list.
        tag (str): The tag associated with the inbound. Defaults to an empty string.
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
        """Converts the inbound configuration to a JSON-compatible dictionary.

        This method includes only specific fields in the output and serializes nested models to JSON strings.

        Returns:
            dict[str, Any]: A dictionary representing the inbound configuration in JSON format.
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
                InboundFields.SNIFFING: self.sniffing.model_dump_json(by_alias=True),  # type: ignore
            }
        )

        return result