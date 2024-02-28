import marshmallow as ma
from edtf import Date as EDTFDate
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow_utils.fields import TrimmedString
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_date,
)
from oarepo_vocabularies.services.schema import HierarchySchema

from nr_metadata.common.services.records.schema_common import (
    AdditionalTitlesSchema,
    NRCommonMetadataSchema,
)
from nr_metadata.common.services.records.schema_datatypes import (
    NRExternalLocationSchema,
)


class NRDocumentRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDocumentMetadataSchema())

    syntheticFields = ma_fields.Nested(lambda: NRDocumentSyntheticFieldsSchema())


class NRDocumentMetadataSchema(NRCommonMetadataSchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )

    dateModified = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    externalLocation = ma_fields.Nested(lambda: NRExternalLocationSchema())

    publishers = ma_fields.List(ma_fields.String())

    thesis = ma_fields.Nested(lambda: NRThesisSchema())


class NRThesisSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateDefended = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    defended = ma_fields.Boolean()

    degreeGrantors = ma_fields.List(ma_fields.Nested(lambda: NRDegreeGrantorSchema()))

    studyFields = ma_fields.List(ma_fields.String())


class InstitutionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    title = i18n_strings


class NRDegreeGrantorSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    title = i18n_strings


class NRDocumentSyntheticFieldsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE
