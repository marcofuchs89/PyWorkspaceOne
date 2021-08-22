class System(object):
    """
    Base System class

    Workspace ONE UEM REST APIs allows you to manage all the core functionalities around console administration where you can:
    - Create and assign administrator accounts so admins can easily manage users and devices.
    - Create, manage, and view device enrollment user's.
    Identify users and establish permissions using organization groups.
    - Group sets of users into user groups which act as filters (in addition to organization groups) for assigning profiles and applications.
    - Extract particular values from the devices and return it to Workspace ONE UEM. These attributes can then be associated with other rules to further assign to the devices.
    """
    def __init__(self, client):
        self.client = client

    def _get(self, module='system', path=None,
             version=None, params=None, header=None):
        """
        GET requests for base system endpoints
        """
        return self.client.get(module=module, path=path,
                               version=version, params=params, header=header)

    def _post(self, module='system', path=None,
              version=None, params=None, data=None, json=None, header=None):
        """POST requests"""
        return self.client.post(module=module, path=path, version=version,
                                params=params, data=data,
                                json=json, header=header)

    def _post_no_error_check(self, module='system', path=None,
                             version=None, params=None, data=None,
                             json=None, header=None):
        """POST requests with no error check when none json is returned"""
        return self.client.post_no_error_check(module=module, path=path,
                                               version=version, params=params,
                                               data=data,
                                               json=json, header=header)

    def _put(self, module='system', path=None,
             version=None, params=None, data=None, json=None, header=None):
        """PUT requests"""
        return self.client.put(module=module, path=path, version=version,
                               params=params, data=data,
                               json=json, header=header)

    def _delete(self, module="system", path=None,
                version=None, params=None, header=None):
        """Delete requests"""
        return self.client.delete(
            module=module, path=path, version=version, params=params, header=header
        )
