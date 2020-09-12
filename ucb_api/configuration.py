import urllib3

from .python_client.swagger_client.configuration import Configuration as BaseConfiguration


class Configuration(BaseConfiguration):
    def __init__(self, api_key):
        super().__init__()
        self.key = api_key
        self.host = 'https://build-api.cloud.unity3d.com/api/v1'

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return f'Basic {self.key}'
