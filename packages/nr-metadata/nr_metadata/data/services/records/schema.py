import marshmallow as ma
from edtf import Date as EDTFDate
from edtf import Interval as EDTFInterval
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from marshmallow_utils.fields import TrimmedString
from oarepo_runtime.services.schema.i18n import I18nStrField, MultilingualField
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_date,
)
from oarepo_vocabularies.services.schema import HierarchySchema

from nr_metadata.common.schema.identifiers import (
    NRObjectIdentifierSchema,
    NROrganizationIdentifierSchema,
    NRPersonIdentifierSchema,
    NRSystemIdentifierSchema,
)
from nr_metadata.common.services.records.schema_common import (
    AdditionalTitlesSchema,
    NRCreatorSchema,
)
from nr_metadata.common.services.records.schema_datatypes import (
    NRAccessRightsVocabularySchema,
    NRAffiliationVocabularySchema,
    NRAuthoritySchema,
    NRCountryVocabularySchema,
    NREventSchema,
    NRFunderVocabularySchema,
    NRFundingReferenceSchema,
    NRGeoLocationPointSchema,
    NRGeoLocationSchema,
    NRItemRelationTypeVocabularySchema,
    NRLanguageVocabularySchema,
    NRLocationSchema,
    NRObjectIdentifierSchema,
    NROrganizationIdentifierSchema,
    NROrganizationSchema,
    NRPersonIdentifierSchema,
    NRPersonSchema,
    NRRelatedItemContributorSchema,
    NRRelatedItemCreatorSchema,
    NRResourceTypeVocabularySchema,
    NRRightsVocabularySchema,
    NRSeriesSchema,
    NRSubjectCategoryVocabularySchema,
    NRSubjectSchema,
    NRSystemIdentifierSchema,
)
from nr_metadata.schema.identifiers import (
    NRAuthorityIdentifierSchema,
    NRObjectIdentifierSchema,
    NROrganizationIdentifierSchema,
    NRPersonIdentifierSchema,
    NRSystemIdentifierSchema,
)


class NRDataRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDataMetadataSchema())


class NRDataMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    abstract = MultilingualField(I18nStrField(), required=True)

    accessRights = ma_fields.Nested(lambda: NRAccessRightsVocabularySchema())

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemSchema()))

    creators = ma_fields.List(ma_fields.Nested(lambda: NRAuthoritySchema()))

    dateAvailable = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    dateCollected = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    dateCreated = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    dateIssued = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    dateValidTo = TrimmedString(
        validate=[
            CachedMultilayerEDTFValidator(types=(EDTFDate,)),
            validate_date("%Y-%m-%d"),
        ]
    )

    dateWithdrawn = ma_fields.Nested(lambda: DateWithdrawnSchema())

    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: NRFundingReferenceSchema())
    )

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationSchema()))

    languages = ma_fields.List(ma_fields.Nested(lambda: NRLanguageVocabularySchema()))

    methods = MultilingualField(I18nStrField())

    notes = ma_fields.List(ma_fields.String())

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierSchema())
    )

    publicationYear = ma_fields.Integer(required=True)

    publishers = ma_fields.List(
        ma_fields.Nested(lambda: PublishersItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: RelatedItemsItemSchema()))

    resourceType = ma_fields.Nested(
        lambda: NRResourceTypeVocabularySchema(), required=True
    )

    subjectCategories = ma_fields.List(
        ma_fields.Nested(lambda: NRSubjectCategoryVocabularySchema())
    )

    subjects = ma_fields.List(ma_fields.Nested(lambda: NRSubjectSchema()))

    technicalInfo = MultilingualField(I18nStrField())

    title = ma_fields.String(required=True)

    version = ma_fields.String()

    dateModified = ma_fields.String(validate=[validate_date("%Y-%m-%d")])


class RelatedItemsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: ContributorsItemSchema())
    )

    itemCreators = ma_fields.List(ma_fields.Nested(lambda: NRAuthoritySchema()))

    itemEndPage = ma_fields.String()

    itemIssue = ma_fields.String()

    itemPIDs = ma_fields.List(ma_fields.Nested(lambda: NRObjectIdentifierSchema()))

    itemPublisher = ma_fields.String()

    itemRelationType = ma_fields.Nested(lambda: ContributorTypeSchema(), required=True)

    itemResourceType = ma_fields.Nested(lambda: ContributorTypeSchema(), required=True)

    itemStartPage = ma_fields.String()

    itemTitle = ma_fields.String()

    itemURL = ma_fields.String()

    itemVolume = ma_fields.String()

    itemYear = ma_fields.String(validate=[validate_date("%Y-%m-%d")])


class ContributorsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierSchema())
    )

    contributorType = ma_fields.Nested(lambda: ContributorTypeSchema(), required=True)

    familyName = ma_fields.String()

    fullName = ma_fields.String(required=True)

    givenName = ma_fields.String()

    nameType = ma_fields.String(validate=[OneOf(["Personal", "Personal"])])

    Organizational = ma_fields.Nested(lambda: OrganizationalSchema())

    Personal = ma_fields.Nested(lambda: PersonalSchema())

    type_field = "nameType"


class ContributorTypeSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class DateWithdrawnSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    dateInformation = ma_fields.String()

    type = ma_fields.String(validate=[validate_date("%Y-%m-%d")])


class PublishersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    ror = ma_fields.String()

    title = i18n_strings


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
