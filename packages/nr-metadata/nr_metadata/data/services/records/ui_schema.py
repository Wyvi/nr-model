import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import (
    InvenioUISchema,
    LocalizedDate,
    LocalizedEDTFInterval,
)
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

from nr_metadata.common.services.records.ui_schema_common import (
    AdditionalTitlesUISchema,
    NRCommonMetadataUISchema,
    NRContributorUISchema,
    NRCreatorUISchema,
)
from nr_metadata.common.services.records.ui_schema_datatypes import (
    NRAccessRightsVocabularyUISchema,
    NRAffiliationVocabularyUISchema,
    NRCountryVocabularyUISchema,
    NREventUISchema,
    NRFunderVocabularyUISchema,
    NRFundingReferenceUISchema,
    NRGeoLocationPointUISchema,
    NRGeoLocationUISchema,
    NRItemRelationTypeVocabularyUISchema,
    NRLanguageVocabularyUISchema,
    NRLocationUISchema,
    NROrganizationUISchema,
    NRPersonUISchema,
    NRRelatedItemContributorUISchema,
    NRRelatedItemCreatorUISchema,
    NRRelatedItemUISchema,
    NRResourceTypeVocabularyUISchema,
    NRRightsVocabularyUISchema,
    NRSeriesUISchema,
    NRSubjectCategoryVocabularyUISchema,
    NRSubjectUISchema,
)
from nr_metadata.ui_schema.identifiers import (
    NRObjectIdentifierUISchema,
    NROrganizationIdentifierUISchema,
    NRPersonIdentifierUISchema,
    NRSystemIdentifierUISchema,
)


class NRDataRecordUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDataMetadataUISchema())


class GeoLocationsItemUISchema(NRGeoLocationUISchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPoint = ma_fields.Nested(lambda: GeoLocationPointUISchema())


class NRDataMetadataUISchema(NRCommonMetadataUISchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesItemUISchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemUISchema()))

    dateCollected = LocalizedEDTFInterval()

    dateCreated = LocalizedEDTFInterval()

    dateValidTo = LocalizedDate()

    dateWithdrawn = ma_fields.Nested(lambda: DateWithdrawnUISchema())

    publishers = ma_fields.List(ma_fields.Nested(lambda: PublishersItemUISchema()))


class RelatedItemsItemUISchema(NRRelatedItemUISchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: ItemContributorsItemUISchema())
    )


class AccessRightsUISchema(NRAccessRightsVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class AdditionalTitlesItemUISchema(AdditionalTitlesUISchema):
    class Meta:
        unknown = ma.RAISE


class AffiliationsItemUISchema(NRAffiliationVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    ror = ma_fields.String()

    title = VocabularyI18nStrUIField()


class AuthorityIdentifiersItemUISchema(NROrganizationIdentifierUISchema):
    class Meta:
        unknown = ma.RAISE


class ContributorsItemUISchema(NRContributorUISchema):
    class Meta:
        unknown = ma.RAISE


class CountryUISchema(NRCountryVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class CreatorsItemUISchema(NRCreatorUISchema):
    class Meta:
        unknown = ma.RAISE


class DateWithdrawnUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateInformation = ma_fields.String()

    type = LocalizedDate()


class EventLocationUISchema(NRLocationUISchema):
    class Meta:
        unknown = ma.RAISE


class EventsItemUISchema(NREventUISchema):
    class Meta:
        unknown = ma.RAISE


class FunderUISchema(NRFunderVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class FundingReferencesItemUISchema(NRFundingReferenceUISchema):
    class Meta:
        unknown = ma.RAISE


class GeoLocationPointUISchema(NRGeoLocationPointUISchema):
    class Meta:
        unknown = ma.RAISE


class ItemContributorsItemUISchema(NRRelatedItemContributorUISchema):
    class Meta:
        unknown = ma.RAISE


class ItemCreatorsItemUISchema(NRRelatedItemCreatorUISchema):
    class Meta:
        unknown = ma.RAISE


class ItemRelationTypeUISchema(NRItemRelationTypeVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class ItemResourceTypeUISchema(NRResourceTypeVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class LanguagesItemUISchema(NRLanguageVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class ObjectIdentifiersItemUISchema(NRObjectIdentifierUISchema):
    class Meta:
        unknown = ma.RAISE


class OrganizationalUISchema(NROrganizationUISchema):
    class Meta:
        unknown = ma.RAISE


class PersonalAuthorityIdentifiersItemUISchema(NRPersonIdentifierUISchema):
    class Meta:
        unknown = ma.RAISE


class PersonalUISchema(NRPersonUISchema):
    class Meta:
        unknown = ma.RAISE


class PublishersItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    ror = ma_fields.String()

    title = VocabularyI18nStrUIField()


class RightsUISchema(NRRightsVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class SeriesItemUISchema(NRSeriesUISchema):
    class Meta:
        unknown = ma.RAISE


class SubjectCategoriesItemUISchema(NRSubjectCategoryVocabularyUISchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class SubjectsItemUISchema(NRSubjectUISchema):
    class Meta:
        unknown = ma.RAISE


class SystemIdentifiersItemUISchema(NRSystemIdentifierUISchema):
    class Meta:
        unknown = ma.RAISE
