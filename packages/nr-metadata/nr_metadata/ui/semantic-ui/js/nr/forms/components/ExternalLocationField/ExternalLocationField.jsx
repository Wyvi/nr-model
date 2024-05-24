import React from "react";
import PropTypes from "prop-types";
import { TextField, GroupField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import { Form } from "semantic-ui-react";
import { useFormConfig } from "@js/oarepo_ui";

export const ExternalLocationField = ({
  fieldPath,
  label,
  helpText,
  externalLocationUrlLabel,
  externalLocationNoteLabel,
  useModelData,
}) => {
  const {
    formConfig: { getFieldData },
  } = useFormConfig();
  const { label: modelFieldLabel, helpText: modelHelpText } =
    getFieldData(fieldPath).fullRepresentation;
  return (
    <Form.Field>
      {label ?? modelFieldLabel}
      <GroupField>
        <TextField
          width={8}
          fieldPath={`${fieldPath}.externalLocationURL`}
          label={externalLocationUrlLabel}
          {...(useModelData
            ? getFieldData(`${fieldPath}.externalLocationURL`)
                .compactRepresentation
            : {})}
        />
        <TextField
          width={8}
          fieldPath={`${fieldPath}.externalLocationNote`}
          label={externalLocationNoteLabel}
          {...(useModelData
            ? getFieldData(`${fieldPath}.externalLocationNote`)
                .compactRepresentation
            : {})}
        />
      </GroupField>
      <label className="helptext">{helpText ?? modelHelpText}</label>
    </Form.Field>
  );
};

ExternalLocationField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  helpText: PropTypes.string,
  label: PropTypes.node,
  externalLocationUrlLabel: PropTypes.string,
  externalLocationNoteLabel: PropTypes.string,
  useModelData: PropTypes.bool,
};

ExternalLocationField.defaultProps = {
  externalLocationUrlLabel: i18next.t("Resource external location"),
  externalLocationNoteLabel: i18next.t("Note"),
  useModelData: true,
};
