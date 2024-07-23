import React from "react";
import PropTypes from "prop-types";
import { TextField, GroupField } from "react-invenio-forms";
import { Form } from "semantic-ui-react";
import { useFieldData } from "@js/oarepo_ui";

export const ExternalLocationField = ({ fieldPath }) => {
  const { getFieldData } = useFieldData();

  const { label, helpText } = getFieldData(fieldPath).fullRepresentation;
  return (
    <Form.Field>
      {label}
      <GroupField>
        <TextField
          width={8}
          fieldPath={`${fieldPath}.externalLocationURL`}
          {...getFieldData(`${fieldPath}.externalLocationURL`)
            .compactRepresentation}
        />
        <TextField
          width={8}
          fieldPath={`${fieldPath}.externalLocationNote`}
          {...getFieldData(`${fieldPath}.externalLocationNote`)
            .compactRepresentation}
        />
      </GroupField>
      {helpText && <label className="helptext">{helpText}</label>}
    </Form.Field>
  );
};

ExternalLocationField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
