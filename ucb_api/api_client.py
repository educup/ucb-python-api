from .python_client.swagger_client.api_client import ApiClient as BaseApiClient


class ApiClient(BaseApiClient):
    def update_params_for_auth(self, headers, querys, _):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        """
        auth_setting = self.configuration.auth_settings().get('apikey')
        if auth_setting:
            if not auth_setting['value']:
                raise Exception('Value auth settings not found')
            elif auth_setting['in'] == 'header':
                headers[auth_setting['key']] = auth_setting['value']
            elif auth_setting['in'] == 'query':
                querys.append((auth_setting['key'], auth_setting['value']))
            else:
                raise ValueError(
                    'Authentication token must be in `query` or `header`'
                )
