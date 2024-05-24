import React from "react";
import PropTypes from "prop-types";
import { ArrayField, TextField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import { LocalVocabularySelectField } from "@js/oarepo_vocabularies";
import { ArrayFieldItem, useFormConfig } from "@js/oarepo_ui";

export const FundersField = ({
  fieldPath,
  helpText,
  useModelData,
  addButtonLabel,
  label,
  projectIDLabel,
  projectIDPlaceholder,
  projectNameLabel,
  projectNamePlaceholder,
  fundingProgramLabel,
  fundingProgramPlaceholder,
  funderLabel,
  funderPlaceholder,
}) => {
  const {
    formConfig: { getFieldData },
  } = useFormConfig();

  return (
    <ArrayField
      addButtonLabel={addButtonLabel}
      defaultNewValue={{}}
      fieldPath={fieldPath}
      label={label}
      helpText={helpText}
      {...(useModelData ? getFieldData(fieldPath).fullRepresentation : {})}
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        return (
          <ArrayFieldItem
            indexPath={indexPath}
            arrayHelpers={arrayHelpers}
            style={{ display: "block" }}
          >
            <TextField
              width={16}
              fieldPath={`${fieldPathPrefix}.projectID`}
              label={projectIDLabel}
              placeholder={projectIDPlaceholder}
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.projectID`)
                    .compactRepresentation
                : {})}
            />
            <TextField
              className="rel-mt-1"
              width={16}
              fieldPath={`${fieldPathPrefix}.projectName`}
              label={projectNameLabel}
              placeholder={projectNamePlaceholder}
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.projectName`)
                    .compactRepresentation
                : {})}
            />
            <TextField
              className="rel-mt-1"
              width={16}
              fieldPath={`${fieldPathPrefix}.fundingProgram`}
              label={fundingProgramLabel}
              placeholder={fundingProgramPlaceholder}
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.fundingProgram`)
                    .compactRepresentation
                : {})}
            />
            <LocalVocabularySelectField
              className="rel-mt-1"
              width={16}
              fieldPath={`${fieldPathPrefix}.funder`}
              label={funderLabel}
              optionsListName="funders"
              clearable
              required
              placeholder={funderPlaceholder}
              {...(useModelData
                ? getFieldData(`${fieldPathPrefix}.funder`)
                    .compactRepresentation
                : {})}
            />
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

FundersField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  helpText: PropTypes.string,
  useModelData: PropTypes.bool,
  addButtonLabel: PropTypes.string,
  label: PropTypes.string,
  projectIDLabel: PropTypes.string,
  projectIDPlaceholder: PropTypes.string,
  projectNameLabel: PropTypes.string,
  projectNamePlaceholder: PropTypes.string,
  fundingProgramLabel: PropTypes.string,
  fundingProgramPlaceholder: PropTypes.string,
  funderLabel: PropTypes.string,
  funderPlaceholder: PropTypes.string,
};

FundersField.defaultProps = {
  useModelData: true,
  addButtonLabel: i18next.t("Add funder"),
  label: i18next.t("Funding"),
  projectIDLabel: i18next.t("Project code"),
  projectIDPlaceholder: i18next.t("Write down project number."),
  projectNameLabel: i18next.t("Project name"),
  projectNamePlaceholder: i18next.t("Write down name of project."),
  fundingProgramLabel: i18next.t("Funding program"),
  fundingProgramPlaceholder: i18next.t(
    "Write the name of research program in which the project was funded."
  ),
  funderLabel: i18next.t("Funder"),
  funderPlaceholder: i18next.t(
    "Start writing the name of the provider and then choose from the list."
  ),
};
