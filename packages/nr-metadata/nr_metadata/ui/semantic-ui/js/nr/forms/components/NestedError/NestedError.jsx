import React from "react";
import { useFormikContext, getIn } from "formik";
import { Label } from "semantic-ui-react";
import { useFieldData } from "@js/oarepo_ui";
import PropTypes from "prop-types";

export const NestedError = ({ fieldPath, index }) => {
  const { errors } = useFormikContext();
  const beValidationErrors = getIn(errors, "BEvalidationErrors", {});
  const relatedItemErrorPaths = beValidationErrors?.errorPaths?.filter(
    (errorPath) => errorPath.startsWith(`${fieldPath}.${index}`)
  );

  const relatedItemErrors = relatedItemErrorPaths?.map((errorPath) => {
    return {
      errorMessage: getIn(errors, errorPath, ""),
      errorPath,
    };
  });
  const { getFieldData } = useFieldData();

  return (
    relatedItemErrors?.length > 0 &&
    relatedItemErrors.some((error) => Boolean(error.errorMessage)) && (
      <React.Fragment>
        <Label className="rel-mb-1 mt-0" prompt pointing="above">
          {relatedItemErrors.map(({ errorMessage, errorPath }, index) => (
            <p key={index}>{`${
              getFieldData({
                fieldPath: errorPath,
                fieldRepresentation: "text",
                ignorePrefix: true,
              }).label
            }: ${errorMessage}`}</p>
          ))}
        </Label>
        <br />
      </React.Fragment>
    )
  );
};

NestedError.propTypes = {
  fieldPath: PropTypes.string,
  index: PropTypes.number,
};
