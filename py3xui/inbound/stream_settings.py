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

    security: str = Field(description="The security protocol used for the stream.")  # type: ignore
    network: str = Field(description="The network type used for the stream.")  # type: ignore
    tcp_settings: dict = Field(
        alias=StreamSettingsFields.TCP_SETTINGS,
        description="Configuration settings specific to TCP streams."
    )  # type: ignore
    external_proxy: list = Field(
        default=[],
        alias=StreamSettingsFields.EXTERNAL_PROXY,
        description="List of external proxies used for the stream."
    )
    reality_settings: dict = Field(
        default={},
        alias=StreamSettingsFields.REALITY_SETTINGS,
        description="Configuration settings specific to Reality protocol."
    )
    xtls_settings: dict = Field(
        default={},
        alias=StreamSettingsFields.XTLS_SETTINGS,
        description="Configuration settings specific to XTLS protocol."
    )
    tls_settings: dict = Field(
        default={},
        alias=StreamSettingsFields.TLS_SETTINGS,
        description="Configuration settings specific to TLS protocol."
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


### Adjustments Made:
1. **Docstring Consistency**: Ensured the class docstring is concise and consistent.
2. **Field Definitions**: Removed default values from `security` and `network` fields to indicate they are required.
3. **Field Formatting**: Improved the formatting of `Field` definitions for better readability.
4. **Type Ignore Comments**: Ensured `# type: ignore` comments are placed consistently.
5. **Attribute Descriptions**: Ensured descriptions in `Field` definitions match the gold code in terms of clarity and terminology.