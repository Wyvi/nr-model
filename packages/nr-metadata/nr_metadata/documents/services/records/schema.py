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
    NRContributorSchema,
    NRCreatorSchema,
)
from nr_metadata.common.services.records.schema_datatypes import (
    NRAccessRightsVocabularySchema,
    NRAffiliationVocabularySchema,
    NRCountryVocabularySchema,
    NREventSchema,
    NRExternalLocationSchema,
    NRFunderVocabularySchema,
    NRFundingReferenceSchema,
    NRGeoLocationPointSchema,
    NRGeoLocationSchema,
    NRItemRelationTypeVocabularySchema,
    NRLanguageVocabularySchema,
    NRLocationSchema,
    NROrganizationSchema,
    NRPersonSchema,
    NRRelatedItemContributorSchema,
    NRRelatedItemCreatorSchema,
    NRRelatedItemSchema,
    NRResourceTypeVocabularySchema,
    NRRightsVocabularySchema,
    NRSeriesSchema,
    NRSubjectCategoryVocabularySchema,
    NRSubjectSchema,
)
from nr_metadata.schema.identifiers import (
    NRObjectIdentifierSchema,
    NROrganizationIdentifierSchema,
    NRPersonIdentifierSchema,
    NRSystemIdentifierSchema,
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
        ma_fields.Nested(lambda: AdditionalTitlesItemSchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemSchema()))

    dateModified = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    externalLocation = ma_fields.Nested(lambda: NRExternalLocationSchema())

    publishers = ma_fields.List(ma_fields.String())

    thesis = ma_fields.Nested(lambda: NRThesisSchema())


class RelatedItemsItemSchema(NRRelatedItemSchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: ItemContributorsItemSchema())
    )


class ContributorsItemSchema(NRContributorSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: OrganizationalSchema())

    Personal = ma_fields.Nested(lambda: PersonalSchema())

    type_field = "nameType"


class CreatorsItemSchema(NRCreatorSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: OrganizationalSchema())

    Personal = ma_fields.Nested(lambda: PersonalSchema())

    type_field = "nameType"


class GeoLocationsItemSchema(NRGeoLocationSchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPoint = ma_fields.Nested(lambda: GeoLocationPointSchema())


class ItemContributorsItemSchema(NRRelatedItemContributorSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: OrganizationalSchema())

    Personal = ma_fields.Nested(lambda: PersonalSchema())

    type_field = "nameType"


class ItemCreatorsItemSchema(NRRelatedItemCreatorSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: OrganizationalSchema())

    Personal = ma_fields.Nested(lambda: PersonalSchema())

    type_field = "nameType"


class NRThesisSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateDefended = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    defended = ma_fields.Boolean()

    degreeGrantors = ma_fields.List(ma_fields.Nested(lambda: NRDegreeGrantorSchema()))

    studyFields = ma_fields.List(ma_fields.String())


class AccessRightsSchema(NRAccessRightsVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class AdditionalTitlesItemSchema(AdditionalTitlesSchema):
    class Meta:
        unknown = ma.RAISE


class AffiliationsItemSchema(NRAffiliationVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    ror = ma_fields.String()

    title = i18n_strings


class AuthorityIdentifiersItemSchema(NROrganizationIdentifierSchema):
    class Meta:
        unknown = ma.RAISE


class CountrySchema(NRCountryVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class EventLocationSchema(NRLocationSchema):
    class Meta:
        unknown = ma.RAISE


class EventsItemSchema(NREventSchema):
    class Meta:
        unknown = ma.RAISE


class FunderSchema(NRFunderVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class FundingReferencesItemSchema(NRFundingReferenceSchema):
    class Meta:
        unknown = ma.RAISE


class GeoLocationPointSchema(NRGeoLocationPointSchema):
    class Meta:
        unknown = ma.RAISE


class InstitutionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    title = i18n_strings


class ItemRelationTypeSchema(NRItemRelationTypeVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class ItemResourceTypeSchema(NRResourceTypeVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class LanguagesItemSchema(NRLanguageVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

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


class ObjectIdentifiersItemSchema(NRObjectIdentifierSchema):
    class Meta:
        unknown = ma.RAISE


class OrganizationalSchema(NROrganizationSchema):
    class Meta:
        unknown = ma.RAISE


class PersonalAuthorityIdentifiersItemSchema(NRPersonIdentifierSchema):
    class Meta:
        unknown = ma.RAISE


class PersonalSchema(NRPersonSchema):
    class Meta:
        unknown = ma.RAISE


class RightsSchema(NRRightsVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class SeriesItemSchema(NRSeriesSchema):
    class Meta:
        unknown = ma.RAISE


class SubjectCategoriesItemSchema(NRSubjectCategoryVocabularySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class SubjectsItemSchema(NRSubjectSchema):
    class Meta:
        unknown = ma.RAISE


class SystemIdentifiersItemSchema(NRSystemIdentifierSchema):
    class Meta:
        unknown = ma.RAISE
