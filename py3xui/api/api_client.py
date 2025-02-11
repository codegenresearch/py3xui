import json
from typing import Any, List, Optional

from py3xui.api.api_base import ApiFields, BaseApi
from py3xui.client.client import Client
from py3xui.utils import Logger

logger = Logger(__name__)


class ClientApi(BaseApi):
    def get_by_email(self, email: str) -> Optional[Client]:
        """
        Retrieve information about a specific client based on their email.

        This endpoint provides details such as traffic statistics and other relevant information
        related to the client.

        `Source documentation <https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#9d0e5cd5-e6ac-4d72-abca-76cf75af5f00>`_

        Args:
            email (str): The email of the client to retrieve.

        Returns:
            Optional[Client]: The client object if found, otherwise None.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            client: py3xui.Client = api.client.get_by_email("email@example.com")
        """
        endpoint = f"panel/api/inbounds/getClientTraffics/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        logger.info("Getting client stats for email: %s", email)

        response = self._get(url, headers)

        client_json = response.json().get(ApiFields.OBJ)
        if not client_json:
            logger.warning("No client found for email: %s", email)
            return None
        return Client.model_validate(client_json)

    def get_ips(self, email: str) -> Optional[str]:
        """
        Retrieve the IP records associated with a specific client identified by their email.

        `Source documentation <https://documenter.getpostman.com/view/16802678/2s9YkgD5jm#06f1214c-dbb0-49f2-81b5-8e924abd19a9>`_

        Args:
            email (str): The email of the client to retrieve.

        Returns:
            Optional[str]: The client IPs if found, otherwise None.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            ips = api.client.get_ips("email@example.com")
        """
        endpoint = f"panel/api/inbounds/clientIps/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        logger.info("Getting client IPs for email: %s", email)

        response = self._post(url, headers, {})

        ips_json = response.json().get(ApiFields.OBJ)
        return ips_json if ips_json != ApiFields.NO_IP_RECORD else None

    def add(self, inbound_id: int, clients: List[Client]) -> None:
        """
        Add clients to a specific inbound.

        Args:
            inbound_id (int): The ID of the inbound to which clients will be added.
            clients (List[Client]): A list of Client objects to add.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            clients = [py3xui.Client(...)]
            api.client.add(1, clients)
        """
        endpoint = "panel/api/inbounds/addClient"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        settings = {
            "clients": [
                client.model_dump(by_alias=True, exclude_defaults=True) for client in clients
            ]
        }
        data = {"id": inbound_id, "settings": json.dumps(settings)}
        logger.info("Adding %s clients to inbound with ID: %s", len(clients), inbound_id)

        self._post(url, headers, data)
        logger.info("Clients added successfully.")

    def update(self, client_uuid: str, client: Client) -> None:
        """
        Update a specific client.

        Args:
            client_uuid (str): The UUID of the client to update.
            client (Client): The updated Client object.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            client = py3xui.Client(...)
            api.client.update("client-uuid", client)
        """
        endpoint = f"panel/api/inbounds/updateClient/{client_uuid}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        settings = {"clients": [client.model_dump(by_alias=True, exclude_defaults=True)]}
        data = {"id": client.inbound_id, "settings": json.dumps(settings)}

        logger.info("Updating client: %s", client)
        self._post(url, headers, data)
        logger.info("Client updated successfully.")

    def reset_ips(self, email: str) -> None:
        """
        Reset the IP records for a specific client.

        Args:
            email (str): The email of the client whose IPs will be reset.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            api.client.reset_ips("email@example.com")
        """
        endpoint = f"panel/api/inbounds/clearClientIps/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Resetting client IPs for email: %s", email)

        self._post(url, headers, data)
        logger.info("Client IPs reset successfully.")

    def reset_stats(self, inbound_id: int, email: str) -> None:
        """
        Reset the statistics for a specific client within an inbound.

        Args:
            inbound_id (int): The ID of the inbound.
            email (str): The email of the client whose statistics will be reset.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            api.client.reset_stats(1, "email@example.com")
        """
        endpoint = f"panel/api/inbounds/{inbound_id}/resetClientTraffic/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Resetting client stats for inbound ID: %s, email: %s", inbound_id, email)

        self._post(url, headers, data)
        logger.info("Client stats reset successfully.")

    def delete(self, inbound_id: int, client_uuid: str) -> None:
        """
        Delete a specific client from an inbound.

        Args:
            inbound_id (int): The ID of the inbound.
            client_uuid (str): The UUID of the client to delete.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            api.client.delete(1, "client-uuid")
        """
        endpoint = f"panel/api/inbounds/{inbound_id}/delClient/{client_uuid}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Deleting client with UUID: %s", client_uuid)

        self._post(url, headers, data)
        logger.info("Client deleted successfully.")

    def delete_depleted(self, inbound_id: int) -> None:
        """
        Delete all depleted clients from a specific inbound.

        Args:
            inbound_id (int): The ID of the inbound.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            api.client.delete_depleted(1)
        """
        endpoint = f"panel/api/inbounds/delDepletedClients/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Deleting depleted clients for inbound ID: %s", inbound_id)

        self._post(url, headers, data)
        logger.info("Depleted clients deleted successfully.")

    def online(self) -> List[str]:
        """
        Retrieve a list of online clients.

        Returns:
            List[str]: A list of online client UUIDs.

        Examples:
            import py3xui

            api = py3xui.Api.from_env()
            online_clients = api.client.online()
        """
        endpoint = "panel/api/inbounds/onlines"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Getting online clients")

        response = self._post(url, headers, data)
        online = response.json().get(ApiFields.OBJ)
        return online or []