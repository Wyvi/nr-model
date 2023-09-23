# NR model

This github project generates:

* `nr-metadata` - runtime support containing marshmallow, serializers, ... for NR metadata (documents and data)
* `oarepo-model-builder-nr` - a plugin for oarepo-model-builder to generate 

## Incompatible changes

None yet. If you introduce any incompatible changes (vs previous major version),
enumerate them here and link the readme file from the previous major version
for reference.

## Usage

See the `examples/model.yaml` file for a skeleton of a repository 
which uses nr metadata document model. An even easier way is to use the
[nrp](https://narodni-repozitar.github.io/developer-docs/docs/technology/invenio/nrp-toolchain/) 
command to generate a documents- or data- compatible repository. 
See the same pages to get help about the model contents.

## Branches

Branches are always named "aa.bb" and denote the version of the contained metadata schema.

## Updating package

Package needs to be updated whenever the version of oarepo-model-builder and 
other builder plugins changes and influences the generated files.

The package version is always in the form of `aa.bb.ccc`, where `aa.bb` is the version
of the metadata schema and `ccc` is the version of the python package.

To rebuild python packages, increase the version number in `version` file,
run `build.sh`, push to the branch and create a new github release.

## Updating model

To update the model version, start by creating a new branch with the name 
`aa.bb`, where `aa.bb` represents the new model version. 

For example, if the current version is `2.0` and your changes are minor, 
the new version should be `2.1`, while major changes warrant 
a version bump to `3.0`.

Set this branch as the default branch on GitHub. 

Next, make your modifications to the files within the model directory, 
and update the content of the `version` file to reflect the new version as 
`aa.bb.0`. Afterward, execute the `build.sh` script to ensure that everything 
builds correctly. 

Push your changes to GitHub, and mark the branch as the default branch.
Then create a new GitHub release.