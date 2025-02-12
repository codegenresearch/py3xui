"""This module contains the InboundApi class for handling inbounds in the XUI API."""

from typing import Any, Optional

from py3xui.api.api_base import ApiFields, BaseApi
from py3xui.inbound import Inbound


class InboundApi(BaseApi):
    """This class provides methods to interact with the inbounds in the XUI API.\n\n    Attributes and Properties:\n        host (str): The XUI host URL.\n        username (str): The XUI username.\n        password (str): The XUI password.\n        token (str | None): The XUI secret token.\n        use_tls_verify (bool): Whether to verify the server TLS certificate.\n        custom_certificate_path (str | None): Path to a custom certificate file.\n        session (requests.Session): The session object for the API.\n        max_retries (int): The maximum number of retries for the API requests.\n\n    Public Methods:\n        get_list: Retrieves a list of inbounds.\n        get_by_id: Retrieves a specific inbound by its ID.\n        add: Adds a new inbound.\n        delete: Deletes an inbound.\n        update: Updates an inbound.\n        reset_stats: Resets the statistics of all inbounds.\n        reset_client_stats: Resets the statistics of a specific inbound.\n\n    Examples:\n        \n        import py3xui\n\n        api = py3xui.Api.from_env()\n        api.login()\n\n        inbounds: list[py3xui.Inbound] = api.inbound.get_list()\n        inbound: py3xui.Inbound = api.inbound.get_by_id(1)\n        \n    """

    def get_list(self) -> list[Inbound]:
        """Retrieves a comprehensive list of all inbounds along with their associated\n        client options and statistics.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#b7c42b67-4362-44d3-bd61-ba7df0721802)\n\n        Returns:\n            list[Inbound]: A list of inbounds.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.Api.from_env()\n            api.login()\n\n            inbounds: list[py3xui.Inbound] = api.inbound.get_list()\n            \n        """
        endpoint = "panel/api/inbounds/list"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbounds...")

        response = self._get(url, headers)

        inbounds_json = response.json().get(ApiFields.OBJ, [])
        inbounds = [Inbound.model_validate(data) for data in inbounds_json]
        return inbounds

    def get_by_id(self, inbound_id: int) -> Optional[Inbound]:
        """Retrieves a specific inbound by its ID.\n\n        This route is used to retrieve statistics and details for a specific inbound connection\n        identified by the specified ID. This includes information about the inbound itself, its\n        statistics, and the clients connected to it.\n\n        [Source documentation](https://www.postman.com/hsanaei/3x-ui/request/uu7wm1k/inbound)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to retrieve.\n\n        Returns:\n            Inbound | None: The inbound object if found, otherwise None.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.Api.from_env()\n            api.login()\n\n            inbound_id = 1\n\n            inbound = api.inbound.get_by_id(inbound_id)\n            \n        """
        endpoint = f"panel/api/inbounds/get/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbound by ID: %s", inbound_id)

        response = self._get(url, headers)

        inbound_json = response.json().get(ApiFields.OBJ)
        if not inbound_json:
            return None

        inbound = Inbound.model_validate(inbound_json)
        return inbound

    def add(self, inbound: Inbound) -> None:
        """Adds a new inbound configuration.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#813ac729-5ba6-4314-bc2a-d0d3acc70388)\n\n        Arguments:\n            inbound (Inbound): The inbound object to add.\n\n        Examples:\n            \n            import py3xui\n            from py3xui.inbound import Inbound, Settings, Sniffing, StreamSettings\n\n            api = py3xui.Api.from_env()\n            api.login()\n\n            settings = Settings()\n            sniffing = Sniffing(enabled=True)\n\n            tcp_settings = {\n                "acceptProxyProtocol": False,\n                "header": {"type": "none"},\n            }\n            stream_settings = StreamSettings(security="reality", network="tcp", tcp_settings=tcp_settings)\n\n            inbound = Inbound(\n                enable=True,\n                port=443,\n                protocol="vless",\n                settings=settings,\n                stream_settings=stream_settings,\n                sniffing=sniffing,\n                remark="test3",\n            )\n\n            api.inbound.add(inbound)\n            \n        """
        endpoint = "panel/api/inbounds/add"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info("Adding inbound: %s", inbound)

        self._post(url, headers, data)
        self.logger.info("Inbound added successfully.")

    def delete(self, inbound_id: int) -> None:
        """Deletes an inbound identified by its ID.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#a655d0e3-7d8c-4331-9061-422fcb515da9)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to delete.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.Api.from_env()\n            api.login()\n            inbounds: list[py3xui.Inbound] = api.inbound.get_list()\n\n            for inbound in inbounds:\n                api.inbound.delete(inbound.id)\n            \n        """
        endpoint = f"panel/api/inbounds/del/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}

        self.logger.info("Deleting inbound with ID: %s", inbound_id)
        self._post(url, headers, data)
        self.logger.info("Inbound deleted successfully.")

    def update(self, inbound_id: int, inbound: Inbound) -> None:
        """Updates an existing inbound identified by its ID.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#19249b9f-a940-41e2-8bf4-86ff8dde857e)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to update.\n            inbound (Inbound): The inbound object to update.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.Api.from_env()\n            api.login()\n            inbounds: list[py3xui.Inbound] = api.inbound.get_list()\n            inbound = inbounds[0]\n\n            inbound.remark = "updated"\n\n            api.inbound.update(inbound.id, inbound)\n            \n        """
        endpoint = f"panel/api/inbounds/update/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info("Updating inbound: %s", inbound)

        self._post(url, headers, data)
        self.logger.info("Inbound updated successfully.")

    def reset_stats(self) -> None:
        """Resets the traffic statistics for all inbounds within the system.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#6749f362-dc81-4769-8f45-37dc9e99f5e9)\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.Api.from_env()\n            api.login()\n            api.inbound.reset_stats()\n            \n        """
        endpoint = "panel/api/inbounds/resetAllTraffics"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Resetting inbounds stats...")

        self._post(url, headers, data)
        self.logger.info("Inbounds stats reset successfully.")

    def reset_client_stats(self, inbound_id: int) -> None:
        """Resets the traffic statistics for all clients associated with a specific inbound.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#9bd93925-12a0-40d8-a390-d4874dea3683)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to reset the client stats.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.Api.from_env()\n            api.login()\n            inbounds: list[py3xui.Inbound] = api.inbound.get_list()\n            inbound = inbounds[0]\n\n            api.inbound.reset_client_stats(inbound.id)\n            \n        """
        endpoint = f"panel/api/inbounds/resetAllClientTraffics/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Resetting inbound client stats for ID: %s", inbound_id)

        self._post(url, headers, data)
        self.logger.info("Inbound client stats reset successfully.")