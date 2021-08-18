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