import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import (
    InvenioUISchema,
    LocalizedDate,
    LocalizedEDTF,
)
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

from nr_metadata.common.services.records.ui_schema_common import (
    AdditionalTitlesUISchema,
    NRCommonMetadataUISchema,
)
from nr_metadata.common.services.records.ui_schema_datatypes import (
    NRExternalLocationUISchema,
)


class NRDocumentRecordUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDocumentMetadataUISchema())

    syntheticFields = ma_fields.Nested(lambda: NRDocumentSyntheticFieldsUISchema())


class NRDocumentMetadataUISchema(NRCommonMetadataUISchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesUISchema())
    )

    dateModified = LocalizedEDTF()

    externalLocation = ma_fields.Nested(lambda: NRExternalLocationUISchema())

    publishers = ma_fields.List(ma_fields.String())

    thesis = ma_fields.Nested(lambda: NRThesisUISchema())


class NRDocumentSyntheticFieldsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = LocalizedDate()

    institutions = ma_fields.Nested(lambda: InstitutionsUISchema())

    keywords = ma_fields.String()

    people = ma_fields.String()


class NRThesisUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateDefended = LocalizedDate()

    defended = ma_fields.Boolean()

    degreeGrantors = ma_fields.List(ma_fields.Nested(lambda: NRDegreeGrantorUISchema()))

    studyFields = ma_fields.List(ma_fields.String())


class InstitutionsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()


class NRDegreeGrantorUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()
