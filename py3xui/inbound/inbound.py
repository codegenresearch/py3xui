from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from py3xui.client.client import Client
from py3xui.inbound.settings import Settings
from py3xui.inbound.sniffing import Sniffing
from py3xui.inbound.stream_settings import StreamSettings

# Represents the inbound configuration for the XUI API.
# This module defines the Inbound class, which encapsulates all necessary settings and statistics for an inbound connection.

class Inbound(BaseModel):
    """
    Represents an inbound connection configuration for the XUI API.

    Attributes:
        enable (bool): Whether the inbound is enabled.
        port (int): The port number for the inbound.
        protocol (str): The protocol used by the inbound.
        settings (Settings): The settings for the inbound.
        stream_settings (StreamSettings): The stream settings for the inbound.
        sniffing (Sniffing): The sniffing settings for the inbound.
        listen (str): The address to listen on. Defaults to an empty string.
        remark (str): A remark for the inbound. Defaults to an empty string.
        id (int): The unique identifier for the inbound. Defaults to 0.
        up (int): The upload traffic. Defaults to 0.
        down (int): The download traffic. Defaults to 0.
        total (int): The total traffic. Defaults to 0.
        expiry_time (int): The expiry time for the inbound. Defaults to 0.
        client_stats (list[Client]): The client statistics for the inbound. Defaults to an empty list.
        tag (str): A tag for the inbound. Defaults to an empty string.
    """

    enable: bool
    port: int
    protocol: str
    settings: Settings
    stream_settings: StreamSettings = Field(alias="streamSettings")  # type: ignore
    sniffing: Sniffing

    listen: str = ""
    remark: str = ""
    id: int = 0

    up: int = 0
    down: int = 0

    total: int = 0

    expiry_time: int = Field(default=0, alias="expiryTime")  # type: ignore
    client_stats: list[Client] = Field(default=[], alias="clientStats")  # type: ignore

    tag: str = ""

    model_config = ConfigDict(
        populate_by_name=True,
    )

    def to_json(self) -> dict[str, Any]:
        """
        Converts the inbound configuration to a JSON-compatible dictionary for the XUI API.

        Returns:
            dict[str, Any]: A dictionary representing the inbound configuration.
        """
        include = {
            "remark",
            "enable",
            "listen",
            "port",
            "protocol",
            "expiryTime",
        }

        result = super().model_dump(by_alias=True)
        result = {k: v for k, v in result.items() if k in include}
        result.update(
            {
                "settings": self.settings.model_dump_json(by_alias=True),
                "streamSettings": self.stream_settings.model_dump_json(by_alias=True),  # pylint: disable=no-member
                "sniffing": self.sniffing.model_dump_json(by_alias=True),
            }
        )

        return result