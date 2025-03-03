import React from "react";
import PropTypes from "prop-types";
import { ArrayField, TextField, GroupField } from "react-invenio-forms";
import { LocalVocabularySelectField } from "@js/oarepo_vocabularies";
import { StringArrayField } from "../StringArray/StringArrayField";
import {
  ArrayFieldItem,
  EDTFDaterangePicker,
  useSanitizeInput,
  useFieldData,
} from "@js/oarepo_ui";
import { i18next } from "@translations/nr/i18next";
import { useFormikContext, getIn } from "formik";
import { Label } from "semantic-ui-react";

export const EventsField = ({ fieldPath }) => {
  const { values, setFieldValue, setFieldTouched, errors } = useFormikContext();

  const { sanitizeInput } = useSanitizeInput();
  const { getFieldData } = useFieldData();
  return (
    <ArrayField
      addButtonLabel={i18next.t("Add event")}
      fieldPath={fieldPath}
      {...getFieldData({ fieldPath, fieldRepresentation: "text" })}
      addButtonClassName="array-field-add-button"
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        const eventNameOriginalFieldPath = `${fieldPathPrefix}.eventNameOriginal`;

        const beValidationErrors = getIn(errors, "BEvalidationErrors", {});
        const eventLocationError = beValidationErrors?.errors?.find(
          (e) => e.field === `${fieldPathPrefix}.eventLocation`
        );

        return (
          <ArrayFieldItem
            indexPath={indexPath}
            arrayHelpers={arrayHelpers}
            className={"invenio-group-field events"}
            fieldPathPrefix={fieldPathPrefix}
          >
            <TextField
              width={16}
              fieldPath={eventNameOriginalFieldPath}
              {...getFieldData({
                fieldPath: eventNameOriginalFieldPath,
                fieldRepresentation: "compact",
              })}
              onBlur={() => {
                const cleanedContent = sanitizeInput(
                  getIn(values, eventNameOriginalFieldPath)
                );
                setFieldValue(eventNameOriginalFieldPath, cleanedContent);
                setFieldTouched(eventNameOriginalFieldPath, true);
              }}
            />
            <StringArrayField
              width={16}
              fieldPath={`${fieldPathPrefix}.eventNameAlternate`}
              {...getFieldData({
                fieldPath: `${fieldPathPrefix}.eventNameAlternate`,
                fieldRepresentation: "compact",
              })}
              addButtonLabel={i18next.t("Add event alternate name")}
            />
            <EDTFDaterangePicker
              fieldPath={`${fieldPathPrefix}.eventDate`}
              {...getFieldData({
                fieldPath: `${fieldPathPrefix}.eventDate`,
                icon: "calendar",
              })}
            />
            <GroupField>
              <TextField
                width={10}
                fieldPath={`${fieldPathPrefix}.eventLocation.place`}
                {...getFieldData({
                  fieldPath: `${fieldPathPrefix}.eventLocation.place`,
                  fieldRepresentation: "compact",
                })}
              />
              <LocalVocabularySelectField
                selectOnBlur={false}
                width={6}
                fieldPath={`${fieldPathPrefix}.eventLocation.country`}
                optionsListName="countries"
                clearable
                {...getFieldData({
                  fieldPath: `${fieldPathPrefix}.eventLocation.country`,
                  fieldRepresentation: "compact",
                })}
              />
            </GroupField>
            {eventLocationError && (
              <React.Fragment>
                <Label className="rel-mb-1 mt-0 ml-5" prompt pointing="above">
                  {eventLocationError.messages.join(" ")}
                </Label>
                <br />
              </React.Fragment>
            )}
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

EventsField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
