import typer

from json import load
from os import getenv, putenv, system
from pprint import pprint
from typing import Optional

from .api import BuildtargetsApi
from .api_client import ApiClient
from .configuration import Configuration
from .python_client.swagger_client.rest import ApiException
from .utils import get_buildtargets, set_envvar_buildtarget


app = typer.Typer()

buildtargets_app = typer.Typer()

app.add_typer(buildtargets_app, name='buildtargets')


@app.callback()
def callback():
    """
    Python package for Unity Cloud Build api
    """


@buildtargets_app.command()
def set_var_json(json_dir: str, platform: Optional[str] = typer.Option('all', help='android, ios or all'), replace: bool = typer.Option(False, '--replace'), app_name: Optional[str] = typer.Option('', '--name')):
    with open(json_dir) as file:
        json = load(file)
        buildtargetslist = get_buildtargets(platform, app_name)
        set_envvar_buildtarget(buildtargetslist, json, replace)


@buildtargets_app.command()
def set_var(name: str, value: str, platform: Optional[str] = typer.Option('all', help='android, ios or all'), replace: bool = typer.Option(False, '--replace'), app_name: Optional[str] = typer.Option('', '--name')):
    buildtargetslist = get_buildtargets(platform, app_name)
    set_envvar_buildtarget(buildtargetslist, {name: value}, replace)


@buildtargets_app.command()
def get_list(platform: Optional[str] = typer.Option('all', help='android, ios or all'), name: Optional[str] = typer.Option('')):
    result = get_buildtargets(platform, name)
    typer.echo([item.buildtargetid for item in result])


@app.command()
def show_env_vars():
    typer.echo(f'UCB_API_KEY: {getenv("UCB_API_KEY")}')
    typer.echo(f'UCB_ORG_ID: {getenv("UCB_ORG_ID")}')
    typer.echo(f'UCB_PROJECT_ID: {getenv("UCB_PROJECT_ID")}')
