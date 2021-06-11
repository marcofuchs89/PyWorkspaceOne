from .system import System


class Users(System):

    def __init__(self, client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Enrollment User's details matching the search parameters

        /api/system/users/search?{params}

        PARAMS:
            username={username}
            firstname={firstname}
            lastname={lastname}
            email={email}
            organizationgroupid={locationgroupid}
            role={role}
        """
        return System._get(self, path='/users/search', params=kwargs)

    def get_user_by_uuid(self, uuid):
        """
        Returns the enrollment user for a specific uuid using the v2 endpoint.

        PARAMS:
            uuid (str): AirWatch UUID to return
        """
        _path = "/users/{}".format(uuid)
        _header = {'Accept': 'application/json;version=2'}
        return System._get(self, header=_header, path=_path)

    def create_user(self, **kwargs):
        """
        Create an enrollment user using the v2 endpoint.

        /api/system/users/

        PARAMS:
            externalId={e559e7df-4ba0-4891-9fcd-8574c1770d34}
            userName={username}
            password={password}
            firstName={firstname}
            lastName={lastname}
            displayName={displayname}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.come}
            phoneNumber={1-111-111-1111}
            mobileNumber={+1(111)-111-1111}
            messageType={Email}
            messageTemplateUuid={53f732a0-3e08-474d-80f4-ff976b8eb698}
            enrollmentRoleUuid={599b9117-f399-4e60-a96b-cd1f771d5f06}
            status=true,
            securityType={directory}     REQUIRED
            deviceStagingEnabled=false,
            deviceStagingType={StagingDisabled}
            organizationGroupUuid={6fbc95c6-3269-4a88-804d-c8db7f479d7f}
            enrollmentOrganizationGroupUuid={94b1b965-59b9-462c-ad18-4a228f9830dd}
            customAttribute1={CustomAttribute1}
            customAttribute2={CustomAttribute2}
            customAttribute3={CustomAttribute3}
            customAttribute4={CustomAttribute4}
            customAttribute5={CustomAttribute5}
            aadMappingAttribute={e559e7df-4ba0-4891-9fcd-8574c1770d34}
            department={Sales}
            employeeIdentifier={12345}
            costCenter={110)
        """
        _header = {'Accept': 'application/json;version=2'}
        return System._post(self, header=_header, path="/users/", json=kwargs)

    def update_user_by_uuid(self, uuid: str=None, **kwargs):
        """
        Update the enrollment user with attributes using the v2 endpoint.

        /api/system/users/{uuid}

        PARAMS:
            password={Password1}
            firstName={Firstname}
            lastName={Lastname}
            displayName={displayName}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.com}
            phoneNumber={5551234567}
            mobileNumber={5551234567}
            messageType={Email}
            messageTemplateUuid={2aca918b-3468-4539-8750-41a7074b120d}
            deviceStagingEnabled": false,
            deviceStagingType={StagingDisabled}
            enrollmentRoleUuid={0aa0256e-89c6-450e-854c-aa97233b61b6}
            enrollmentOrganizationGroupUuid={db1d3802-6885-4035-99ab-e39239b5a0f2}
            CustomAttribute1={CustomAttribute1}
            CustomAttribute2={CustomAttribute2}
            CustomAttribute3={CustomAttribute3}
            CustomAttribute4={CustomAttribute4}
            CustomAttribute5={CustomAttribute5}
        """
        _path = "/users/{}".format(uuid)
        _header = {'Accept': 'application/json;version=2'}
        return System._put(self, path=_path, header=_header, json=kwargs)

    def delete_user_by_uuid(self, uuid):
        """
        Delete the enrollment user by enrollment user uuid with the v2 endpoint.

        :param uuid:
        :return: API response
        """
        _path = '/users/{}'.format(uuid)
        _header = {'Accept': 'application/json;version=2'}
        return System._delete(self, header=_header, path=_path)

    def delete_user_by_id(self, user_id):
        """
        Delete the enrollment user by enrollment user id

        :param user_id:
        :return: API response
        """
        path = '/users/{}/delete'.format(user_id)
        return System._delete(self, path=path)

    def create_device_registration_to_user(self, user_id, register_device_details):
        path = '/users/{}/registerdevice'.format(user_id)
        response = System._post(path=path, data=register_device_details)
        return response