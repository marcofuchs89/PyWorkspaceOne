# PyWorkspaceOneUEM

=========

PyWorkspaceOneUEM is a Python API library for [VMware Workspace ONE UEM](https://www.vmware.com/content/vmware/vmware-published-sites/us/products/workspace-one.html.html) formerly known as [AirWatch](https://www.air-watch.com/)

## Credit

A huge credit goes to John Richrads [@jprichards](https://github.com/jprichards) and his project [PyVMwareAirWatch](https://github.com/jprichards/PyVMwareAirWatch) from which a majority of the codebase was adopted.

## Usage

example.py

```python
from pyws1uem.client import WorkspaceOneAPI

wso = WorkspaceOneAPI(env='your_environment_url',
                    apikey='your_api_token_key',
                    username='username',
                    password='password')


# Get the OG ID for a specified Group ID
wso.groups.get_id_from_groupid(groupid='testog')

# Create a Child OG for a specified Parent OG Group ID (Type/Name optional)
wso.groups.create_child_og(parent_groupid='testog', groupid='newog', og_type='Container', name='newog')

# Get a Device ID via an alternate device identifier
wso.devices.get_id_by_alt_id(serialnumber='C09Z1TC8FJWT')
```

## Supported Functionality

* Devices
  * Search devices with specific criteria
    * V1 Endpoint criteria > user, model, platform, lastseen, ownership, lgid(OrganizationGroup ID), compliantstatus, seensince
    * V2 Endpoint criteria > user, model, platform, lastseen, ownership, lgid, compliance_status, seen_since
    * V3 Endpoint criteria > user, model_identifier, device_type, last_seen, ownership, organization_group_uuid, compliance_status, seen_since
  * Return the full device details by an Extensive Device Search
  * Get Device Details by Alt ID (Macaddress, Udid, Serialnumber, ImeiNumber, EasId)
  * Get Device ID by Alt ID (Macaddress, Udid, Serialnumber, ImeiNumber, EasId)
  * Clear Device Passcode
  * Get Device Details by Device ID
  * Send Commands To devices via Device ID or by Alt ID
  * Get Device FileVualt Recover Key
  * Get Security Info Sample by Device ID or Alt ID
  * Get Bulk Security Info Sample
  * Switch device From Staging User to End User
  * Get Network info Sample by Device ID
  * Delete a Device by Device ID
  * Delete a Device Custom Attribute by Device ID or Alternate ID
  * Get a list of device enrollment tokens for a given Group ID
  * Create a device enrollment token in a given OG
* Tags
  * Add a Tag to a Device
  * Remove a Tag from a Device
  * Check if a tag is already applied
* Users
  * Search for users by Username, Firstname, Lastname, Email,
  OrganizationGroupID, or Role
  * Delete user
* Groups
  * Get OG ID from Group ID
  * Create Customer type OG (On-Prem only)
  * Create Child OG
  * Get UUID from OG ID

## Requirements

* [requests](http://docs.python-requests.org/en/latest/)

![Lines of code](https://shields.devops.telekom.de:/tokei/lines/github.com/marcofuchs89/PyWorkspaceOne)
