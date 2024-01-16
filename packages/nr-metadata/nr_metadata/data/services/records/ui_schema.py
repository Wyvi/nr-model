import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.i18n_ui import I18nStrUIField, MultilingualUIField
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import (
    InvenioUISchema,
    LocalizedDate,
    LocalizedEDTF,
    LocalizedEDTFInterval,
)
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

from nr_metadata.common.services.records.ui_schema_common import (
    AdditionalTitlesUISchema,
)
from nr_metadata.common.services.records.ui_schema_datatypes import (
    NRAccessRightsVocabularyUISchema,
    NRAffiliationVocabularyUISchema,
    NRAuthorityUIUISchema,
    NRFundingReferenceUISchema,
    NRGeoLocationUISchema,
    NRLanguageVocabularyUISchema,
    NRResourceTypeVocabularyUISchema,
    NRSubjectCategoryVocabularyUISchema,
    NRSubjectUISchema,
)
from nr_metadata.ui_schema.identifiers import (
    NRAuthorityIdentifierUISchema,
    NRObjectIdentifierUISchema,
)


class NRDataRecordUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDataMetadataUISchema())


class NRDataMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    abstract = MultilingualUIField(I18nStrUIField(), required=True)

    accessRights = ma_fields.Nested(lambda: NRAccessRightsVocabularyUISchema())

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesUISchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemUISchema()))

    creators = ma_fields.List(ma_fields.Nested(lambda: NRAuthorityUIUISchema()))

    dateAvailable = LocalizedDate()

    dateCollected = LocalizedEDTFInterval()

    dateCreated = LocalizedEDTFInterval()

    dateIssued = LocalizedEDTF()

    dateValidTo = LocalizedEDTF()

    dateWithdrawn = ma_fields.Nested(lambda: DateWithdrawnUISchema())

    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: NRFundingReferenceUISchema())
    )

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationUISchema()))

    languages = ma_fields.List(ma_fields.Nested(lambda: NRLanguageVocabularyUISchema()))

    methods = MultilingualUIField(I18nStrUIField())

    notes = ma_fields.List(ma_fields.String())

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierUISchema())
    )

    publicationYear = ma_fields.Integer(required=True)

    publishers = ma_fields.List(ma_fields.Nested(lambda: PublishersItemUISchema()))

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: RelatedItemsItemUISchema()))

    resourceType = ma_fields.Nested(
        lambda: NRResourceTypeVocabularyUISchema(), required=True
    )

    subjectCategories = ma_fields.List(
        ma_fields.Nested(lambda: NRSubjectCategoryVocabularyUISchema())
    )

    subjects = ma_fields.List(ma_fields.Nested(lambda: NRSubjectUISchema()))

    technicalInfo = MultilingualUIField(I18nStrUIField())

    title = ma_fields.String(required=True)

    version = ma_fields.String()

    dateModified = LocalizedDate()


class RelatedItemsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: ContributorsItemUISchema())
    )

    itemCreators = ma_fields.List(ma_fields.Nested(lambda: NRAuthorityUIUISchema()))

    itemEndPage = ma_fields.String()

    itemIssue = ma_fields.String()

    itemPIDs = ma_fields.List(ma_fields.Nested(lambda: NRObjectIdentifierUISchema()))

    itemPublisher = ma_fields.String()

    itemRelationType = ma_fields.Nested(
        lambda: ContributorTypeUISchema(), required=True
    )

    itemResourceType = ma_fields.Nested(
        lambda: ContributorTypeUISchema(), required=True
    )

    itemStartPage = ma_fields.String()

    itemTitle = ma_fields.String()

    itemURL = ma_fields.String()

    itemVolume = ma_fields.String()

    itemYear = LocalizedDate()


class ContributorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )

    contributorType = ma_fields.Nested(lambda: ContributorTypeUISchema(), required=True)

    familyName = ma_fields.String()

    fullName = ma_fields.String(required=True)

    givenName = ma_fields.String()

    nameType = ma_fields.String(validate=[OneOf(["Personal", "Personal"])])


class ContributorTypeUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class DateWithdrawnUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = LocalizedDate()

    dateInformation = ma_fields.String()


class PublishersItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    ror = ma_fields.String()

    title = VocabularyI18nStrUIField()
