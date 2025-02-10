from pydantic import ConfigDict, Field

from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class StreamSettingsFields:
    """Stores the fields returned by the XUI API for parsing.

    Attributes:
        SECURITY (str): The key for the security settings in the API response.
        NETWORK (str): The key for the network settings in the API response.
        TCP_SETTINGS (str): The key for the TCP settings in the API response.
        EXTERNAL_PROXY (str): The key for the external proxy settings in the API response.
        REALITY_SETTINGS (str): The key for the reality settings in the API response.
        XTLS_SETTINGS (str): The key for the XTLS settings in the API response.
        TLS_SETTINGS (str): The key for the TLS settings in the API response.
    """

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
        tcp_settings (dict): The TCP-specific settings for the stream.
        external_proxy (list): The external proxy settings for the stream.
        reality_settings (dict): The reality-specific settings for the stream.
        xtls_settings (dict): The XTLS-specific settings for the stream.
        tls_settings (dict): The TLS-specific settings for the stream.
    """

    security: str
    network: str
    tcp_settings: dict = Field(
        alias=StreamSettingsFields.TCP_SETTINGS, default={}
    )  # type: ignore

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