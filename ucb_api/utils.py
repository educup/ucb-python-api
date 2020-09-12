import typer

from os import getenv, putenv, system
from pprint import pprint
from typing import List, Optional

from .api import BuildtargetsApi
from .api_client import ApiClient
from .configuration import Configuration
from .models import InlineBuildTarget
from .python_client.swagger_client.rest import ApiException


def check_var(api_key: str, org_id: str, project_id: str):
    if not api_key:
        raise Exception('Environment variable UCB_API_KEY not found')
    if not org_id:
        raise Exception('Environment variable UCB_ORG_ID not found')
    if not project_id:
        raise Exception('Environment variable UCB_PROJECT_ID not found')


def get_buildtargets(platform: str, name: str) -> List[InlineBuildTarget]:
    api_key = getenv('UCB_API_KEY')
    org_id = getenv('UCB_ORG_ID')
    project_id = getenv('UCB_PROJECT_ID')
    check_var(api_key, org_id, project_id)

    configuration = Configuration(api_key)

    api_instance: BuildtargetsApi = BuildtargetsApi(ApiClient(configuration))

    try:
        response = api_instance.get_build_targets(org_id, project_id)
        result = []
        for item in response:
            if (platform == 'all' or item.platform == platform) and name.lower() in item.name.lower():
                result.append(item)
        return result
    except ApiException as e:
        print("Exception: %s\n" % e)


def set_envvar_buildtarget(buildtargetslist: List[InlineBuildTarget], vars: dict, replace: bool):
    api_key = getenv('UCB_API_KEY')
    org_id = getenv('UCB_ORG_ID')
    project_id = getenv('UCB_PROJECT_ID')
    check_var(api_key, org_id, project_id)

    configuration = Configuration(api_key)

    api_instance: BuildtargetsApi = BuildtargetsApi(ApiClient(configuration))

    try:
        for item in buildtargetslist:
            envvar = {}
            if not replace:
                response = api_instance.get_env_variables_for_build_target(org_id, project_id, item.buildtargetid)
                envvar.update(response)
            envvar.update(vars)
            response = api_instance.set_env_variables_for_build_target(org_id, project_id, item.buildtargetid, envvar)
            typer.echo(f'{item.buildtargetid}: {response}')
    except ApiException as e:
        print("Exception: %s\n" % e)
