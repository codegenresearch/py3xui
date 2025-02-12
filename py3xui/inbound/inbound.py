"""This module contains the Inbound class, which represents an inbound connection in the XUI API."""

from typing import Any, Optional, List
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
    """Represents an inbound connection in the XUI API.\n\n    Attributes:\n        enable (bool): Whether the inbound connection is enabled. Required.\n        port (int): The port number for the inbound connection. Required.\n        protocol (str): The protocol for the inbound connection. Required.\n        settings (Settings): The settings for the inbound connection. Required.\n        stream_settings (StreamSettings): The stream settings for the inbound connection. Required.\n        sniffing (Sniffing): The sniffing settings for the inbound connection. Required.\n        listen (str): The listen address for the inbound connection. Optional.\n        remark (str): The remark for the inbound connection. Optional.\n        id (int): The ID of the inbound connection. Optional.\n        up (int): The up value for the inbound connection. Optional.\n        down (int): The down value for the inbound connection. Optional.\n        total (int): The total value for the inbound connection. Optional.\n        expiry_time (int): The expiry time for the inbound connection. Optional.\n        client_stats (list[Client]): The client stats for the inbound connection. Optional.\n        tag (str): The tag for the inbound connection. Optional.\n\n    Examples:\n        >>> inbound = Inbound(\n        ...     enable=True,\n        ...     port=8080,\n        ...     protocol="vmess",\n        ...     settings=Settings(),\n        ...     stream_settings=StreamSettings(security="none", network="tcp"),\n        ...     sniffing=Sniffing(enabled=True, dest_override=["http", "tls"])\n        ... )\n        >>> inbound.to_json()\n        {'remark': '', 'enable': True, 'listen': '', 'port': 8080, 'protocol': 'vmess', 'expiryTime': 0, 'settings': '{}', 'streamSettings': '{"security": "none", "network": "tcp", "tcpSettings": {}, "kcpSettings": {}, "externalProxy": [], "realitySettings": {}, "xtlsSettings": {}, "tlsSettings": {}}', 'sniffing': '{"enabled": true, "destOverride": ["http", "tls"]}'}\n    """

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
    client_stats: List[Client] = Field(default=[], alias=InboundFields.CLIENT_STATS)  # type: ignore

    tag: str = ""

    model_config = ConfigDict(
        populate_by_name=True,
    )

    def to_json(self) -> dict[str, Any]:
        """Converts the Inbound instance to a JSON-compatible dictionary for the XUI API.\n\n        Returns:\n            dict[str, Any]: The JSON-compatible dictionary.\n\n        Examples:\n            >>> inbound = Inbound(\n            ...     enable=True,\n            ...     port=8080,\n            ...     protocol="vmess",\n            ...     settings=Settings(),\n            ...     stream_settings=StreamSettings(security="none", network="tcp"),\n            ...     sniffing=Sniffing(enabled=True, dest_override=["http", "tls"])\n            ... )\n            >>> inbound.to_json()\n            {'remark': '', 'enable': True, 'listen': '', 'port': 8080, 'protocol': 'vmess', 'expiryTime': 0, 'settings': '{}', 'streamSettings': '{"security": "none", "network": "tcp", "tcpSettings": {}, "kcpSettings": {}, "externalProxy": [], "realitySettings": {}, "xtlsSettings": {}, "tlsSettings": {}}', 'sniffing': '{"enabled": true, "destOverride": ["http", "tls"]}'}\n        """

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

    @staticmethod
    async def get_inbound_by_id(client: Client, inbound_id: int) -> Optional['Inbound']:
        """Retrieves an inbound by its ID asynchronously.\n\n        Args:\n            client (Client): The client instance to interact with the XUI API.\n            inbound_id (int): The ID of the inbound to retrieve.\n\n        Returns:\n            Optional[Inbound]: The Inbound instance if found, otherwise None.\n\n        Examples:\n            >>> client = Client(api_url="https://api.example.com", api_token="your_token")\n            >>> inbound = await Inbound.get_inbound_by_id(client, inbound_id=1)\n            >>> if inbound:\n            ...     print(inbound.remark)\n        """
        response = await client.get(f"/inbounds/{inbound_id}")
        if response.status_code == 200:
            return Inbound(**response.json())
        return None