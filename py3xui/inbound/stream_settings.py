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
        security (str): The security protocol used for the stream.
        network (str): The network type used for the stream.
        tcp_settings (dict): Configuration settings specific to TCP streams.
        external_proxy (list): List of external proxies used for the stream.
        reality_settings (dict): Configuration settings specific to Reality protocol.
        xtls_settings (dict): Configuration settings specific to XTLS protocol.
        tls_settings (dict): Configuration settings specific to TLS protocol.
    """

    security: str = Field(description="The security protocol used for the stream.")
    network: str = Field(description="The network type used for the stream.")
    tcp_settings: dict = Field(
        default={}, alias=StreamSettingsFields.TCP_SETTINGS, description="Configuration settings specific to TCP streams."
    )
    external_proxy: list = Field(
        default=[], alias=StreamSettingsFields.EXTERNAL_PROXY, description="List of external proxies used for the stream."
    )
    reality_settings: dict = Field(
        default={}, alias=StreamSettingsFields.REALITY_SETTINGS, description="Configuration settings specific to Reality protocol."
    )
    xtls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.XTLS_SETTINGS, description="Configuration settings specific to XTLS protocol."
    )
    tls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.TLS_SETTINGS, description="Configuration settings specific to TLS protocol."
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )