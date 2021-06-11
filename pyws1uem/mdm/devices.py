from .mdm import MDM


class Devices(MDM):
    """
    A class to manage functionalities of Mobile Device Management (MDM).
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def search(self, **kwargs):
        """Returns the Device information matching the search parameters."""
        return MDM._get(self, path='/devices', params=kwargs)

    def searchv2(self, **kwargs):
        """Returns the Device information matching the search parameters with v2 endpoint."""
        _header = {'Accept': 'application/json;version=2'}
        return MDM._get(self, path='/devices/search', header=_header, params=kwargs)

    def searchv3(self, **kwargs):
        """Returns the Device information matching the search parameters with v3 endpoint."""
        _header = {'Accept': 'application/json;version=3'}
        return MDM._get(self, path='/devices/search', header=_header, params=kwargs)

    def search_all(self, **kwargs):
        """Returns the Devices matching the search parameters."""
        response = MDM._get(self, path='/devices/search', params=kwargs)
        return response

    def extensive_search(self, **kwargs):
        """Full device details search with many attributes included.

        PARAMS:
            organizationgroupid (int, optional): OrganizationGroup to be searched,
                user's OG is considered if not sent. Defaults to None.
            platform (str, optional): Device platform. Defaults to None.
            startdatetime (str, optional): Filters devices such that devices with
                last seen after this date will be returned. Defaults to None.
            enddatetime (str, optional): Filters devices such that devices with
                last seen till this date will be returned. Defaults to None.
            deviceid (int, optional): Device Identifier. Defaults to None.
            customattributeslist (str, optional): Custom attribute names.
                Defaults to None.
            enrollmentstatus (str, optional): Filters devices based on EnrollmentStatus
                [Enrolled, EnterpriseWipePending, DeviceWipePending, Unenrolled].
                Defaults to None.
            statuschangestarttime (str, optional): Filters the devices for which
                EnrollmentStatus has changes from enrollmentstatuschangefrom datetime.
                This filter is only for Enrolled and Unenrolled enrollment status.
                Defaults to None.
            statuschangeendtime (str, optional): Filters the devices for which
                EnrollmentStatus has changes till enrollmentstatuschangeto datetime.
                This filter is only for Enrolled and Unenrolled enrollment status.
                Defaults to None.
            page (int, optional): Specific page number to get. 0 based index.
                Defaults to 0.
            pagesize (int, optional): Maximumm records per page. Defaults to 500.
            macaddress (str, optional): MAC address. Defaults to None.

        Returns:
            dict: API paged of devices that meet the search requirements.
        """
        response = MDM._get(
            self, path='/devices/extensivesearch', params=kwargs)
        return response

    def get_details_by_alt_id(self, serialnumber=None, macaddress=None,
                              udid=None, imeinumber=None, easid=None):
        """Returns the Device information matching the search parameters."""
        if serialnumber:
            response = self.search(
                searchby='Serialnumber', id=str(serialnumber))
        elif macaddress:
            response = self.search(searchby='Macaddress', id=str(macaddress))
        elif udid:
            response = self.search(searchby='Udid', id=str(udid))
        elif imeinumber:
            response = self.search(searchby='ImeiNumber', id=str(imeinumber))
        elif easid:
            response = self.search(searchby='EasId', id=str(easid))
        else:
            return None
        return response

    def get_id_by_alt_id(self, serialnumber=None, macaddress=None, udid=None,
                         imeinumber=None, easid=None):
        response = self.get_details_by_alt_id(
            serialnumber, macaddress, udid, imeinumber, easid)
        return response['Id']['Value']

    def clear_device_passcode(self, device_id):
        """
        Clear the passcode on a device
        """
        return MDM._post(self,
                         path='/devices/{}/clearpasscode'.format(device_id))

    def send_commands_for_device_id(self, command, device_id):
        """
        Commands for devices selecting device based on id
        """
        path = '/devices/{}/commands'.format(device_id)
        command = 'command={}'.format(command)
        return MDM._post(self, path=path, params=command)

    def send_commands_by_id(self, command, searchby, id):
        """
        Commands for devices selecting device based on id
        """
        _path = '/devices/commands'
        _query = 'command={}&searchBy={}&id={}'.format(str(command),
                                                       str(searchby),
                                                       str(id))
        return MDM._post(self, path=_path, params=_query)

    def get_details_by_device_id(self, device_id):
        """
        device details by device id
        """
        return MDM._get(self, path='/devices/{}'.format(device_id))

    def get_device_filevault_recovery_key(self, device_uuid):
        """
        Gets a macOS device's FileVault Recovery Key
        """
        _path = '/devices/{}/security/recovery-key'.format(device_uuid)
        return MDM._get(self, path=_path)

    def get_security_info_by_id(self, device_id):
        """
        Processes the device ID to retrieve the security
        information sample related info
        """
        _path = '/devices/{}/security'.format(device_id)
        return MDM._get(self, path=_path)

    def get_security_info_by_alternate_id(self, searchby, id):
        """
        Processes the device ID to retrieve the security
        information sample related info by Alternate ID
        """
        _path = '/devices/security'
        _params = 'searchby={}&id={}'.format(searchby, id)
        return MDM._get(self, path=_path, params=_params)

    def get_bulk_security_info(self, organization_group_id, user_name,
                               params=None):
        """
        Processes the information like organization group ID, user name, model,
        platform, last seen, ownership, compliant status, seen since parameters
        and fetches the security information for the same.
        """
        _path = '/devices/securityinfosearch'
        _query = 'organizationgroupid={}&user={}'.format(organization_group_id,
                                                         user_name)
        return MDM._get(self, path=_path, params=_query)

    def switch_device_from_staging_to_user(self, device_id, user_id):
        """
        API for Single Staging switch to directory or basic user
        """
        _path = "/devices/{}/enrollmentuser/{}".format(device_id, user_id)
        return MDM._patch(self, path=_path)

    def get_managed_admin_account_by_uuid(self, device_id):
        """
        Get information of the administrator account configured on a macOS
        device via device enrollment program (DEP).
        """
        _path = "/devices/{}/security/managed-admin-information".format(
            device_id)
        return MDM._get(self, path=_path)

    def delete_device_by_id(self, device_id):
        """
        Delete a device from management.

        :param device_id: The device ID
        :return: API response
        """
        return MDM._delete(self, path='/devices/{}'.format(device_id))

    def delete_customattribute_by_id(self, device_id, customAttributes):
        """
        Delete a device customattribute.

        :param device_id: The device ID
               customAttributes: The attributes to remove separated by a comma
        :return: API response
        """
        _path = "/devices/{}/customattributes".format(device_id)
        _data = {"CustomAttributes": []}
        for item in customAttributes.split(","):
            _data["CustomAttributes"].append({"Name": item})
        return MDM._delete(self, path=_path, json=_data)

    def delete_customattribute_by_alt_id(self, serialnumber, customAttributes):
        """
        Delete a device customattribute by it's serial number.

        # NOTE: (clayton) This function doesn't seem to work from testing?

        :param device_id: The device ID
               customAttributes: The attributes to remove separated by a comma
        :return: API response
        """
        _path = "/devices/serialnumber/{}/customattributes".format(
            serialnumber)
        _data = {"CustomAttributes": []}
        for item in customAttributes.split(","):
            _data["CustomAttributes"].append({"Name": item})
        return MDM._delete(self, path=_path, json=_data)

    def search_enrollment_token(self, organization_group_uuid, **kwargs):
        """
        Returns a list of enrollment tokes that match the search criteria.

        :param organization_group_uuid: The Uuid of the Organization Group

        :return: API response
        """
        _path = "/groups/{}/enrollment-tokens".format(organization_group_uuid)
        response = MDM._get(self, path=_path, params=kwargs)
        return response

    def create_enrollment_token(self, organization_group_uuid, registration_record):
        """
        Creates a device enrollment token in the given organization unit with a given registration record (data)
        """
        _path = "/groups/{}/enrollment-tokens".format(organization_group_uuid)
        return MDM._post(self, path=_path, json=registration_record)
