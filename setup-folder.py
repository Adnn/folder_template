#!/usr/bin/env python3
import argparse
from os import mkdir, path, walk
from pathlib import Path


def substitute(template, context):
    """ Short and pessimised, as Guido intended """
    for key, value in context.items():
        template = template.replace("{{"+key+"}}", value)
    return template


def get_destination(template_dir, template_root, destination_root):
    """ Returns the destination folder to deploy the content of current_source """
    return str(Path(destination_root, *Path(template_dir).parts[len(Path(template_root).parts):]))


def deploy(template_root, destination_root, context):
    """ Recursively create file and folders while calling substitute on names and content """
    for current, _, filenames in walk(template_root):
        destination_dir = substitute(get_destination(current, template_root, destination_root),
                                     context)
        mkdir(destination_dir)
        for f in filenames:
            if f != ".DS_Store":
                with open(path.join(current, f)) as source:
                    with open(path.join(destination_dir, substitute(f, context)), "a") as destination:
                        destination.write(substitute(source.read(), context))


def main():
    """ Main """
    parser = argparse.ArgumentParser(description="Setup a development repository")
    parser.add_argument("deploy_prefix", metavar="deploy-prefix",
                        help="Folder where the repository folder will be created")
    parser.add_argument("project", help="Name of the project")
    parser.add_argument("description", help="One sentence description of the project")
    parser.add_argument("--template", default="agcpplib", help="The folder template to deploy")
    args = parser.parse_args()

    # Good: raises exception if folder already exists
    project = args.project.lower()
    repopath = path.join(args.deploy_prefix, project)

    ctx = {
        "project": project,
        "Project": project.capitalize(),
        "Project_description": args.description,
    }
    deploy(args.template, repopath, ctx)


if __name__ == "__main__":
    main()
