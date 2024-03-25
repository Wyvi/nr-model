// This file is part of React-Invenio-Deposit
// Copyright (C) 2021 CERN.
// Copyright (C) 2021-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// React-Invenio-Deposit is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import { Button, Item } from "semantic-ui-react";
import _truncate from "lodash/truncate";
import { LicenseModal } from "./LicenseModal";
import { i18next } from "@translations/i18next";
import PropTypes from "prop-types";
import { useFormikContext } from "formik";
import { getTitleFromMultilingualObject } from "@js/oarepo_ui";

export const LicenseFieldItem = ({
  license,
  searchConfig,
  serializeLicenses,
  handleLicenseChange,
  fieldPath,
}) => {
  const { setFieldValue } = useFormikContext();
  console.log(license);
  return (
    <div className="flex" key={license.key}>
      <div>{getTitleFromMultilingualObject(license.title)}</div>
      <LicenseModal
        searchConfig={searchConfig}
        handleLicenseChange={handleLicenseChange}
        mode={license.type}
        initialLicense={license.initial}
        action="edit"
        trigger={
          <Button size="mini" primary type="button">
            {i18next.t("Edit")}
          </Button>
        }
        serializeLicenses={serializeLicenses}
      />
      <Button
        size="mini"
        type="button"
        onClick={() => {
          setFieldValue(fieldPath, "");
        }}
      >
        {i18next.t("Remove")}
      </Button>
    </div>
  );
};

LicenseFieldItem.propTypes = {
  license: PropTypes.object.isRequired,
  searchConfig: PropTypes.object.isRequired,
  serializeLicenses: PropTypes.func,
};

LicenseFieldItem.defaultProps = {
  serializeLicenses: undefined,
};
