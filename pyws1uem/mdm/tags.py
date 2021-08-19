from .mdm import MDM


class Tags(MDM):
    """
    Base Tags Class

    Contains REST-API Calls to add Devices to specific tags to trigger dependent actions,
    such as installing profiles, apps or trigger compliance actions.
    """

    def __init__(self, client):
        MDM.__init__(self, client)

# TODO: Implement the tagging resources ...

    def add_device_tag(self, tag_id, device_id):
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

    def remove_device_tag(self, tag_id, device_id):
        """[summary]

        Args:
            kwargs ([type]): [description]
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
