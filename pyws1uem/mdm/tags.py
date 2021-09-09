"""
Module to manage device tags (add and remove)
"""

from .mdm import MDM


class Tags(MDM):
    """
    Base Tags Class

    Contains REST-API Calls to add Devices to specific tags to trigger dependent actions,
    such as installing profiles, apps or trigger compliance actions.
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def add_device_tag(self, tag_id: str, device_id: str):
        """Add a tag to a given device

        Args:
            tag_id (string): The ID of the Tag in WorkspaceOneUEM
            device_id (string): The ID of the Device in WorkspaceOneUEM

        Returns:
            json: Status of the executed command (Accepted/Failed)
        """
        path = f'/tags/{tag_id}/adddevices'
        device_to_add = {
            "BulkValues": {
                "Value": [
                    device_id
                ]
            }
        }
        response = MDM._post(self, path=path, json=device_to_add)
        return response

    def remove_device_tag(self, tag_id: str, device_id: str):
        """Remove a tag from a given device

        Args:
            tag_id (string): The ID of the Tag in WorkspaceOneUEM
            device_id (string): The ID of the Device in WorkspaceOneUEM

        Returns:
            json: Status of the executed command (Accepted/Failed)
        """
        path = f'/tags/{tag_id}/removedevices'
        device_to_add = {
            "BulkValues": {
                "Value": [
                    device_id
                ]
            }
        }
        response = MDM._post(self, path=path, json=device_to_add)
        return response

    def check_device_tag(self, tag_id: str, device_id: str = None, device_uuid: str = None) -> bool:
        """Get a list of devices for the given tags and check
        if a specific device, defined by it's UUID, has the tag already assigned

        Args:
            tag_id (str): The ID of the Tag in WorkspaceOneUEM
            device_id (str, optional): The DeviceID of the Device in WorkspaceOneUEM.
                                        Defaults to None.
            device_uuid (str, optional): The UUID of the Device in WorkspaceOneUEM.
                                        Defaults to None.

        Returns:
            [bool]: True if the tag is assigned / False if not
        """
        path = f'tags/{tag_id}/devices'
        response = MDM._get(self, path=path)
        for device in response['Device']:
            if (str(device['DeviceId']) == str(device_id)
                    or str(device['DeviceUuid']) == str(device_uuid)):
                return True
        return False
