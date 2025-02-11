"""This module contains the Inbound class, which represents an inbound connection in the XUI API."""

from typing import Any, List, Optional

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
    """Represents an inbound connection in the XUI API.

    Attributes:
        enable (bool): Whether the inbound connection is enabled. Required.
        port (int): The port number for the inbound connection. Required.
        protocol (str): The protocol for the inbound connection. Required.
        settings (Settings): The settings for the inbound connection. Required.
        stream_settings (StreamSettings): The stream settings for the inbound connection. Required.
        sniffing (Sniffing): The sniffing settings for the inbound connection. Required.
        listen (str): The listen address for the inbound connection. Optional.
        remark (str): The remark for the inbound connection. Optional.
        id (int): The ID of the inbound connection. Optional.
        up (int): The up value for the inbound connection. Optional.
        down (int): The down value for the inbound connection. Optional.
        total (int): The total value for the inbound connection. Optional.
        expiry_time (int): The expiry time for the inbound connection. Optional.
        client_stats (list[Client] | None): The client stats for the inbound connection. Optional.
        tag (str): The tag for the inbound connection. Optional.
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
    client_stats: Optional[List[Client]] = Field(default=None, alias=InboundFields.CLIENT_STATS)  # type: ignore

    tag: str = ""

    model_config = ConfigDict(
        populate_by_name=True,
    )

    def to_json(self) -> dict[str, Any]:
        """Converts the Inbound instance to a JSON-compatible dictionary for the XUI API.

        Returns:
            dict[str, Any]: The JSON-compatible dictionary.
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
                InboundFields.STREAM_SETTINGS: self.stream_settings.model_dump_json(
                    by_alias=True
                ),  # pylint: disable=no-member
                InboundFields.SNIFFING: self.sniffing.model_dump_json(by_alias=True),
            }
        )

        return result

    @classmethod
    def from_api_response(cls, data: dict[str, Any]) -> 'Inbound':
        """Creates an Inbound instance from an API response.

        Args:
            data (dict[str, Any]): The API response data.

        Returns:
            Inbound: The created Inbound instance.

        Example:
            >>> api_response = {
            ...     "remark": "My Inbound",
            ...     "enable": True,
            ...     "listen": "127.0.0.1",
            ...     "port": 8080,
            ...     "protocol": "vmess",
            ...     "expiryTime": 1672531200,
            ...     "settings": '{"..."',
            ...     "streamSettings": '{"..."',
            ...     "sniffing": '{"..."}'
            ... }
            >>> inbound = Inbound.from_api_response(api_response)
            >>> inbound
            Inbound(enable=True, port=8080, protocol='vmess', settings=Settings(...), stream_settings=StreamSettings(...), sniffing=Sniffing(...), listen='127.0.0.1', remark='My Inbound', id=0, up=0, down=0, total=0, expiry_time=1672531200, client_stats=None, tag='')
        """
        settings = Settings.model_validate_json(data[InboundFields.SETTINGS])
        stream_settings = StreamSettings.model_validate_json(data[InboundFields.STREAM_SETTINGS])
        sniffing = Sniffing.model_validate_json(data[InboundFields.SNIFFING])

        return cls(
            enable=data[InboundFields.ENABLE],
            port=data[InboundFields.PORT],
            protocol=data[InboundFields.PROTOCOL],
            settings=settings,
            stream_settings=stream_settings,
            sniffing=sniffing,
            listen=data.get(InboundFields.LISTEN, ""),
            remark=data.get(InboundFields.REMARK, ""),
            expiry_time=data.get(InboundFields.EXPIRY_TIME, 0),
            client_stats=[Client.model_validate(item) for item in data.get(InboundFields.CLIENT_STATS, [])] if data.get(InboundFields.CLIENT_STATS) else None,
            tag=data.get(InboundFields.TAG, "")
        )