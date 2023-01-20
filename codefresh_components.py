#!/usr/bin/env python3

import typing as t
from os import environ as env
from pathlib import Path
from pprint import pprint

import yaml

DEBUG = bool(env.get("DEBUG", False))


def create_pipeline_structure(
    pipelines: t.List[str], branch: str, revision: str
) -> t.List[t.Dict[str, str]]:
    """Fill in the data structure"""

    pipelines_to_run: t.List[t.Dict[str, str]] = []
    for pipeline in pipelines:
        pipeline_dict = dict(
            pipeline_id=pipeline, trigger_id=pipeline, branch=branch, sha=revision
        )
        pipelines_to_run.append(pipeline_dict)
    return pipelines_to_run


def render_yaml(
    pipelines: t.List[str], destination: Path, branch: str, revision: str
) -> None:
    """
    Control function to build up the data structure from parameters and then render it to a file.
    """
    pipeline_struct = create_pipeline_structure(pipelines, branch, revision)
    if DEBUG:
        print(f"Rendering the following to YAML at {destination}:")
        print(yaml.dump(pipeline_struct))
    with open(destination, "w") as dst_fh:
        yaml.dump(pipeline_struct, dst_fh)


def main():
    """Entrypoint and input validation"""

    pipelines = env["COMPONENT_PIPELINES"].split()
    destination = Path(env["DESTINATION"])
    branch = env["CF_BRANCH"]
    revision = env["CF_REVISION"]

    if DEBUG:
        print("Environment Variables:")
        pprint(dict(env))

    render_yaml(pipelines, destination, branch, revision)


if __name__ == "__main__":
    main()
