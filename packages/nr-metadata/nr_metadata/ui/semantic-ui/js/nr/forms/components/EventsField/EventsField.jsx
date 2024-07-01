import React from "react";
import PropTypes from "prop-types";
import { ArrayField, TextField, GroupField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import { LocalVocabularySelectField } from "@js/oarepo_vocabularies";
import { StringArrayField } from "../StringArray/StringArrayField";
import {
  ArrayFieldItem,
  EDTFDaterangePicker,
  sanitizeInput,
  useFieldData,
} from "@js/oarepo_ui";
import { useFormikContext, getIn } from "formik";

export const EventsField = ({
  fieldPath,
  helpText,
  validTags,
  label,
  useModelData,
  addButtonLabel,
}) => {
  const { values, setFieldValue, setFieldTouched } = useFormikContext();
  const { getFieldData } = useFieldData();

  return (
    <ArrayField
      addButtonLabel={addButtonLabel}
      fieldPath={fieldPath}
      label={label}
      helpText={helpText}
      {...(useModelData ? getFieldData(fieldPath).fullRepresentation : {})}
      addButtonClassName="array-field-add-button"
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        return (
          <ArrayFieldItem
            indexPath={indexPath}
            arrayHelpers={arrayHelpers}
            className={"invenio-group-field events"}
            fieldPathPrefix={fieldPathPrefix}
          >
            <TextField
              width={16}
              fieldPath={`${fieldPathPrefix}.eventNameOriginal`}
              required
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.eventNameOriginal`)
                    .compactRepresentation
                : {})}
              onBlur={() => {
                const cleanedContent = sanitizeInput(
                  getIn(values, `${fieldPathPrefix}.eventNameOriginal`),
                  validTags
                );
                setFieldValue(
                  `${fieldPathPrefix}.eventNameOriginal`,
                  cleanedContent
                );
                setFieldTouched(`${fieldPathPrefix}.eventNameOriginal`, true);
              }}
            />
            <StringArrayField
              width={16}
              fieldPath={`${fieldPathPrefix}.eventNameAlternate`}
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.eventNameAlternate`)
                    .compactRepresentation
                : {})}
            />
            <EDTFDaterangePicker
              required
              fieldPath={`${fieldPathPrefix}.eventDate`}
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.eventDate`, "calendar")
                    .fullRepresentation
                : {})}
            />
            <GroupField>
              <TextField
                width={10}
                fieldPath={`${fieldPathPrefix}.eventLocation.place`}
                label={i18next.t("Place")}
                placeholder={i18next.t("Write down the place of the event.")}
                required
              />
              <LocalVocabularySelectField
                selectOnBlur={false}
                width={6}
                fieldPath={`${fieldPathPrefix}.eventLocation.country`}
                optionsListName="countries"
                clearable
                {...(useModelData
                  ? getFieldData(`${fieldPathPrefix}.eventLocation.country`)
                      .compactRepresentation
                  : {})}
              />
            </GroupField>
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

EventsField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  helpText: PropTypes.string,
  useModelData: PropTypes.bool,
  addButtonLabel: PropTypes.string,
  label: PropTypes.string,
  eventNameOriginalLabel: PropTypes.string,
  eventNameOriginalPlaceholder: PropTypes.string,
  eventNameAlternateLabel: PropTypes.string,
  eventNameAlternateAddButtonLabel: PropTypes.string,
  eventNameAlternateHelpText: PropTypes.string,
  eventDateLabel: PropTypes.string,
  eventLocationPlaceLabel: PropTypes.string,
  eventLocationPlacePlaceholder: PropTypes.string,
  eventLocationCountryLabel: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.node,
  ]),
  eventLocationCountryPlaceholder: PropTypes.string,
};

EventsField.defaultProps = {
  helpText: i18next.t("Provide details about the events."),
  useModelData: true,
  addButtonLabel: i18next.t("Add event"),
  label: i18next.t("Events"),
  eventNameOriginalLabel: i18next.t("Event name"),
  eventNameOriginalPlaceholder: i18next.t(
    "Write down the main name of the event."
  ),
  eventNameAlternateLabel: i18next.t("Event alternate name"),
  eventNameAlternateAddButtonLabel: i18next.t("Add event alternate name"),
  eventNameAlternateHelpText: i18next.t(
    "If event has other known names, write them here."
  ),
  eventDateLabel: i18next.t("Event date"),
  eventLocationPlaceLabel: i18next.t("Place"),
  eventLocationPlacePlaceholder: i18next.t(
    "Write down the place of the event."
  ),
  eventLocationCountryLabel: i18next.t("Country"),
  eventLocationCountryPlaceholder: i18next.t("Choose country from the list."),
};
