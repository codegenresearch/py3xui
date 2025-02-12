"""This module contains the AsyncInboundApi class which provides methods to interact with the\ninbounds in the XUI API asynchronously."""

from typing import Any, Optional

from py3xui.api.api_base import ApiFields
from py3xui.async_api.async_api_base import AsyncBaseApi
from py3xui.inbound import Inbound


class AsyncInboundApi(AsyncBaseApi):
    """This class provides methods to interact with the inbounds in the XUI API asynchronously.\n\n    Attributes and Properties:\n        host (str): The XUI host URL.\n        username (str): The XUI username.\n        password (str): The XUI password.\n        token (str | None): The XUI secret token.\n        use_tls_verify (bool): Whether to verify the server TLS certificate.\n        custom_certificate_path (str | None): Path to a custom certificate file.\n        session (requests.Session): The session object for the API.\n        max_retries (int): The maximum number of retries for the API requests.\n\n    Public Methods:\n        get_list: Retrieves a list of inbounds.\n        get_by_id: Retrieves a specific inbound by its ID.\n        add: Adds a new inbound.\n        delete: Deletes an inbound.\n        update: Updates an inbound.\n        reset_stats: Resets the statistics of all inbounds.\n        reset_client_stats: Resets the statistics of a specific inbound optionally.\n\n    Examples:\n        \n        import py3xui\n\n        api = py3xui.AsyncApi.from_env()\n        await api.login()\n\n        inbounds: list[py3xui.Inbound] = await api.inbound.get_list()\n        \n    """

    async def get_list(self) -> list[Inbound]:
        """Retrieves a comprehensive list of all inbounds along with their associated client options and statistics.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#b7c42b67-4362-44d3-bd61-ba7df0721802)\n\n        Returns:\n            list[Inbound]: A list of inbound configurations.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n\n            inbounds: list[py3xui.Inbound] = await api.inbound.get_list()\n            \n        """
        endpoint = "panel/api/inbounds/list"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbounds...")

        response = await self._get(url, headers)

        inbounds_json = response.json().get(ApiFields.OBJ)
        inbounds = [Inbound.model_validate(data) for data in inbounds_json]
        return inbounds

    async def get_by_id(self, inbound_id: int) -> Inbound:
        """Retrieves a specific inbound by its ID, including details and statistics.\n\n        [Source documentation](https://www.postman.com/hsanaei/3x-ui/request/uu7wm1k/inbound)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to retrieve.\n\n        Returns:\n            Inbound: The inbound object if found.\n\n        Raises:\n            Exception: If the inbound is not found.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n\n            inbound_id = 1\n            inbound = await api.inbound.get_by_id(inbound_id)\n            \n        """
        endpoint = f"panel/api/inbounds/get/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbound by ID: %s", inbound_id)

        response = await self._get(url, headers)

        inbound_json = response.json().get(ApiFields.OBJ)
        inbound = Inbound.model_validate(inbound_json)
        return inbound

    async def add(self, inbound: Inbound) -> None:
        """Adds a new inbound configuration.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#813ac729-5ba6-4314-bc2a-d0d3acc70388)\n\n        Arguments:\n            inbound (Inbound): The inbound object to add.\n\n        Examples:\n            \n            import py3xui\n            from py3xui.inbound import Inbound, Settings, Sniffing, StreamSettings\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n\n            settings = Settings()\n            sniffing = Sniffing(enabled=True)\n\n            tcp_settings = {\n                "acceptProxyProtocol": False,\n                "header": {"type": "none"},\n            }\n            stream_settings = StreamSettings(security="reality", network="tcp", tcp_settings=tcp_settings)\n\n            inbound = Inbound(\n                enable=True,\n                port=443,\n                protocol="vless",\n                settings=settings,\n                stream_settings=stream_settings,\n                sniffing=sniffing,\n                remark="test3",\n            )\n\n            await api.inbound.add(inbound)\n            \n        """
        endpoint = "panel/api/inbounds/add"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info("Adding inbound: %s", inbound)

        await self._post(url, headers, data)
        self.logger.info("Inbound added successfully.")

    async def delete(self, inbound_id: int) -> None:
        """Deletes an inbound identified by its ID.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#a655d0e3-7d8c-4331-9061-422fcb515da9)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to delete.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n            inbounds: list[py3xui.Inbound] = await api.inbound.get_list()\n\n            for inbound in inbounds:\n                await api.inbound.delete(inbound.id)\n            \n        """
        endpoint = f"panel/api/inbounds/del/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}

        self.logger.info("Deleting inbound with ID: %s", inbound_id)
        await self._post(url, headers, data)
        self.logger.info("Inbound deleted successfully.")

    async def update(self, inbound_id: int, inbound: Inbound) -> None:
        """Updates an existing inbound identified by its ID.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#19249b9f-a940-41e2-8bf4-86ff8dde857e)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to update.\n            inbound (Inbound): The inbound object containing the updated details.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n            inbounds: list[py3xui.Inbound] = await api.inbound.get_list()\n            inbound = inbounds[0]\n\n            inbound.remark = "updated"\n\n            await api.inbound.update(inbound.id, inbound)\n            \n        """
        endpoint = f"panel/api/inbounds/update/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info("Updating inbound: %s", inbound)

        await self._post(url, headers, data)
        self.logger.info("Inbound updated successfully.")

    async def reset_stats(self) -> None:
        """Resets the traffic statistics for all inbounds within the system.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#6749f362-dc81-4769-8f45-37dc9e99f5e9)\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n            await api.inbound.reset_stats()\n            \n        """
        endpoint = "panel/api/inbounds/resetAllTraffics"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Resetting inbounds stats...")

        await self._post(url, headers, data)
        self.logger.info("Inbounds stats reset successfully.")

    async def reset_client_stats(self, inbound_id: int, client_stats: Optional[bool] = True) -> None:
        """Resets the traffic statistics for all clients associated with a specific inbound identified by its ID.\n\n        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#9bd93925-12a0-40d8-a390-d4874dea3683)\n\n        Arguments:\n            inbound_id (int): The ID of the inbound to reset the client stats.\n            client_stats (bool, optional): Whether to reset client stats. Defaults to True.\n\n        Examples:\n            \n            import py3xui\n\n            api = py3xui.AsyncApi.from_env()\n            await api.login()\n            inbounds: list[py3xui.Inbound] = await api.inbound.get_list()\n            inbound = inbounds[0]\n\n            await api.inbound.reset_client_stats(inbound.id)\n            \n        """
        endpoint = f"panel/api/inbounds/resetAllClientTraffics/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {"client_stats": client_stats}
        self.logger.info("Resetting inbound client stats for ID: %s", inbound_id)

        await self._post(url, headers, data)
        self.logger.info("Inbound client stats reset successfully.")