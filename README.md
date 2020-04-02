# Folder template

Python script to deploy and configure a folder to a target prefix, following a template.
The template specifies the file and folders structures, as well as basic substitutions.

## Substitution

The substitution syntax is `{{identifier}}`,
it can appear in both file/folder names and file content.

Identifiers:

* project: all lowercase project name
* Project: capitalized project name
* Project_description
