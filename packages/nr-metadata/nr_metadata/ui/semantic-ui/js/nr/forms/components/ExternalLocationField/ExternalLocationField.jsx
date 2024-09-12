import React from "react";
import PropTypes from "prop-types";
import { TextField, GroupField } from "react-invenio-forms";
import { Form, Icon } from "semantic-ui-react";
import { useFieldData } from "@js/oarepo_ui";
import { i18next } from "@translations/nr/i18next";
import { useFormikContext, getIn } from "formik";

export const ExternalLocationField = ({ fieldPath }) => {
  const { getFieldData } = useFieldData();
  const { values } = useFormikContext();
  const fieldValue = getIn(values, fieldPath, {});

  const hasValue = Object.values(fieldValue).some((v) => v);

  const [showInput, setShowInput] = React.useState(hasValue);

  const { label, helpText } = getFieldData({ fieldPath });
  return (
    <Form.Field>
      {label}
      {showInput && (
        <GroupField>
          <TextField
            width={8}
            fieldPath={`${fieldPath}.externalLocationURL`}
            {...getFieldData({
              fieldPath: `${fieldPath}.externalLocationURL`,
              fieldRepresentation: "compact",
            })}
          />
          <TextField
            width={8}
            fieldPath={`${fieldPath}.externalLocationNote`}
            {...getFieldData({
              fieldPath: `${fieldPath}.externalLocationNote`,
              fieldRepresentation: "compact",
            })}
          />
        </GroupField>
      )}
      {helpText && <label className="helptext">{helpText}</label>}
      {!showInput && (
        <Form.Button
          type="button"
          icon
          className={"array-field-add-button"}
          labelPosition="left"
          onClick={() => {
            setShowInput(true);
          }}
        >
          <Icon name="add" />
          {i18next.t("Add external location")}
        </Form.Button>
      )}
    </Form.Field>
  );
};

ExternalLocationField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
