"""WorkspaceOneAPI Client Module

The module handles all basic methods to interact with the API.
Basic HTTP Method calls are defined here (GET, POST, PUT, PATCH, DELETE)
and static methods for error checking, building the client object and constructing header values.

In Case of errors in the response the requests will raise an exception
using the WorkspaceOneAPIError Class.
"""

from __future__ import print_function, absolute_import
import base64
import logging
import requests
from .error import WorkspaceOneAPIError
from .mdm.devices import Devices
from .system.groups import Groups
from .system.users import Users
from .system.info import Info
from .mdm.tags import Tags


# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with
# HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 0

# TODO: programing using library should be able to set logging level
# TODO: Implement logging to using config https://docs.python.org/3/howto/logging.html#configuring-logging
# TODO: sett logging correctly for a library https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class WorkspaceOneAPI(object):
    """
    Class for building a WorkspaceONE UEM API Object
    """

    def __init__(self, env: str, apikey: str, username: str, password: str):
        """
        Initialize an AirWatchAPI Client Object.

        :param  env: Base URL of the AirWatch API Service
                apikey: API Key to authorize
                username: Admin username
                password: corresponding pasword
        """
        self.env = env
        self.apikey = apikey
        self.username = username
        self.password = password
        self.groups = Groups(self)
        self.devices = Devices(self)
        self.users = Users(self)
        self.info = Info(self)
        self.tags = Tags(self)

    def get(self, module, path, version=None, params=None, header=None, timeout=30):
        """
        Sends a GET request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(
            self._build_header(self.username, self.password,
                               self.apikey, header)
        )
        header.update({"Content-Type": "application/json"})
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            api_response = requests.get(
                endpoint, params=params, headers=header, timeout=timeout)
            api_response = self._check_for_error(api_response)
            return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def post(
        self,
        module,
        path,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None,
        timeout=30,
    ):
        """
        Sends a POST request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(
            self._build_header(self.username, self.password,
                               self.apikey, header)
        )
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            api_response = requests.post(
                endpoint,
                params=params,
                data=data,
                json=json,
                headers=header,
                timeout=timeout,
            )
            api_response = self._check_for_error(api_response)
            return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def put(
        self,
        module,
        path,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None,
        timeout=30,
    ):
        """
        Sends a PUT request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(
            self._build_header(self.username, self.password,
                               self.apikey, header)
        )
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            api_response = requests.put(
                endpoint,
                params=params,
                data=data,
                json=json,
                headers=header,
                timeout=timeout,
            )
            api_response = self._check_for_error(api_response)
            return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def patch(
        self,
        module,
        path,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None,
        timeout=30,
    ):
        """
        Sends a Patch request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(
            self._build_header(self.username, self.password,
                               self.apikey, header)
        )
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            api_response = requests.patch(
                endpoint,
                params=params,
                data=data,
                json=json,
                headers=header,
                timeout=timeout,
            )
            api_response = self._check_for_error(api_response)
            return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    # NOQA

    def delete(
        self,
        module,
        path,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None,
        timeout=30,
    ):
        """
        Sends a DELETE request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(
            self._build_header(self.username, self.password,
                               self.apikey, header)
        )
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            api_response = requests.delete(
                endpoint,
                params=params,
                data=data,
                json=json,
                headers=header,
                timeout=timeout,
            )
            api_response = self._check_for_error(api_response)
            return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    @staticmethod
    def _check_for_error(response):
        """
        Checks the response for json data, then for an error, then for
        a status code
        """
        if response.headers.get("Content-Type") in (
            "application/json",
            "application/json; charset=utf-8",
        ):
            json = response.json()
            if json.get("errorCode"):
                raise WorkspaceOneAPIError(json_response=json)
            else:
                return json
        else:
            return response.status_code

    @staticmethod
    def _build_endpoint(base_url, module, path=None, version=None):
        """
        Builds the full url endpoint for the API request
        """
        if not base_url.startswith("https://"):
            base_url = "https://" + base_url
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        if version is None:
            url = "{}/api/{}".format(base_url, module)
        else:
            url = "{}/api/v{}/{}".format(base_url, version, module)
        if path:
            if path.startswith("/"):
                return url + "{}".format(path)
            else:
                return url + "/{}".format(path)
        return url

    @staticmethod
    def _build_header(username, password, token, header=None):
        """
        Build the header with base64 login, AW API token,
        and accept a json response
        """
        if not header:
            header = {}
        hashed_auth = base64.b64encode(
            (username + ":" + password).encode("utf8")
        ).decode("utf-8")
        header.update({"Authorization": "Basic {}".format(hashed_auth)})
        header.update({"aw-tenant-code": token})
        if not header.get("Accept"):
            header.update({"Accept": "application/json"})
        return header
