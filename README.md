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

To update model version, at first create a new branch with name `aa.bb`, `aa.bb` meaning
the new version of the model. Mark that branch a default inside github.
The initial version is `2.0`, so a version with a minor
change should be `2.1`, version with a major change is `3.0`.

Then introduce your changes to files within the `model` directory and change
the contents of `version` file to `aa.bb.0`. Finally run `build.sh` to make
sure everything builds, push to github and run a new github release.