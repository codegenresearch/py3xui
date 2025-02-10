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

    ENABLE = "enable"  # Field for enabling or disabling the inbound
    PORT = "port"  # Field for the port number of the inbound
    PROTOCOL = "protocol"  # Field for the protocol used by the inbound
    SETTINGS = "settings"  # Field for the settings of the inbound
    STREAM_SETTINGS = "streamSettings"  # Field for the stream settings of the inbound
    SNIFFING = "sniffing"  # Field for the sniffing settings of the inbound

    ID = "id"  # Field for the unique identifier of the inbound
    UP = "up"  # Field for the upload traffic of the inbound
    DOWN = "down"  # Field for the download traffic of the inbound
    TOTAL = "total"  # Field for the total traffic of the inbound
    REMARK = "remark"  # Field for any remarks or notes about the inbound

    EXPIRY_TIME = "expiryTime"  # Field for the expiry time of the inbound
    CLIENT_STATS = "clientStats"  # Field for the client statistics of the inbound
    LISTEN = "listen"  # Field for the listening address of the inbound

    TAG = "tag"  # Field for the tag associated with the inbound


class Inbound(BaseModel):
    """Represents an inbound configuration from the XUI API.

    Attributes:
        enable (bool): Indicates whether the inbound is enabled. (Required)
        port (int): The port number on which the inbound listens. (Required)
        protocol (str): The protocol used by the inbound (e.g., vmess, vless). (Required)
        settings (Settings): The settings specific to the protocol. (Required)
        stream_settings (StreamSettings): Stream settings for the inbound. (Required)
        sniffing (Sniffing): Sniffing settings for the inbound. (Required)
        listen (str): The address on which the inbound listens. (Optional, default is an empty string)
        remark (str): Any remarks or notes about the inbound. (Optional, default is an empty string)
        id (int): The unique identifier for the inbound. (Optional, default is 0)
        up (int): The upload traffic of the inbound. (Optional, default is 0)
        down (int): The download traffic of the inbound. (Optional, default is 0)
        total (int): The total traffic of the inbound. (Optional, default is 0)
        expiry_time (int): The expiry time of the inbound. (Optional, default is 0)
        client_stats (list[Client]): List of client statistics. (Optional, default is an empty list)
        tag (str): The tag associated with the inbound. (Optional, default is an empty string)
    """

    enable: bool  # Required: Indicates whether the inbound is enabled
    port: int  # Required: The port number on which the inbound listens
    protocol: str  # Required: The protocol used by the inbound (e.g., vmess, vless)
    settings: Settings  # Required: The settings specific to the protocol
    stream_settings: StreamSettings = Field(alias=InboundFields.STREAM_SETTINGS)  # Required: Stream settings for the inbound # type: ignore
    sniffing: Sniffing  # Required: Sniffing settings for the inbound

    listen: str = ""  # Optional: The address on which the inbound listens (default is an empty string)
    remark: str = ""  # Optional: Any remarks or notes about the inbound (default is an empty string)
    id: int = 0  # Optional: The unique identifier for the inbound (default is 0)

    up: int = 0  # Optional: The upload traffic of the inbound (default is 0)
    down: int = 0  # Optional: The download traffic of the inbound (default is 0)
    total: int = 0  # Optional: The total traffic of the inbound (default is 0)

    expiry_time: int = Field(default=0, alias=InboundFields.EXPIRY_TIME)  # Optional: The expiry time of the inbound (default is 0) # type: ignore
    client_stats: list[Client] = Field(default=[], alias=InboundFields.CLIENT_STATS)  # Optional: List of client statistics (default is an empty list) # type: ignore

    tag: str = ""  # Optional: The tag associated with the inbound (default is an empty string)

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
                InboundFields.STREAM_SETTINGS: self.stream_settings.model_dump_json(by_alias=True),  # pylint: disable=no-member
                InboundFields.SNIFFING: self.sniffing.model_dump_json(by_alias=True),
            }
        )

        return result