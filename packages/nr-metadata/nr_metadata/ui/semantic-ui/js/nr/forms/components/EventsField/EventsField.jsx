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
import { useFormikContext, getIn } from "formik";

export const EventsField = ({ fieldPath }) => {
  const { values, setFieldValue, setFieldTouched } = useFormikContext();

  const { sanitizeInput } = useSanitizeInput();
  const { getFieldData } = useFieldData();
  return (
    <ArrayField
      fieldPath={fieldPath}
      {...getFieldData({ fieldPath }).fullRepresentation}
      addButtonClassName="array-field-add-button"
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        const eventNameOriginalFieldPath = `${fieldPathPrefix}.eventNameOriginal`;

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
              {...getFieldData({ fieldPath: eventNameOriginalFieldPath })
                .compactRepresentation}
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
              }).compactRepresentation}
            />
            <EDTFDaterangePicker
              fieldPath={`${fieldPathPrefix}.eventDate`}
              {...getFieldData({
                fieldPath: `${fieldPathPrefix}.eventDate`,
                icon: "calendar",
              }).fullRepresentation}
            />
            <GroupField>
              <TextField
                width={10}
                fieldPath={`${fieldPathPrefix}.eventLocation.place`}
                {...getFieldData({
                  fieldPath: `${fieldPathPrefix}.eventLocation.place`,
                }).compactRepresentation}
              />
              <LocalVocabularySelectField
                selectOnBlur={false}
                width={6}
                fieldPath={`${fieldPathPrefix}.eventLocation.country`}
                optionsListName="countries"
                clearable
                {...getFieldData({
                  fieldPath: `${fieldPathPrefix}.eventLocation.country`,
                }).compactRepresentation}
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
};
