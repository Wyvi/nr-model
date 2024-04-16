// This file is part of React-Invenio-Deposit
// Copyright (C) 2021 CERN.
// Copyright (C) 2021-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// React-Invenio-Deposit is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import { Button, Grid, Image } from "semantic-ui-react";
import { i18next } from "@translations/nr/i18next";
import PropTypes from "prop-types";
import { useFormikContext } from "formik";
import { useFormConfig } from "@js/oarepo_ui";

export const LicenseFieldItem = ({ license, fieldPath }) => {
  const { setFieldValue } = useFormikContext();
  const {
    formConfig: {
      vocabularies: {
        rights: { all },
      },
    },
  } = useFormConfig();
  const licenseUI = all.find((r) => r.value === license.id);

  return (
    <Grid key={license.key}>
      <Grid.Row only="computer tablet" verticalAlign="middle">
        <Grid.Column stretched width={2}>
          <Image src={licenseUI.icon} size="tiny" />
        </Grid.Column>
        <Grid.Column stretched width={10}>
          {licenseUI.text}
        </Grid.Column>
        <Grid.Column stretched textAlign="right" width={4}>
          <Button
            size="mini"
            type="button"
            onClick={() => {
              setFieldValue(fieldPath, "");
            }}
          >
            {i18next.t("Remove")}
          </Button>
        </Grid.Column>
      </Grid.Row>
      <Grid.Row only="mobile" verticalAlign="middle">
        <Grid.Column width={8}>
          <Image src={licenseUI.icon} size="tiny" />
        </Grid.Column>
        <Grid.Column textAlign="right" width={8}>
          <Button
            size="mini"
            type="button"
            onClick={() => {
              setFieldValue(fieldPath, "");
            }}
          >
            {i18next.t("Remove")}
          </Button>
        </Grid.Column>
      </Grid.Row>
      <Grid.Row only="mobile" verticalAlign="middle">
        <Grid.Column>{licenseUI.text}</Grid.Column>
      </Grid.Row>
    </Grid>
  );
};

LicenseFieldItem.propTypes = {
  license: PropTypes.object.isRequired,
  fieldPath: PropTypes.string.isRequired,
};
