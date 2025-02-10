from time import sleep
from typing import Any, Callable

import requests

from py3xui.utils import Logger

logger = Logger(__name__)


# pylint: disable=too-few-public-methods
class ApiFields:
    """Stores the fields returned by the XUI API for parsing.

    Attributes:
        SUCCESS (str): Key for the success status in API responses.
        MSG (str): Key for the message in API responses.
        OBJ (str): Key for the object data in API responses.
        CLIENT_STATS (str): Key for client statistics in API responses.
        NO_IP_RECORD (str): Message indicating no IP record found.
    """

    SUCCESS = "success"
    MSG = "msg"
    OBJ = "obj"
    CLIENT_STATS = "clientStats"
    NO_IP_RECORD = "No IP Record"


class BaseApi:
    """Provides a base class for interacting with the XUI API.

    This class handles the basic setup and authentication for API interactions.

    Args:
        host (str): The XUI host URL.
        username (str): The XUI username.
        password (str): The XUI password.

    Attributes:
        host (str): The XUI host URL.
        username (str): The XUI username.
        password (str): The XUI password.
        max_retries (int): The maximum number of retries for API requests.
        session (str | None): The session cookie for authenticated requests.

    Public Methods:
        login: Logs into the XUI API and sets the session cookie.

    Private Methods:
        _check_response: Checks the API response for success status.
        _url: Constructs the full URL for an API endpoint.
        _request_with_retry: Sends a request to the API with retry logic.
        _post: Sends a POST request to the API.
        _get: Sends a GET request to the API.
    """

    def __init__(self, host: str, username: str, password: str):
        """Initializes the BaseApi with the provided credentials.

        Args:
            host (str): The XUI host URL.
            username (str): The XUI username.
            password (str): The XUI password.
        """
        self._host = host.rstrip("/")
        self._username = username
        self._password = password
        self._max_retries: int = 3
        self._session: str | None = None

    @property
    def host(self) -> str:
        """The XUI host URL."""
        return self._host

    @property
    def username(self) -> str:
        """The XUI username."""
        return self._username

    @property
    def password(self) -> str:
        """The XUI password."""
        return self._password

    @property
    def max_retries(self) -> int:
        """The maximum number of retries for API requests."""
        return self._max_retries

    @max_retries.setter
    def max_retries(self, value: int) -> None:
        """Set the maximum number of retries for API requests.

        Args:
            value (int): The new maximum number of retries.
        """
        self._max_retries = value

    @property
    def session(self) -> str | None:
        """The session cookie for authenticated requests."""
        return self._session

    @session.setter
    def session(self, value: str | None) -> None:
        """Set the session cookie for authenticated requests.

        Args:
            value (str | None): The new session cookie.
        """
        self._session = value

    def login(self) -> None:
        """Logs into the XUI API and sets the session cookie.

        Raises:
            ValueError: If no session cookie is found after login.
        """
        endpoint = "login"
        headers: dict[str, str] = {}

        url = self._url(endpoint)
        data = {"username": self.username, "password": self.password}
        logger.info("Logging in with username: %s", self.username)

        response = self._post(url, headers, data)
        cookie: str | None = response.cookies.get("session")
        if not cookie:
            raise ValueError("Login failed: No session cookie received from the server.")
        logger.info("Session cookie retrieved for username: %s", self.username)
        self.session = cookie

    def _check_response(self, response: requests.Response) -> None:
        """Checks the API response for success status.

        Args:
            response (requests.Response): The API response to check.

        Raises:
            ValueError: If the response status is not successful.
        """
        response_json = response.json()

        status = response_json.get(ApiFields.SUCCESS)
        message = response_json.get(ApiFields.MSG)
        if not status:
            raise ValueError(f"API request failed with message: {message}")

    def _url(self, endpoint: str) -> str:
        """Constructs the full URL for an API endpoint.

        Args:
            endpoint (str): The API endpoint.

        Returns:
            str: The full URL for the API endpoint.
        """
        return f"{self._host}/{endpoint}"

    def _request_with_retry(
        self,
        method: Callable[..., requests.Response],
        url: str,
        headers: dict[str, str],
        **kwargs: Any,
    ) -> requests.Response:
        """Sends a request to the API with retry logic.

        Args:
            method (Callable[..., requests.Response]): The HTTP method to use.
            url (str): The URL to send the request to.
            headers (dict[str, str]): The headers to include in the request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            requests.Response: The API response.

        Raises:
            requests.exceptions.ConnectionError: If a connection error occurs.
            requests.exceptions.Timeout: If a timeout occurs.
            requests.exceptions.RequestException: If any other request exception occurs.
            requests.exceptions.RetryError: If the maximum number of retries is exceeded.
        """
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
        """Sends a POST request to the API.

        Args:
            url (str): The URL to send the request to.
            headers (dict[str, str]): The headers to include in the request.
            data (dict[str, Any]): The data to send in the request body.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            requests.Response: The API response.
        """
        return self._request_with_retry(requests.post, url, headers, json=data, **kwargs)

    def _get(self, url: str, headers: dict[str, str], **kwargs) -> requests.Response:
        """Sends a GET request to the API.

        Args:
            url (str): The URL to send the request to.
            headers (dict[str, str]): The headers to include in the request.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            requests.Response: The API response.
        """
        return self._request_with_retry(requests.get, url, headers, **kwargs)