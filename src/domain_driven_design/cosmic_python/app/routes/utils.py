from flask import Blueprint


def create_blueprint_version(name: str, prefix: str, version: str) -> Blueprint:
    prefix = prefix.replace('_', '-')
    url_prefix = f"/api/{version}/{prefix}"
    return Blueprint(import_name=name, name=name, url_prefix=url_prefix)
