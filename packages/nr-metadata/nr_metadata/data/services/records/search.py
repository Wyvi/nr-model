from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


class DataSearchOptions(InvenioSearchOptions):
    """DataRecord search options."""

    facet_groups = {
        "default": {
            "metadata_abstract_cs": facets.metadata_abstract_cs,
            "metadata_abstract_en": facets.metadata_abstract_en,
            "metadata_additionalTitles_title_cs": (
                facets.metadata_additionalTitles_title_cs
            ),
            "metadata_additionalTitles_title_en": (
                facets.metadata_additionalTitles_title_en
            ),
            "metadata_methods_cs": facets.metadata_methods_cs,
            "metadata_methods_en": facets.metadata_methods_en,
            "metadata_subjects_subject_cs": facets.metadata_subjects_subject_cs,
            "metadata_subjects_subject_en": facets.metadata_subjects_subject_en,
            "metadata_technicalInfo_cs": facets.metadata_technicalInfo_cs,
            "metadata_technicalInfo_en": facets.metadata_technicalInfo_en,
            **getattr(InvenioSearchOptions, "facet_groups", {}).get("default", {}),
        },
    }

    facets = {
        "metadata_abstract_cs": facets.metadata_abstract_cs,
        "metadata_abstract_en": facets.metadata_abstract_en,
        "metadata_abstract_lang": facets.metadata_abstract_lang,
        "metadata_accessRights": facets.metadata_accessRights,
        "metadata_additionalTitles_title_cs": facets.metadata_additionalTitles_title_cs,
        "metadata_additionalTitles_title_en": facets.metadata_additionalTitles_title_en,
        "metadata_additionalTitles_title_lang": (
            facets.metadata_additionalTitles_title_lang
        ),
        "metadata_additionalTitles_titleType": (
            facets.metadata_additionalTitles_titleType
        ),
        "metadata_contributors_affiliations": facets.metadata_contributors_affiliations,
        "metadata_contributors_authorityIdentifiers_identifier": (
            facets.metadata_contributors_authorityIdentifiers_identifier
        ),
        "metadata_contributors_authorityIdentifiers_scheme": (
            facets.metadata_contributors_authorityIdentifiers_scheme
        ),
        "metadata_contributors_contributorType": (
            facets.metadata_contributors_contributorType
        ),
        "metadata_contributors_familyName": facets.metadata_contributors_familyName,
        "metadata_contributors_fullName": facets.metadata_contributors_fullName,
        "metadata_contributors_givenName": facets.metadata_contributors_givenName,
        "metadata_contributors_nameType": facets.metadata_contributors_nameType,
        "metadata_creators_affiliations": facets.metadata_creators_affiliations,
        "metadata_creators_authorityIdentifiers_identifier": (
            facets.metadata_creators_authorityIdentifiers_identifier
        ),
        "metadata_creators_authorityIdentifiers_scheme": (
            facets.metadata_creators_authorityIdentifiers_scheme
        ),
        "metadata_creators_fullName": facets.metadata_creators_fullName,
        "metadata_creators_nameType": facets.metadata_creators_nameType,
        "metadata_dateAvailable": facets.metadata_dateAvailable,
        "metadata_dateIssued": facets.metadata_dateIssued,
        "metadata_dateValidTo": facets.metadata_dateValidTo,
        "metadata_dateWithdrawn_date": facets.metadata_dateWithdrawn_date,
        "metadata_dateWithdrawn_dateInformation": (
            facets.metadata_dateWithdrawn_dateInformation
        ),
        "metadata_fundingReferences_funder": facets.metadata_fundingReferences_funder,
        "metadata_fundingReferences_projectID": (
            facets.metadata_fundingReferences_projectID
        ),
        "metadata_geoLocations_geoLocationPlace": (
            facets.metadata_geoLocations_geoLocationPlace
        ),
        "metadata_geoLocations_geoLocationPoint_pointLatitude": (
            facets.metadata_geoLocations_geoLocationPoint_pointLatitude
        ),
        "metadata_geoLocations_geoLocationPoint_pointLongitude": (
            facets.metadata_geoLocations_geoLocationPoint_pointLongitude
        ),
        "metadata_languages": facets.metadata_languages,
        "metadata_methods_cs": facets.metadata_methods_cs,
        "metadata_methods_en": facets.metadata_methods_en,
        "metadata_methods_lang": facets.metadata_methods_lang,
        "metadata_objectIdentifiers_identifier": (
            facets.metadata_objectIdentifiers_identifier
        ),
        "metadata_objectIdentifiers_scheme": facets.metadata_objectIdentifiers_scheme,
        "metadata_objectIdentifiers_status": facets.metadata_objectIdentifiers_status,
        "metadata_publicationYear": facets.metadata_publicationYear,
        "metadata_publishers": facets.metadata_publishers,
        "metadata_relatedItems_itemContributors_affiliations": (
            facets.metadata_relatedItems_itemContributors_affiliations
        ),
        "metadata_relatedItems_itemContributors_authorityIdentifiers_identifier": (
            facets.metadata_relatedItems_itemContributors_authorityIdentifiers_identifier
        ),
        "metadata_relatedItems_itemContributors_authorityIdentifiers_scheme": (
            facets.metadata_relatedItems_itemContributors_authorityIdentifiers_scheme
        ),
        "metadata_relatedItems_itemContributors_contributorType": (
            facets.metadata_relatedItems_itemContributors_contributorType
        ),
        "metadata_relatedItems_itemContributors_familyName": (
            facets.metadata_relatedItems_itemContributors_familyName
        ),
        "metadata_relatedItems_itemContributors_fullName": (
            facets.metadata_relatedItems_itemContributors_fullName
        ),
        "metadata_relatedItems_itemContributors_givenName": (
            facets.metadata_relatedItems_itemContributors_givenName
        ),
        "metadata_relatedItems_itemContributors_nameType": (
            facets.metadata_relatedItems_itemContributors_nameType
        ),
        "metadata_relatedItems_itemCreators_affiliations": (
            facets.metadata_relatedItems_itemCreators_affiliations
        ),
        "metadata_relatedItems_itemCreators_authorityIdentifiers_identifier": (
            facets.metadata_relatedItems_itemCreators_authorityIdentifiers_identifier
        ),
        "metadata_relatedItems_itemCreators_authorityIdentifiers_scheme": (
            facets.metadata_relatedItems_itemCreators_authorityIdentifiers_scheme
        ),
        "metadata_relatedItems_itemCreators_fullName": (
            facets.metadata_relatedItems_itemCreators_fullName
        ),
        "metadata_relatedItems_itemCreators_nameType": (
            facets.metadata_relatedItems_itemCreators_nameType
        ),
        "metadata_relatedItems_itemEndPage": facets.metadata_relatedItems_itemEndPage,
        "metadata_relatedItems_itemIssue": facets.metadata_relatedItems_itemIssue,
        "metadata_relatedItems_itemPIDs_identifier": (
            facets.metadata_relatedItems_itemPIDs_identifier
        ),
        "metadata_relatedItems_itemPIDs_scheme": (
            facets.metadata_relatedItems_itemPIDs_scheme
        ),
        "metadata_relatedItems_itemPublisher": (
            facets.metadata_relatedItems_itemPublisher
        ),
        "metadata_relatedItems_itemRelationType": (
            facets.metadata_relatedItems_itemRelationType
        ),
        "metadata_relatedItems_itemResourceType": (
            facets.metadata_relatedItems_itemResourceType
        ),
        "metadata_relatedItems_itemStartPage": (
            facets.metadata_relatedItems_itemStartPage
        ),
        "metadata_relatedItems_itemURL": facets.metadata_relatedItems_itemURL,
        "metadata_relatedItems_itemVolume": facets.metadata_relatedItems_itemVolume,
        "metadata_relatedItems_itemYear": facets.metadata_relatedItems_itemYear,
        "metadata_resourceType": facets.metadata_resourceType,
        "metadata_subjectCategories": facets.metadata_subjectCategories,
        "metadata_subjects_classificationCode": (
            facets.metadata_subjects_classificationCode
        ),
        "metadata_subjects_subject_cs": facets.metadata_subjects_subject_cs,
        "metadata_subjects_subject_en": facets.metadata_subjects_subject_en,
        "metadata_subjects_subject_lang": facets.metadata_subjects_subject_lang,
        "metadata_subjects_subjectScheme": facets.metadata_subjects_subjectScheme,
        "metadata_subjects_valueURI": facets.metadata_subjects_valueURI,
        "metadata_technicalInfo_cs": facets.metadata_technicalInfo_cs,
        "metadata_technicalInfo_en": facets.metadata_technicalInfo_en,
        "metadata_technicalInfo_lang": facets.metadata_technicalInfo_lang,
        "metadata_version": facets.metadata_version,
        **getattr(InvenioSearchOptions, "facets", {}),
        "metadata_abstract_cs": facets.metadata_abstract_cs,
        "metadata_abstract_en": facets.metadata_abstract_en,
        "metadata_abstract_lang": facets.metadata_abstract_lang,
        "metadata_accessRights": facets.metadata_accessRights,
        "metadata_additionalTitles_title_cs": facets.metadata_additionalTitles_title_cs,
        "metadata_additionalTitles_title_en": facets.metadata_additionalTitles_title_en,
        "metadata_additionalTitles_title_lang": (
            facets.metadata_additionalTitles_title_lang
        ),
        "metadata_additionalTitles_titleType": (
            facets.metadata_additionalTitles_titleType
        ),
        "metadata_contributors_affiliations": facets.metadata_contributors_affiliations,
        "metadata_contributors_authorityIdentifiers_identifier": (
            facets.metadata_contributors_authorityIdentifiers_identifier
        ),
        "metadata_contributors_authorityIdentifiers_scheme": (
            facets.metadata_contributors_authorityIdentifiers_scheme
        ),
        "metadata_contributors_contributorType": (
            facets.metadata_contributors_contributorType
        ),
        "metadata_contributors_familyName": facets.metadata_contributors_familyName,
        "metadata_contributors_fullName": facets.metadata_contributors_fullName,
        "metadata_contributors_givenName": facets.metadata_contributors_givenName,
        "metadata_contributors_nameType": facets.metadata_contributors_nameType,
        "metadata_creators_affiliations": facets.metadata_creators_affiliations,
        "metadata_creators_authorityIdentifiers_identifier": (
            facets.metadata_creators_authorityIdentifiers_identifier
        ),
        "metadata_creators_authorityIdentifiers_scheme": (
            facets.metadata_creators_authorityIdentifiers_scheme
        ),
        "metadata_creators_fullName": facets.metadata_creators_fullName,
        "metadata_creators_nameType": facets.metadata_creators_nameType,
        "metadata_dateAvailable": facets.metadata_dateAvailable,
        "metadata_dateIssued": facets.metadata_dateIssued,
        "metadata_dateModified": facets.metadata_dateModified,
        "metadata_dateValidTo": facets.metadata_dateValidTo,
        "metadata_dateWithdrawn_date": facets.metadata_dateWithdrawn_date,
        "metadata_dateWithdrawn_dateInformation": (
            facets.metadata_dateWithdrawn_dateInformation
        ),
        "metadata_fundingReferences_funder": facets.metadata_fundingReferences_funder,
        "metadata_fundingReferences_projectID": (
            facets.metadata_fundingReferences_projectID
        ),
        "metadata_geoLocations_geoLocationPlace": (
            facets.metadata_geoLocations_geoLocationPlace
        ),
        "metadata_geoLocations_geoLocationPoint_pointLatitude": (
            facets.metadata_geoLocations_geoLocationPoint_pointLatitude
        ),
        "metadata_geoLocations_geoLocationPoint_pointLongitude": (
            facets.metadata_geoLocations_geoLocationPoint_pointLongitude
        ),
        "metadata_languages": facets.metadata_languages,
        "metadata_methods_cs": facets.metadata_methods_cs,
        "metadata_methods_en": facets.metadata_methods_en,
        "metadata_methods_lang": facets.metadata_methods_lang,
        "metadata_objectIdentifiers_identifier": (
            facets.metadata_objectIdentifiers_identifier
        ),
        "metadata_objectIdentifiers_scheme": facets.metadata_objectIdentifiers_scheme,
        "metadata_objectIdentifiers_status": facets.metadata_objectIdentifiers_status,
        "metadata_publicationYear": facets.metadata_publicationYear,
        "metadata_publishers": facets.metadata_publishers,
        "metadata_relatedItems_itemContributors_affiliations": (
            facets.metadata_relatedItems_itemContributors_affiliations
        ),
        "metadata_relatedItems_itemContributors_authorityIdentifiers_identifier": (
            facets.metadata_relatedItems_itemContributors_authorityIdentifiers_identifier
        ),
        "metadata_relatedItems_itemContributors_authorityIdentifiers_scheme": (
            facets.metadata_relatedItems_itemContributors_authorityIdentifiers_scheme
        ),
        "metadata_relatedItems_itemContributors_contributorType": (
            facets.metadata_relatedItems_itemContributors_contributorType
        ),
        "metadata_relatedItems_itemContributors_familyName": (
            facets.metadata_relatedItems_itemContributors_familyName
        ),
        "metadata_relatedItems_itemContributors_fullName": (
            facets.metadata_relatedItems_itemContributors_fullName
        ),
        "metadata_relatedItems_itemContributors_givenName": (
            facets.metadata_relatedItems_itemContributors_givenName
        ),
        "metadata_relatedItems_itemContributors_nameType": (
            facets.metadata_relatedItems_itemContributors_nameType
        ),
        "metadata_relatedItems_itemCreators_affiliations": (
            facets.metadata_relatedItems_itemCreators_affiliations
        ),
        "metadata_relatedItems_itemCreators_authorityIdentifiers_identifier": (
            facets.metadata_relatedItems_itemCreators_authorityIdentifiers_identifier
        ),
        "metadata_relatedItems_itemCreators_authorityIdentifiers_scheme": (
            facets.metadata_relatedItems_itemCreators_authorityIdentifiers_scheme
        ),
        "metadata_relatedItems_itemCreators_fullName": (
            facets.metadata_relatedItems_itemCreators_fullName
        ),
        "metadata_relatedItems_itemCreators_nameType": (
            facets.metadata_relatedItems_itemCreators_nameType
        ),
        "metadata_relatedItems_itemEndPage": facets.metadata_relatedItems_itemEndPage,
        "metadata_relatedItems_itemIssue": facets.metadata_relatedItems_itemIssue,
        "metadata_relatedItems_itemPIDs_identifier": (
            facets.metadata_relatedItems_itemPIDs_identifier
        ),
        "metadata_relatedItems_itemPIDs_scheme": (
            facets.metadata_relatedItems_itemPIDs_scheme
        ),
        "metadata_relatedItems_itemPublisher": (
            facets.metadata_relatedItems_itemPublisher
        ),
        "metadata_relatedItems_itemRelationType": (
            facets.metadata_relatedItems_itemRelationType
        ),
        "metadata_relatedItems_itemResourceType": (
            facets.metadata_relatedItems_itemResourceType
        ),
        "metadata_relatedItems_itemStartPage": (
            facets.metadata_relatedItems_itemStartPage
        ),
        "metadata_relatedItems_itemURL": facets.metadata_relatedItems_itemURL,
        "metadata_relatedItems_itemVolume": facets.metadata_relatedItems_itemVolume,
        "metadata_relatedItems_itemYear": facets.metadata_relatedItems_itemYear,
        "metadata_resourceType": facets.metadata_resourceType,
        "metadata_subjectCategories": facets.metadata_subjectCategories,
        "metadata_subjects_classificationCode": (
            facets.metadata_subjects_classificationCode
        ),
        "metadata_subjects_subject_cs": facets.metadata_subjects_subject_cs,
        "metadata_subjects_subject_en": facets.metadata_subjects_subject_en,
        "metadata_subjects_subject_lang": facets.metadata_subjects_subject_lang,
        "metadata_subjects_subjectScheme": facets.metadata_subjects_subjectScheme,
        "metadata_subjects_valueURI": facets.metadata_subjects_valueURI,
        "metadata_technicalInfo_cs": facets.metadata_technicalInfo_cs,
        "metadata_technicalInfo_en": facets.metadata_technicalInfo_en,
        "metadata_technicalInfo_lang": facets.metadata_technicalInfo_lang,
        "metadata_version": facets.metadata_version,
        **getattr(InvenioSearchOptions, "facets", {}),
    }

    facet_groups = {
        "default": {
            "metadata_abstract_cs": facets.metadata_abstract_cs,
            "metadata_abstract_en": facets.metadata_abstract_en,
            "metadata_additionalTitles_title_cs": (
                facets.metadata_additionalTitles_title_cs
            ),
            "metadata_additionalTitles_title_en": (
                facets.metadata_additionalTitles_title_en
            ),
            "metadata_methods_cs": facets.metadata_methods_cs,
            "metadata_methods_en": facets.metadata_methods_en,
            "metadata_subjects_subject_cs": facets.metadata_subjects_subject_cs,
            "metadata_subjects_subject_en": facets.metadata_subjects_subject_en,
            "metadata_technicalInfo_cs": facets.metadata_technicalInfo_cs,
            "metadata_technicalInfo_en": facets.metadata_technicalInfo_en,
            **getattr(InvenioSearchOptions, "facet_groups", {}).get("default", {}),
        },
    }
