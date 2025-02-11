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
        security (str): The security protocol used for the stream. Required.
        network (str): The network type used for the stream. Required.
        tcp_settings (dict): Configuration settings specific to TCP streams. Required.
        external_proxy (list): List of external proxies used for the stream. Optional.
        reality_settings (dict): Configuration settings specific to Reality protocol. Optional.
        xtls_settings (dict): Configuration settings specific to XTLS protocol. Optional.
        tls_settings (dict): Configuration settings specific to TLS protocol. Optional.
    """

    security: str = Field(description="The security protocol used for the stream.")
    network: str = Field(description="The network type used for the stream.")
    tcp_settings: dict = Field(
        alias=StreamSettingsFields.TCP_SETTINGS, description="Configuration settings specific to TCP streams."
    )  # type: ignore
    external_proxy: list = Field(
        default=[], alias=StreamSettingsFields.EXTERNAL_PROXY, description="List of external proxies used for the stream."
    )  # type: ignore
    reality_settings: dict = Field(
        default={}, alias=StreamSettingsFields.REALITY_SETTINGS, description="Configuration settings specific to Reality protocol."
    )  # type: ignore
    xtls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.XTLS_SETTINGS, description="Configuration settings specific to XTLS protocol."
    )  # type: ignore
    tls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.TLS_SETTINGS, description="Configuration settings specific to TLS protocol."
    )  # type: ignore

    model_config = ConfigDict(
        populate_by_name=True,
    )