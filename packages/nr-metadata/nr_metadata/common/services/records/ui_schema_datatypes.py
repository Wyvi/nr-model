import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.i18n_ui import I18nStrUIField
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import LocalizedEDTFInterval
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

from nr_metadata.ui_schema.identifiers import (
    NRAuthorityIdentifierUISchema,
    NRObjectIdentifierUISchema,
)


class NREventUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eventDate = LocalizedEDTFInterval(required=True)

    eventLocation = ma_fields.Nested(lambda: NRLocationUISchema(), required=True)

    eventNameAlternate = ma_fields.List(ma_fields.String())

    eventNameOriginal = ma_fields.String(required=True)


class NRRelatedItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: NRRelatedItemContributorUISchema())
    )

    itemCreators = ma_fields.List(
        ma_fields.Nested(lambda: NRRelatedItemCreatorUISchema())
    )

    itemEndPage = ma_fields.String()

    itemIssue = ma_fields.String()

    itemPIDs = ma_fields.List(ma_fields.Nested(lambda: NRObjectIdentifierUISchema()))

    itemPublisher = ma_fields.String()

    itemRelationType = ma_fields.Nested(lambda: NRItemRelationTypeVocabularyUISchema())

    itemResourceType = ma_fields.Nested(lambda: NRResourceTypeVocabularyUISchema())

    itemStartPage = ma_fields.String()

    itemTitle = ma_fields.String(required=True)

    itemURL = ma_fields.String()

    itemVolume = ma_fields.String()

    itemYear = ma_fields.Integer()


class NRFundingReferenceUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    funder = ma_fields.Nested(lambda: NRFunderVocabularyUISchema())

    fundingProgram = ma_fields.String()

    projectID = ma_fields.String(required=True)

    projectName = ma_fields.String()


class NRGeoLocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPlace = ma_fields.String(required=True)

    geoLocationPoint = ma_fields.Nested(lambda: NRGeoLocationPointUISchema())


class NRLocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    country = ma_fields.Nested(lambda: NRCountryVocabularyUISchema())

    place = ma_fields.String(required=True)


class NRRelatedItemContributorUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])

    role = ma_fields.Nested(lambda: NRAuthorityRoleVocabularyUISchema())


class NRRelatedItemCreatorUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])


class NRAccessRightsVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRAffiliationVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()


class NRAuthorityRoleVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRCountryVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRExternalLocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    externalLocationNote = ma_fields.String()

    externalLocationURL = ma_fields.String(required=True)


class NRFunderVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRGeoLocationPointUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma_fields.Float(required=True)

    pointLongitude = ma_fields.Float(required=True)


class NRItemRelationTypeVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRLanguageVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRLicenseVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRResourceTypeVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRSeriesUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    seriesTitle = ma_fields.String(required=True)

    seriesVolume = ma_fields.String()


class NRSubjectCategoryVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRSubjectUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma_fields.String()

    subject = I18nStrUIField()

    subjectScheme = ma_fields.String()

    valueURI = ma_fields.String()
