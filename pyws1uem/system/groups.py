"""
Module to manage all core functionalities for WorkspaceONE UEM Organization Groups
"""

import json
from .system import System


class Groups(System):
    """
    Sub-Class to manage Groups, inherited from the base System class
    """
    jheader = {'Content-Type': 'application/json'}

    def __init__(self, client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Groups matching the search parameters
        """
        response = System._get(self, path='/groups/search', params=kwargs)
        return response

    def get_id_from_groupid(self, groupid):
        """
        Returns the OG ID for a given Group ID
        """
        response = self.search(groupid=str(groupid))
        return response['LocationGroups'][0]['Id']['Value']

    def get_groupid_from_id(self, groupid):
        """
        Returns the Group ID for a given ID
        """
        response = System._get(self, path='/groups/{}'.format(groupid))
        return response['GroupId']

    def get_uuid_from_groupid(self, groupid):
        """
        Returns the OG UUID for a given Group ID
        """
        response = System._get(self, path='/groups/{}'.format(groupid))
        return response['Uuid']

    def create(self, parent_id, ogdata):
        """
        Creates a Group and returns the new ID
        """
        response = System._post(self, path='/groups/{}'.format(parent_id),
                                data=ogdata, header=self.jheader)
        return response

    def create_customer_og(self, groupid, name=None):
        """
        Creates a Customer type OG, with a given Group ID and Name,
        and returns the new ID
        """
        new_og = {'GroupId': str(groupid),
                  'Name': str(name),
                  'LocationGroupType': 'Customer'}
        if name is None:
            new_og['Name'] = str(groupid)
        response = self.create(parent_id=7, ogdata=json.dumps(new_og))
        return response.get('Value')

    def create_child_og(self, parent_groupid, groupid, og_type=None, name=None):
        """
        Creates a Child OG for a given Parent Group ID, with a given Type,
        Group ID, and Name, and returns the new ID
        """
        pid = self.get_id_from_groupid(parent_groupid)
        new_og = {'GroupId': str(groupid),
                  'Name': str(name),
                  'LocationGroupType': str(og_type)}
        if name is None:
            new_og['Name'] = str(groupid)
        if og_type is None:
            new_og['LocationGroupType'] = 'Container'
        response = self.create(parent_id=pid, ogdata=json.dumps(new_og))
        return response.get('Value')
