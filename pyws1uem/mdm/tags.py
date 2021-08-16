from .mdm import MDM

class Tags(MDM):
    """
    Base MDM class

    Workspace ONE UEM REST APIs allows you to manage
    all the functionalities of Mobile Device Management (MDM).
    The functionalities that are included but not limited to are device commands,
    retrieval of compliance, profile, network, location, and event log details.
    """
    def __init__(self, client):
        self.client = client

# TODO: Implement the tagging resources ...