"""This module contains the AsyncInboundApi class which provides asynchronous methods to interact with the
inbounds in the XUI API."""

from typing import Any, Optional

from py3xui.api.api_base import ApiFields
from py3xui.async_api.async_api_base import AsyncBaseApi
from py3xui.inbound import Inbound


class AsyncInboundApi(AsyncBaseApi):
    """This class provides asynchronous methods to interact with the inbounds in the XUI API.

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

    api = py3xui.AsyncApi.from_env()
    await api.login()

    inbounds: list[py3xui.Inbound] = await api.inbound.get_list()
    
    """

    async def get_list(self) -> list[Inbound]:
        """Retrieves a comprehensive list of all inbounds along with their associated client options and statistics.

        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#b7c42b67-4362-44d3-bd61-ba7df0721802)

        Returns:
            list[Inbound]: A list of inbounds.

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()
        inbounds: list[py3xui.Inbound] = await api.inbound.get_list()
        
        """  # pylint: disable=line-too-long
        endpoint = "panel/api/inbounds/list"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbounds...")

        response = await self._get(url, headers)

        inbounds_json = response.json().get(ApiFields.OBJ)
        inbounds = [Inbound.model_validate(data) for data in inbounds_json]
        return inbounds

    async def get_by_id(self, inbound_id: int) -> Inbound:
        """Retrieves a specific inbound by its ID, including its statistics and client details.

        [Source documentation](https://www.postman.com/hsanaei/3x-ui/request/uu7wm1k/inbound)

        Arguments:
            inbound_id (int): The ID of the inbound to retrieve.

        Returns:
            Inbound: The inbound object if found.

        Raises:
            ValueError: If the inbound is not found.

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()

        inbound_id = 1
        inbound = await api.inbound.get_by_id(inbound_id)
        
        """  # pylint: disable=line-too-long
        endpoint = f"panel/api/inbounds/get/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        self.logger.info("Getting inbound by ID: %s", inbound_id)

        response = await self._get(url, headers)

        inbound_json = response.json().get(ApiFields.OBJ)
        if inbound_json:
            inbound = Inbound.model_validate(inbound_json)
            return inbound
        self.logger.error("Inbound with ID %s not found", inbound_id)
        raise ValueError(f"Inbound with ID {inbound_id} not found")

    async def add(self, inbound: Inbound) -> None:
        """Adds a new inbound configuration.

        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#813ac729-5ba6-4314-bc2a-d0d3acc70388)

        Arguments:
            inbound (Inbound): The inbound object to add.

        Returns:
            None

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()

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
        await api.inbound.add(inbound)
        
        """  # pylint: disable=line-too-long
        endpoint = "panel/api/inbounds/add"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info("Adding inbound: %s", inbound)

        await self._post(url, headers, data)
        self.logger.info("Inbound added successfully.")

    async def delete(self, inbound_id: int) -> None:
        """Deletes an inbound identified by its ID.

        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#a655d0e3-7d8c-4331-9061-422fcb515da9)

        Arguments:
            inbound_id (int): The ID of the inbound to delete.

        Returns:
            None

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()
        inbounds: list[py3xui.Inbound] = await api.inbound.get_list()

        for inbound in inbounds:
            await api.inbound.delete(inbound.id)
        
        """  # pylint: disable=line-too-long
        endpoint = f"panel/api/inbounds/del/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}

        self.logger.info("Deleting inbound with ID: %s", inbound_id)
        await self._post(url, headers, data)
        self.logger.info("Inbound deleted successfully.")

    async def update(self, inbound_id: int, inbound: Inbound) -> None:
        """Updates an existing inbound identified by its ID.

        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#19249b9f-a940-41e2-8bf4-86ff8dde857e)

        Arguments:
            inbound_id (int): The ID of the inbound to update.
            inbound (Inbound): The inbound object with updated details.

        Returns:
            None

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()
        inbounds: list[py3xui.Inbound] = await api.inbound.get_list()
        inbound = inbounds[0]

        inbound.remark = "updated"

        await api.inbound.update(inbound.id, inbound)
        
        """  # pylint: disable=line-too-long
        endpoint = f"panel/api/inbounds/update/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = inbound.to_json()
        self.logger.info("Updating inbound: %s", inbound)

        await self._post(url, headers, data)
        self.logger.info("Inbound updated successfully.")

    async def reset_stats(self) -> None:
        """Resets the traffic statistics for all inbounds within the system.

        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#6749f362-dc81-4769-8f45-37dc9e99f5e9)

        Returns:
            None

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()
        await api.inbound.reset_stats()
        
        """  # pylint: disable=line-too-long
        endpoint = "panel/api/inbounds/resetAllTraffics"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Resetting inbounds stats...")

        await self._post(url, headers, data)
        self.logger.info("Inbounds stats reset successfully.")

    async def reset_client_stats(self, inbound_id: int) -> None:
        """Resets the traffic statistics for all clients associated with a specific inbound identified by its ID.

        [Source documentation](https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#9bd93925-12a0-40d8-a390-d4874dea3683)

        Arguments:
            inbound_id (int): The ID of the inbound to reset the client stats.

        Returns:
            None

        Examples:
        
        import py3xui

        api = py3xui.AsyncApi.from_env()
        await api.login()
        inbounds: list[py3xui.Inbound] = await api.inbound.get_list()
        inbound = inbounds[0]

        await api.inbound.reset_client_stats(inbound.id)
        
        """  # pylint: disable=line-too-long
        endpoint = f"panel/api/inbounds/resetAllClientTraffics/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Resetting inbound client stats for ID: %s", inbound_id)

        await self._post(url, headers, data)
        self.logger.info("Inbound client stats reset successfully.")


This revised code addresses the feedback by ensuring consistent docstring formatting, detailed method descriptions, clear logging messages, and properly formatted example code snippets. The `get_by_id` method now raises a `ValueError` if the inbound is not found, and the logging messages provide clear context.