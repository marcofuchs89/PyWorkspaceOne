"""
WorkspaceOneAPIError Module
--
Handles error messages returned by the API as a json response
and filters the response to return a human readable error code and message.
"""

class WorkspaceOneAPIError(Exception):
    """WorkspaceONEAPIError

    Args:
        Exception (json): Exception message in json formatting
                            returned by an API Call

    Returns:
        An easy to read error message in the format "Error #{error_code}: {message}"
    """
    def __init__(self, json_response=None):
        if json_response is None:
            pass
        else:
            self.response = json_response
            self.error_code = json_response.get('errorCode')
            self.error_msg = str(json_response.get('message'))
            if self.error_code is None:
                self.error_code = 0
                self.error_msg = 'Unknown API error occurred'

    def __str__(self):
        return 'Error #{}: {}'.format(self.error_code, self.error_msg)
