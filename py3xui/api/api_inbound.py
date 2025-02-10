"""This module contains the InboundApi class for handling inbounds in the XUI API."""

from typing import Any, List

from py3xui.api.api_base import ApiFields, BaseApi
from py3xui.inbound import Inbound


class InboundApi(BaseApi):
    """This class provides methods to interact with the inbounds in the XUI API.

    Attributes and Properties:
        host (str): The XUI host URL.
        username (str): The XUI username.
        password (str): The XUI password.
        token (str | None): The XUI secret token.
        use_tls_verify (bool): Whether to verify the server TLS certificate.
        custom_certificate_path (str | None): Path to a custom certificate file.
        session (requests.Session): The session object for the API.
        max_retries (int): The maximum number of retries for the API requests.

    Public Methods:
        get_list: Retrieves a list of inbounds.
        get_by_id: Retrieves a specific inbound by its ID.
        add: Adds a new inbound.
        delete: Deletes an inbound.
        update: Updates an inbound.
        reset_stats: Resets the statistics of all inbounds.
        reset_client_stats: Resets the statistics of a specific inbound.

    Examples:
    
    import py3xui

    api = py3xui.Api.from_env()
    api.login()

    inbounds: list[py3xui.Inbound] = api.inbound.get_list()
    
    """

    def get_list(self) -> list[Inbound]:
        """Retrieves a list of all inbounds.

        Returns:
            list[Inbound]: A list of inbounds.

        Examples:
        
        import py3xui

        api = py3xui.Api.from_env()
        api.login()

        inbounds: list[py3xui.Inbound] = api.inbound.get_list()
        
        """
        endpoint = "panel/api/inbounds/list"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbounds...")
        response = self._get(url, headers)

        inbounds_json = response.json().get(ApiFields.OBJ, [])
        inbounds = [Inbound.model_validate(data) for data in inbounds_json]
        return inbounds

    def get_by_id(self, inbound_id: int) -> Inbound:
        """Retrieves an inbound by its ID.

        Args:
            inbound_id (int): The ID of the inbound to retrieve.

        Returns:
            Inbound: The inbound object.

        Raises:
            ValueError: If the inbound is not found.

        Examples:
        
        import py3xui

        api = py3xui.Api.from_env()
        api.login()

        inbound_id = 1

        inbound = api.inbound.get_by_id(inbound_id)
        
        """
        endpoint = f"panel/api/inbounds/get/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info(f"Getting inbound by ID: {inbound_id}")
        response = self._get(url, headers)

        inbound_json = response.json().get(ApiFields.OBJ)
        if inbound_json:
            return Inbound.model_validate(inbound_json)
        else:
            raise ValueError(f"Inbound with ID {inbound_id} not found.")

    def add(self, inbound: Inbound) -> None:
        """Adds a new inbound.

        Args:
            inbound (Inbound): The inbound object to add.

        Examples:
        
        import py3xui
        from py3xui.inbound import Inbound, Settings, Sniffing, StreamSettings

        api = py3xui.Api.from_env()
        api.login()

        settings = Settings()
        sniffing = Sniffing(enabled=True)

        tcp_settings = {
            "acceptProxyProtocol": False,
            "header": {"type": "none"},
        }
        stream_settings = StreamSettings(security="reality", network="tcp", tcp_settings=tcp_settings)

        inbound = Inbound(
            enable=True,
            port=443,
            protocol="vless",
            settings=settings,
            stream_settings=stream_settings,
            sniffing=sniffing,
            remark="test3",
        )

        api.inbound.add(inbound)
        
        """
        endpoint = "panel/api/inbounds/add"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info(f"Adding inbound: {inbound}")
        self._post(url, headers, data)

    def delete(self, inbound_id: int) -> None:
        """Deletes an inbound by its ID.

        Args:
            inbound_id (int): The ID of the inbound to delete.

        Examples:
        
        import py3xui

        api = py3xui.Api.from_env()
        api.login()
        inbounds: list[py3xui.Inbound] = api.inbound.get_list()

        for inbound in inbounds:
            api.inbound.delete(inbound.id)
        
        """
        endpoint = f"panel/api/inbounds/del/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info(f"Deleting inbound with ID: {inbound_id}")
        self._post(url, headers, data)

    def update(self, inbound_id: int, inbound: Inbound) -> None:
        """Updates an existing inbound by its ID.

        Args:
            inbound_id (int): The ID of the inbound to update.
            inbound (Inbound): The inbound object to update.

        Examples:
        
        import py3xui

        api = py3xui.Api.from_env()
        api.login()
        inbounds: list[py3xui.Inbound] = api.inbound.get_list()
        inbound = inbounds[0]

        inbound.remark = "updated"

        api.inbound.update(inbound.id, inbound)
        
        """
        endpoint = f"panel/api/inbounds/update/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info(f"Updating inbound: {inbound}")
        self._post(url, headers, data)

    def reset_stats(self) -> None:
        """Resets the statistics of all inbounds.

        Examples:
        
        import py3xui

        api = py3xui.Api.from_env()
        api.login()
        api.inbound.reset_stats()
        
        """
        endpoint = "panel/api/inbounds/resetAllTraffics"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Resetting inbounds stats...")
        self._post(url, headers, data)

    def reset_client_stats(self, inbound_id: int) -> None:
        """Resets the statistics of a specific inbound's clients.

        Args:
            inbound_id (int): The ID of the inbound to reset the client stats.

        Examples:
        
        import py3xui

        api = py3xui.Api.from_env()
        api.login()
        inbounds: list[py3xui.Inbound] = api.inbound.get_list()
        inbound = inbounds[0]

        api.inbound.reset_client_stats(inbound.id)
        
        """
        endpoint = f"panel/api/inbounds/resetAllClientTraffics/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info(f"Resetting inbound client stats for ID: {inbound_id}")
        self._post(url, headers, data)