from time import sleep
from typing import Any, Callable

import requests

from py3xui.utils import Logger

logger = Logger(__name__)


# pylint: disable=too-few-public-methods
class ApiFields:
    """Stores the fields returned by the XUI API for parsing.\n\n    Attributes:\n        SUCCESS (str): Key for the success status in API responses.\n        MSG (str): Key for the message in API responses.\n        OBJ (str): Key for the object data in API responses.\n        CLIENT_STATS (str): Key for client statistics in API responses.\n        NO_IP_RECORD (str): Message indicating no IP record is found.\n    """

    SUCCESS = "success"
    MSG = "msg"
    OBJ = "obj"
    CLIENT_STATS = "clientStats"
    NO_IP_RECORD = "No IP Record"


class BaseApi:
    """Base class for all API interactions with the XUI API.\n\n    Args:\n        host (str): The XUI host URL.\n        username (str): The XUI username.\n        password (str): The XUI password.\n\n    Attributes:\n        host (str): The XUI host URL.\n        username (str): The XUI username.\n        password (str): The XUI password.\n        max_retries (int): Maximum number of retries for API requests.\n        session (str | None): Session cookie for authenticated requests.\n    """

    def __init__(self, host: str, username: str, password: str):
        self._host = host.rstrip("/")
        self._username = username
        self._password = password
        self._max_retries: int = 3
        self._session: str | None = None

    @property
    def host(self) -> str:
        """Get the XUI host URL."""
        return self._host

    @property
    def username(self) -> str:
        """Get the XUI username."""
        return self._username

    @property
    def password(self) -> str:
        """Get the XUI password."""
        return self._password

    @property
    def max_retries(self) -> int:
        """Get the maximum number of retries for API requests."""
        return self._max_retries

    @max_retries.setter
    def max_retries(self, value: int) -> None:
        """Set the maximum number of retries for API requests."""
        self._max_retries = value

    @property
    def session(self) -> str | None:
        """Get the session cookie for authenticated requests."""
        return self._session

    @session.setter
    def session(self, value: str | None) -> None:
        """Set the session cookie for authenticated requests."""
        self._session = value

    def login(self) -> None:
        """Logs into the XUI API and sets the session cookie.\n\n        Raises:\n            ValueError: If no session cookie is found after a successful login attempt.\n        """
        endpoint = "login"
        headers: dict[str, str] = {}

        url = self._url(endpoint)
        data = {"username": self.username, "password": self.password}
        logger.info("Logging in with username: %s", self.username)

        response = self._post(url, headers, data)
        cookie: str | None = response.cookies.get("session")
        if not cookie:
            raise ValueError("No session cookie found, something wrong with the login...")
        logger.info("Session cookie successfully retrieved for username: %s", self.username)
        self.session = cookie

    def _check_response(self, response: requests.Response) -> None:
        """Checks the response from the API for errors.\n\n        Args:\n            response (requests.Response): The response object from the API request.\n\n        Raises:\n            ValueError: If the response status is not successful.\n        """
        response_json = response.json()

        status = response_json.get(ApiFields.SUCCESS)
        message = response_json.get(ApiFields.MSG)
        if not status:
            raise ValueError(f"Response status is not successful, message: {message}")

    def _url(self, endpoint: str) -> str:
        """Constructs the full URL for an API request.\n\n        Args:\n            endpoint (str): The API endpoint.\n\n        Returns:\n            str: The full URL for the API request.\n        """
        return f"{self._host}/{endpoint}"

    def _request_with_retry(
        self,
        method: Callable[..., requests.Response],
        url: str,
        headers: dict[str, str],
        **kwargs: Any,
    ) -> requests.Response:
        """Sends an API request with retries in case of failures.\n\n        Args:\n            method (Callable[..., requests.Response]): The HTTP method to use.\n            url (str): The URL to send the request to.\n            headers (dict[str, str]): The headers to include in the request.\n            **kwargs (Any): Additional keyword arguments to pass to the request method.\n\n        Returns:\n            requests.Response: The response object from the API request.\n\n        Raises:\n            requests.exceptions.RetryError: If the maximum number of retries is exceeded.\n        """
        logger.debug("%s request to %s...", method.__name__.upper(), url)
        for retry in range(1, self.max_retries + 1):
            try:
                skip_check = kwargs.pop("skip_check", False)
                response = method(url, cookies={"session": self.session}, headers=headers, **kwargs)
                response.raise_for_status()
                if skip_check:
                    return response
                self._check_response(response)
                return response
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                if retry == self.max_retries:
                    raise e
                logger.warning(
                    "Request to %s failed: %s, retry %s of %s", url, e, retry, self.max_retries
                )
                sleep(1 * (retry + 1))
            except requests.exceptions.RequestException as e:
                raise e
        raise requests.exceptions.RetryError(
            f"Max retries exceeded with no successful response to {url}"
        )

    def _post(
        self, url: str, headers: dict[str, str], data: dict[str, Any], **kwargs
    ) -> requests.Response:
        """Sends a POST request to the API.\n\n        Args:\n            url (str): The URL to send the request to.\n            headers (dict[str, str]): The headers to include in the request.\n            data (dict[str, Any]): The data to send in the request body.\n            **kwargs (Any): Additional keyword arguments to pass to the request method.\n\n        Returns:\n            requests.Response: The response object from the API request.\n        """
        return self._request_with_retry(requests.post, url, headers, json=data, **kwargs)

    def _get(self, url: str, headers: dict[str, str], **kwargs) -> requests.Response:
        """Sends a GET request to the API.\n\n        Args:\n            url (str): The URL to send the request to.\n            headers (dict[str, str]): The headers to include in the request.\n            **kwargs (Any): Additional keyword arguments to pass to the request method.\n\n        Returns:\n            requests.Response: The response object from the API request.\n        """
        return self._request_with_retry(requests.get, url, headers, **kwargs)