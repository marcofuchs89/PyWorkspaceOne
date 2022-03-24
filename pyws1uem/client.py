"""WorkspaceOneAPI Client Module

The module handles all basic methods to interact with the API.
Basic HTTP Method calls are defined here (GET, POST, PUT, PATCH, DELETE)
and static methods for error checking, building the client object and constructing header values.

In Case of errors in the response the requests will raise an exception
using the WorkspaceOneAPIError Class.
"""

from __future__ import print_function, absolute_import
import logging
import requests
import time
from email.utils import formatdate
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

    def __init__(self, env: str, auth_url: str, client_id: str, client_secret: str, aw_tenant_code: str):
        """
        Initialize an AirWatchAPI Client Object.

        :param  env: Base URL of the AirWatch API Service
                client_id: Client ID
                client_secret: Client Secret
                aw_tenant_code: aw-tenant-code
        """
        self.env = env
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.aw_tenant_code = aw_tenant_code
        self.access_token = None
        self.token_acquire_time = 0
        self.token_expiry_seconds = 3600
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
            self._build_header(header)
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
            self._build_header(header)
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
            self._build_header(header)
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
            self._build_header(header)
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
            self._build_header(header)
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

    def _verify_auth_url(self):
        if not self.auth_url.startswith("https://"):
            self.auth_url = "https://" + self.auth_url
        if self.auth_url.endswith("/"):
            self.auth_url = self.auth_url[:-1]
        if not self.auth_url.endswith("connect/token"):
            # TODO raise API exception
            pass

    def _generate_access_token(self, header=None):
        if not header:
            header = {}
        self._verify_auth_url()
        header.update({"Content-Type": "application/x-www-form-urlencoded"})
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        try:
            api_response = requests.post(
                self.auth_url,
                data=data,
                headers=header,
            )
            api_response_code = self._check_for_error(api_response)
            if api_response_code == 200:
                self.access_token = api_response.json()["access_token"]
                self.token_acquire_time = time.perf_counter()
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def _build_header(self, header=None):
        """
        Build the header with OAuth. Built in monitoring of the
        access token expiry. It will only get a new token after
        the current one expires.
        """
        if not header:
            header = {}
        if not self.access_token or time.perf_counter() - self.token_acquire_time > self.token_expiry_seconds:
            self._generate_access_token(header)
        if header.get("Content-Type"):
            del header["Content-Type"]
        header.update({"Authorization": f"Bearer {self.access_token}"})
        header.update({"aw-tenant-code": self.aw_tenant_code})
        header.update({'Date': formatdate(timeval=None, localtime=False, usegmt=True)})
        if not header.get("Accept"):
            header.update({"Accept": "application/json"})
        return header
