import React from "react";
import PropTypes from "prop-types";
import { Form } from "semantic-ui-react";
import { ArrayField, SelectField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import {
  I18nTextInputField,
  ArrayFieldItem,
  useDefaultLocale,
  useFormFieldValue,
  useFieldData,
} from "@js/oarepo_ui";

const subtitleTypes = [
  { text: i18next.t("Alternative title"), value: "alternativeTitle" },
  { text: i18next.t("Translated title"), value: "translatedTitle" },
  { text: i18next.t("Subtitle"), value: "subtitle" },
  { text: i18next.t("Other"), value: "other" },
];

export const AdditionalTitlesField = ({
  fieldPath,
  prefillLanguageWithDefaultLocale,
  defaultNewValue,
  label,
  required,
  addButtonLabel,
  helpText,
  useModelData,
}) => {
  const { getFieldData } = useFieldData();

  const { defaultLocale } = useDefaultLocale();
  const initialValueObj = {
    title: {
      value: "",
    },
  };
  const { defaultNewValue: getNewValue } = useFormFieldValue({
    defaultValue: defaultLocale,
    fieldPath,
    subValuesPath: "title.lang",
    subValuesUnique: false,
  });

  return (
    <ArrayField
      addButtonLabel={addButtonLabel}
      defaultNewValue={
        prefillLanguageWithDefaultLocale
          ? getNewValue(initialValueObj)
          : defaultNewValue
      }
      label={label}
      required={required}
      fieldPath={fieldPath}
      className="additional-titles"
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
            fieldPathPrefix={fieldPathPrefix}
          >
            <Form.Field width={12}>
              <I18nTextInputField
                fieldPath={`${fieldPathPrefix}.title`}
                lngFieldWidth={5}
                label={i18next.t("Title")}
                required
                {...(useModelData
                  ? getFieldData(`${fieldPathPrefix}.title`)
                      .compactRepresentation
                  : {})}
              />
            </Form.Field>
            <Form.Field width={4}>
              <SelectField
                selectOnBlur={false}
                fieldPath={`${fieldPathPrefix}.titleType`}
                label={
                  <label htmlFor={`${fieldPathPrefix}.titleType`}>
                    {i18next.t("Title type")}
                  </label>
                }
                required
                optimized
                options={subtitleTypes}
                clearable
                width={16}
                {...(useModelData
                  ? getFieldData(`${fieldPathPrefix}.titleType`)
                      .compactRepresentation
                  : {})}
              />
            </Form.Field>
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

AdditionalTitlesField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  prefillLanguageWithDefaultLocale: PropTypes.bool,
  defaultNewValue: PropTypes.object,
  addButtonLabel: PropTypes.string,
  label: PropTypes.string,
  required: PropTypes.bool,
  useModelData: PropTypes.bool,
  helpText: PropTypes.string,
};

AdditionalTitlesField.defaultProps = {
  prefillLanguageWithDefaultLocale: false,
  defaultNewValue: {
    title: {
      value: "",
      lang: "",
    },
    titleType: "",
  },
  label: i18next.t("Additional titles"),
  required: false,
  addButtonLabel: i18next.t("Add additional title"),
  useModelData: true,
};
