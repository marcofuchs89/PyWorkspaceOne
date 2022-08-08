"""
Module to get the general system information of the accessed WorkspaceONE UEM environment
"""

from .system import System

class Info(System):
    """
    Base Info Class, inherited from the System class
    """
    def __init__(self, client):
        System.__init__(self, client)

    def get_environment_info(self):
        """
        Get information like system-version from the UEM environment

        Returns:
            dict: System Information in JSON-format
        """
        return System._get(self, path="/info")
