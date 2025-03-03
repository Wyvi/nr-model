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
  addButtonLabel,
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
      fieldPath={fieldPath}
      className="additional-titles"
      {...getFieldData({ fieldPath, fieldRepresentation: "text" })}
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
              />
            </Form.Field>
            <Form.Field width={4}>
              <SelectField
                selectOnBlur={false}
                fieldPath={`${fieldPathPrefix}.titleType`}
                optimized
                options={subtitleTypes}
                clearable
                id={`${fieldPathPrefix}.titleType`}
                width={16}
                {...getFieldData({
                  fieldPath: `${fieldPathPrefix}.titleType`,
                  fieldRepresentation: "compact",
                })}
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
  addButtonLabel: i18next.t("Add additional title"),
};
