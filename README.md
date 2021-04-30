# Folder template

Python script to deploy and configure a folder to a target prefix, following a template.
The template specifies the file and folders structures, as well as basic substitutions.

## Installation

Clone the project.

    $ git clone git@github.com:Adnn/folder_template.git
    $ cd folder_template

Symlink the wrapper into a binary folder on your path.

Example on _macos_:

    $ ln -s $(pwd)/folder-template /usr/local/bin/

## Usage

See `./folder-template.py -h` for usage.

## Substitution

The substitution syntax is `{{identifier}}`,
it can appear in both file/folder names and file content.

Identifiers:

* `project`: all lowercase project name.
* `Project`: capitalized project name.
* `Project_description`
* `cmake_namespace`: the CMake namespace that will be assigned to created targets.
* `person`: a name to associate with the project.
* `year`: current year.
