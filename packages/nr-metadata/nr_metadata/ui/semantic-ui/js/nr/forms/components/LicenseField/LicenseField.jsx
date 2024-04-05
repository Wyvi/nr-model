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
import { FieldLabel } from "react-invenio-forms";
import { Button, Form, Icon } from "semantic-ui-react";
import { LicenseModal } from "./LicenseModal";
import { LicenseFieldItem } from "./LicenseFieldItem";
import { i18next } from "@translations/i18next";

export const visibleLicense = ({ id, title }) => ({ id, title: title });

export const LicenseField = ({
  label,
  labelIcon,
  fieldPath,
  required,
  searchConfig,
  serializeLicenses,
  helpText,
}) => {
  const { values, setFieldValue } = useFormikContext();
  let licenseUI;
  const license = getIn(values, fieldPath, {})?.id
    ? getIn(values, fieldPath, {})
    : "";
  if (license) {
    licenseUI = new visibleLicense(license);
  }
  const handleLicenseChange = (selectedLicense) => {
    setFieldValue(fieldPath, selectedLicense);
  };
  return (
    <Form.Field required={required}>
      <FieldLabel htmlFor={fieldPath} icon={labelIcon} label={label} />
      <label className="helptext">{helpText}</label>
      {license && (
        <LicenseFieldItem
          key={license.id}
          license={licenseUI}
          searchConfig={searchConfig}
          serializeLicenses={serializeLicenses}
          handleLicenseChange={handleLicenseChange}
          fieldPath={fieldPath}
        />
      )}
      <LicenseModal
        searchConfig={searchConfig}
        initialLicense={licenseUI}
        trigger={
          <Button type="button" key="license" icon labelPosition="left">
            <Icon name="add" />
            {i18next.t("Choose license")}
          </Button>
        }
        handleLicenseChange={handleLicenseChange}
        serializeLicenses={serializeLicenses}
      />
    </Form.Field>
  );
};

LicenseField.propTypes = {
  label: PropTypes.string,
  labelIcon: PropTypes.string,
  fieldPath: PropTypes.string.isRequired,
  required: PropTypes.bool,
  searchConfig: PropTypes.object.isRequired,
  serializeLicenses: PropTypes.func,
  helpText: PropTypes.string,
};

LicenseField.defaultProps = {
  labelIcon: "drivers license",
  label: i18next.t("License"),
  serializeLicenses: undefined,
  required: false,
  helpText: i18next.t(
    "If a Creative Commons license is associated with the resource, select the appropriate license option from the menu. We recommend choosing the latest versions, namely 3.0 Czech and 4.0 International."
  ),
};
