import json
from typing import Any, List, Optional

from py3xui.api.api_base import ApiFields, BaseApi
from py3xui.client.client import Client
from py3xui.utils import Logger

logger = Logger(__name__)


class ClientApi(BaseApi):
    def get_by_email(self, email: str) -> Optional[Client]:
        """\n        Retrieve information about a specific client based on their email.\n\n        This endpoint provides details such as traffic statistics and other relevant information\n        related to the client.\n\n        Args:\n            email (str): The email of the client to retrieve.\n\n        Returns:\n            Optional[Client]: The client object if found, otherwise None.\n\n        Examples:\n            import py3xui\n\n            api = py3xui.Api.from_env()\n            client: py3xui.Client = api.client.get_by_email("email@example.com")\n        """
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
        """\n        Retrieve the IP records associated with a specific client identified by their email.\n\n        Args:\n            email (str): The email of the client to retrieve.\n\n        Returns:\n            Optional[str]: The client IPs if found, otherwise None.\n\n        Examples:\n            import py3xui\n\n            api = py3xui.Api.from_env()\n            ips = api.client.get_ips("email@example.com")\n        """
        endpoint = f"panel/api/inbounds/clientIps/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        logger.info("Getting client IPs for email: %s", email)

        response = self._post(url, headers, {})

        ips_json = response.json().get(ApiFields.OBJ)
        return ips_json if ips_json != ApiFields.NO_IP_RECORD else None

    def add(self, inbound_id: int, clients: List[Client]) -> None:
        """\n        Add clients to a specific inbound configuration.\n\n        Args:\n            inbound_id (int): The ID of the inbound configuration.\n            clients (List[Client]): A list of client objects to add.\n        """
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
        """\n        Update a specific client's information.\n\n        Args:\n            client_uuid (str): The UUID of the client to update.\n            client (Client): The updated client object.\n        """
        endpoint = f"panel/api/inbounds/updateClient/{client_uuid}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        settings = {"clients": [client.model_dump(by_alias=True, exclude_defaults=True)]}
        data = {"id": client.inbound_id, "settings": json.dumps(settings)}

        logger.info("Updating client: %s", client)
        self._post(url, headers, data)
        logger.info("Client updated successfully.")

    def reset_ips(self, email: str) -> None:
        """\n        Reset the IP records for a specific client.\n\n        Args:\n            email (str): The email of the client to reset.\n        """
        endpoint = f"panel/api/inbounds/clearClientIps/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Resetting client IPs for email: %s", email)

        self._post(url, headers, data)
        logger.info("Client IPs reset successfully.")

    def reset_stats(self, inbound_id: int, email: str) -> None:
        """\n        Reset the traffic statistics for a specific client.\n\n        Args:\n            inbound_id (int): The ID of the inbound configuration.\n            email (str): The email of the client to reset.\n        """
        endpoint = f"panel/api/inbounds/{inbound_id}/resetClientTraffic/{email}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Resetting client stats for inbound ID: %s, email: %s", inbound_id, email)

        self._post(url, headers, data)
        logger.info("Client stats reset successfully.")

    def delete(self, inbound_id: int, client_uuid: str) -> None:
        """\n        Delete a specific client from an inbound configuration.\n\n        Args:\n            inbound_id (int): The ID of the inbound configuration.\n            client_uuid (str): The UUID of the client to delete.\n        """
        endpoint = f"panel/api/inbounds/{inbound_id}/delClient/{client_uuid}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Deleting client with ID: %s", client_uuid)

        self._post(url, headers, data)
        logger.info("Client deleted successfully.")

    def delete_depleted(self, inbound_id: int) -> None:
        """\n        Delete all depleted clients from an inbound configuration.\n\n        Args:\n            inbound_id (int): The ID of the inbound configuration.\n        """
        endpoint = f"panel/api/inbounds/delDepletedClients/{inbound_id}"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Deleting depleted clients for inbound ID: %s", inbound_id)

        self._post(url, headers, data)
        logger.info("Depleted clients deleted successfully.")

    def online(self) -> List[str]:
        """\n        Retrieve a list of currently online clients.\n\n        Returns:\n            List[str]: A list of UUIDs of online clients.\n        """
        endpoint = "panel/api/inbounds/onlines"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        logger.info("Getting online clients")

        response = self._post(url, headers, data)
        online = response.json().get(ApiFields.OBJ)
        return online or []