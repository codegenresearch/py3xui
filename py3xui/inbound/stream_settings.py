"""This module contains the StreamSettings class, which is used to parse the JSON response
from the XUI API for stream settings."""

from pydantic import ConfigDict, Field

from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class StreamSettingsFields:
    """Stores the fields returned by the XUI API for parsing."""

    SECURITY = "security"
    NETWORK = "network"
    TCP_SETTINGS = "tcpSettings"

    EXTERNAL_PROXY = "externalProxy"

    REALITY_SETTINGS = "realitySettings"
    XTLS_SETTINGS = "xtlsSettings"
    TLS_SETTINGS = "tlsSettings"


class StreamSettings(JsonStringModel):
    """Represents the stream settings for an inbound connection.

    Attributes:
        security (str): The security protocol for the stream.
        network (str): The network type for the stream.
        tcp_settings (dict): The TCP settings for the stream.
        external_proxy (list): The external proxy settings for the stream. Optional.
        reality_settings (dict): The Reality settings for the stream. Optional.
        xtls_settings (dict): The xTLS settings for the stream. Optional.
        tls_settings (dict): The TLS settings for the stream. Optional.
    """

    security: str
    network: str
    tcp_settings: dict = Field(alias=StreamSettingsFields.TCP_SETTINGS)  # type: ignore

    external_proxy: list = Field(  # type: ignore
        default=[], alias=StreamSettingsFields.EXTERNAL_PROXY
    )

    reality_settings: dict = Field(  # type: ignore
        default={}, alias=StreamSettingsFields.REALITY_SETTINGS
    )
    xtls_settings: dict = Field(  # type: ignore
        default={}, alias=StreamSettingsFields.XTLS_SETTINGS
    )
    tls_settings: dict = Field(default={}, alias=StreamSettingsFields.TLS_SETTINGS)  # type: ignore

    model_config = ConfigDict(
        populate_by_name=True,
    )