# NR model

This github project generates:

* `nr-metadata` - runtime support containing marshmallow, serializers, ... for NR metadata (documents and data)
* `oarepo-model-builder-nr` - a plugin for oarepo-model-builder to generate 

## Usage

See the `examples/model.yaml` file for a skeleton of a repository 
which uses nr metadata document model. An even easier way is to use the
[nrp](https://narodni-repozitar.github.io/developer-docs/docs/technology/invenio/nrp-toolchain/) 
command to generate a documents-compatible repository. See the same pages to get help
about the model contents.

## Branches

Branches are always named "aa.bb" and denote the version of the contained metadata schema.

## Updating package version

The package version is always in the form of `aa.bb.ccc`, where `aa.bb` is the version
of the metadata schema and `ccc` is the version of the python package.

To rebuild python packages, increase the version number in `version` file,
run `build.sh`, push to the branch and create a new github release.

## Updating model version

To update model version, at first create a new branch with name `aa.bb`, `aa.bb` meaning
the new version of the model. The initial version is `2.0`, so a version with a minor
change should be `2.1`, version with a major change (but keep it always backward compatible!)
is `3.0`.

Then introduce your changes to files within the `model` directory and run build.sh