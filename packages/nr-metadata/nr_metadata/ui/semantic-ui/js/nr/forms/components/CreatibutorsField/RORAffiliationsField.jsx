import * as React from "react";

import { RORInstitutionResult } from "../RORInstitutionResult";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { Button, Icon } from "semantic-ui-react";
import { useFieldData } from "@js/oarepo_ui";
import { i18next } from "@translations/nr/i18next";

export const RORAffiliationsField = ({
  fieldPath,
  multiple = false,
  ...rest
}) => {
  const { getFieldData } = useFieldData();

  return (
    <VocabularyRemoteSelectField
      overriddenComponents={{
        "VocabularyRemoteSelect.ext.ResultsList.item": RORInstitutionResult,
      }}
      vocabulary="institutions"
      multiple={multiple}
      fieldPath={fieldPath}
      modalHeader={
        getFieldData({
          fieldPath: fieldPath,
          fieldRepresentation: "text",
        }).label
      }
      closeOnDimmerClick={true}
      triggerButton={
        <Button
          className="array-field-add-button"
          type="button"
          icon
          labelPosition="left"
        >
          <Icon name="add" />
          {i18next.t(`Choose affiliation${multiple ? "s" : ""}`)}
        </Button>
      }
      {...getFieldData({
        fieldPath: fieldPath,
      })}
      {...rest}
    />
  );
};
