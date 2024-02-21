import marshmallow as ma
from edtf import Interval as EDTFInterval
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


class NRDataRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDataMetadataSchema())


class NRDataMetadataSchema(NRCommonMetadataSchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesItemSchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemSchema()))

    dateCollected = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    dateCreated = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    dateValidTo = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    dateWithdrawn = ma_fields.Nested(lambda: DateWithdrawnSchema())

    publishers = ma_fields.List(
        ma_fields.Nested(lambda: PublishersItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


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


class DateWithdrawnSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateInformation = ma_fields.String()

    type = ma_fields.String(validate=[validate_date("%Y-%m-%d")])


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


class PublishersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    ror = ma_fields.String()

    title = i18n_strings


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
