"""
Module to access the WorkspaceONE UEM /mdm API Endpoint

This module sets basic parameters that are needed to
correctly connect to /mdm API Endpoints
"""

class MDM(object):
    """
    Base MDM class

    Workspace ONE UEM REST APIs allows you
    to manage all the functionalities of Mobile Device Management (MDM).
    The functionalities that are included but not limited to are device commands,
    retrieval of compliance, profile, network, location, and event log details.
    """

    def __init__(self, client):
        self.client = client

    def _get(self, module='mdm', path=None, version=None, params=None,
             header=None):
        """GET requests for base mdm endpoints"""
        return self.client.get(module=module, path=path,
                               version=version, params=params, header=header)

    def _post(self, module='mdm', path=None, version=None, params=None,
              data=None, json=None, header=None):
        """POST requests for base mdm endpoints"""
        return self.client.post(module=module, path=path, version=version,
                                params=params, data=data,
                                json=json, header=header)

    def _put(self, module='mdm', path=None, version=None, params=None,
             data=None, json=None, header=None):
        """PUT requests for base mdm endpoints"""
        return self.client.put(module=module, path=path, version=version,
                               params=params, data=data,
                               json=json, header=header)

    def _patch(self, module='mdm', path=None, version=None, params=None,
               data=None, json=None, header=None):
        """Patch requests for base mdm endpoints"""
        return self.client.patch(module=module, path=path, version=version,
                                 params=params, data=data,
                                 json=json, header=header)

    def _delete(self, module='MDM', path=None, version=None, params=None,
                data=None, json=None, header=None):
        return self.client.delete(module=module, path=path, version=version,
                                  params=params, data=data, json=json, header=header)
