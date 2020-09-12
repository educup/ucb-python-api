from typing import List
from ..python_client.swagger_client.api_client import ApiClient
from ..python_client.swagger_client.api import BuildtargetsApi as BaseBuildtargetsApi
from ..models import InlineBuildTarget


class BuildtargetsApi(BaseBuildtargetsApi):
    def __init__(self, api_client=None):
        super().__init__(api_client=api_client)

    def get_build_targets(self, orgid, projectid, **kwargs):  # noqa: E501
        try:
            data = super().get_build_targets(orgid, projectid, **kwargs)
            result: List[InlineBuildTarget] = []
            for item in data:
                result.append(InlineBuildTarget.factory(item))
            return result
        except Exception as e:
            raise e
