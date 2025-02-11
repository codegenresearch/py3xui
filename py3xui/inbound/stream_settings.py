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
        security (str): Security protocol. Required.
        network (str): Network type. Required.
        tcp_settings (dict): TCP settings. Required.
        external_proxy (list): External proxy settings. Optional.
        reality_settings (dict): Reality settings. Optional.
        xtls_settings (dict): xTLS settings. Optional.
        tls_settings (dict): TLS settings. Optional.
    """

    security: str
    network: str
    tcp_settings: dict = Field(alias=StreamSettingsFields.TCP_SETTINGS)  # type: ignore

    external_proxy: list = Field(
        default=[], alias=StreamSettingsFields.EXTERNAL_PROXY
    )  # type: ignore

    reality_settings: dict = Field(
        default={}, alias=StreamSettingsFields.REALITY_SETTINGS
    )  # type: ignore

    xtls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.XTLS_SETTINGS
    )  # type: ignore

    tls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.TLS_SETTINGS
    )  # type: ignore

    model_config = ConfigDict(
        populate_by_name=True,
    )