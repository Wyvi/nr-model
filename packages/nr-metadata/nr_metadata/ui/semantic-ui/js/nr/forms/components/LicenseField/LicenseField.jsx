// This file is part of React-Invenio-Deposit
// Copyright (C) 2020-2021 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// React-Invenio-Deposit is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Button, Form, Icon } from "semantic-ui-react";
import { LicenseModal } from "./LicenseModal";
import { LicenseFieldItem } from "./LicenseFieldItem";
import { i18next } from "@translations/nr/i18next";
import { useFormConfig } from "@js/oarepo_ui";

export const LicenseField = ({
  label,
  fieldPath,
  required,
  searchConfig,
  serializeLicense,
  helpText,
}) => {
  const {
    formConfig: { getFieldData },
  } = useFormConfig();
  const {
    label: modelLabel,
    helpText: modelHelpText,
    required: modelRequired,
  } = getFieldData(fieldPath, "drivers license").fullRepresentation;
  const { values, setFieldValue } = useFormikContext();
  const license = getIn(values, fieldPath, {})?.id
    ? getIn(values, fieldPath, {})
    : "";
  const handleLicenseChange = (selectedLicense) => {
    setFieldValue(fieldPath, { id: selectedLicense.id });
  };
  return (
    <Form.Field required={required ?? modelRequired}>
      {label ?? modelLabel}
      <label className="helptext">{helpText ?? modelHelpText}</label>
      {license && (
        <LicenseFieldItem
          key={license.id}
          license={license}
          fieldPath={fieldPath}
        />
      )}
      <LicenseModal
        searchConfig={searchConfig}
        initialLicense={license}
        trigger={
          <Button
            type="button"
            key="license"
            icon
            labelPosition="left"
            className="mt-10"
          >
            <Icon name="add" />
            {i18next.t("Choose license")}
          </Button>
        }
        handleLicenseChange={handleLicenseChange}
        serializeLicense={serializeLicense}
      />
    </Form.Field>
  );
};

LicenseField.propTypes = {
  label: PropTypes.string,
  fieldPath: PropTypes.string.isRequired,
  required: PropTypes.bool,
  searchConfig: PropTypes.object.isRequired,
  serializeLicense: PropTypes.func,
  helpText: PropTypes.string,
};

LicenseField.defaultProps = {
  label: i18next.t("License"),
  serializeLicense: undefined,
  required: false,
  helpText: i18next.t(
    "If a Creative Commons license is associated with the resource, select the appropriate license option from the menu. We recommend choosing the latest versions, namely 3.0 Czech and 4.0 International."
  ),
};
