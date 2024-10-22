from typing import Annotated, Optional
from tools import vault, keycloak, openfga, application, ldap

import typer

myTools = ["keycloak", "ldap", "vault", "openfga", "application"]

app = typer.Typer()


def setup_tool(tool: str) -> None:
    if tool == "keycloak":
        keycloak.setup()
    elif tool == "ldap":
        ldap.setup()
    elif tool == "vault":
        vault.setup()
    elif tool == "openfga":
        openfga.setup()
    else:
        print(f"Cannot setup tool '{tool}'.")


def run_tool(tool: str) -> None:
    if tool == "keycloak":
        keycloak.run()
    elif tool == "ldap":
        ldap.run()
    elif tool == "vault":
        vault.run()
    elif tool == "openfga":
        openfga.run()
    elif tool == "application":
        application.run()
    else:
        print(f"Cannot run tool '{tool}'.")


def check_tool(tools: list[str]) -> list[str]:
    selected_tools = []
    for tool in tools:
        if tool.strip().lower() in myTools:
            selected_tools.append(tool.strip())
        else:
            print(f"Tool '{tool}' not found.")
    return selected_tools


@app.command(short_help="Setup the tools required by applicaton.")
def setup(tool_name: Annotated[Optional[str], typer.Argument(help="The tools to setup. Give comma seperated tools to setup multiple tools. Leave blank to setup all tools.")] = None):
    """
    Setup all the tools required by application.
    """
    if tool_name:
        selected_tools = check_tool(tool_name.split(","))
    else:
        selected_tools = myTools
    for tool in selected_tools:
        setup_tool(tool)


@app.command(short_help="Run the tools required by application.")
def run(tool_name: Annotated[Optional[str], typer.Argument(help="The tools to run. Give comma seperated tools to run multiple tools. Leave blank to run all tools.")]):
    """
    Run all the tools required by application. This will also start and run application backend as well if nothing is provided, or you provide it explicitly.
    """
    if tool_name:
        selected_tools = check_tool(tool_name.split(","))
    else:
        selected_tools = myTools
    for tool in selected_tools:
        run_tool(tool)


if __name__ == '__main__':
    app()
