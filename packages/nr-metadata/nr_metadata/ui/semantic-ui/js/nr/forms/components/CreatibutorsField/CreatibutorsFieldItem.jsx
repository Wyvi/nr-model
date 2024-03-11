// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 New York University.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import { i18next } from "@translations/i18next";
import _get from "lodash/get";
import React from "react";
import { useDrag, useDrop } from "react-dnd";
import { Button, Label, List, Ref } from "semantic-ui-react";
import { CreatibutorsModal } from "./CreatibutorsModal";
import PropTypes from "prop-types";
import { useFormConfig } from "@js/oarepo_ui";

export const CreatibutorsFieldItem = ({
  compKey,
  identifiersError,
  index,
  replaceCreatibutor,
  removeCreatibutor,
  moveCreatibutor,
  addLabel,
  editLabel,
  initialCreatibutor,
  displayName,
  schema,
  autocompleteNames,
}) => {
  const dropRef = React.useRef(null);
  // eslint-disable-next-line no-unused-vars
  const [_, drag, preview] = useDrag({
    item: { index, type: "creatibutor" },
  });
  const [{ hidden }, drop] = useDrop({
    accept: "creatibutor",
    hover(item, monitor) {
      if (!dropRef.current) {
        return;
      }
      const dragIndex = item.index;
      const hoverIndex = index;

      // Don't replace items with themselves
      if (dragIndex === hoverIndex) {
        return;
      }

      if (monitor.isOver({ shallow: true })) {
        moveCreatibutor(dragIndex, hoverIndex);
        item.index = hoverIndex;
      }
    },
    collect: (monitor) => ({
      hidden: monitor.isOver({ shallow: true }),
    }),
  });

  const {
    formConfig: { vocabularies },
  } = useFormConfig();

  const renderRole = (role) => {
    return (
      role && (
        <Label size="tiny">
          {
            vocabularies["contributor-roles"].all.find(
              (item) => item.value === role.id
            ).text
          }
        </Label>
      )
    );
  };

  const firstError = identifiersError?.find(
    (elem) => ![undefined, null].includes(elem)
  );

  // Initialize the ref explicitely
  drop(dropRef);
  return (
    <Ref innerRef={dropRef} key={compKey}>
      <List.Item
        key={compKey}
        className={
          hidden ? "deposit-drag-listitem hidden" : "deposit-drag-listitem"
        }
      >
        <List.Content floated="right">
          <CreatibutorsModal
            addLabel={addLabel}
            editLabel={editLabel}
            onCreatibutorChange={(selectedCreatibutor) => {
              replaceCreatibutor(index, selectedCreatibutor);
            }}
            initialCreatibutor={initialCreatibutor}
            schema={schema}
            autocompleteNames={autocompleteNames}
            initialAction="edit"
            trigger={
              <Button size="mini" primary type="button">
                {i18next.t("Edit")}
              </Button>
            }
          />
          <Button
            size="mini"
            type="button"
            onClick={() => removeCreatibutor(index)}
          >
            {i18next.t("Remove")}
          </Button>
        </List.Content>
        <Ref innerRef={drag}>
          <List.Icon name="bars" className="drag-anchor" />
        </Ref>
        <Ref innerRef={preview}>
          <List.Content>
            <List.Description>
              <span className="creatibutor">
                {_get(initialCreatibutor, "authorityIdentifiers", []).some(
                  (identifier) => identifier.scheme === "orcid"
                ) && (
                  <img
                    alt="ORCID logo"
                    className="inline-id-icon mr-5"
                    src="/static/images/identifiers/orcid-og-image.png"
                    width="16"
                    height="16"
                  />
                )}
                {/* TODO: provide logo assets for this ID schemes */}
                {/* {_get(initialCreatibutor, "authorityIdentifiers", []).some(
                  (identifier) => identifier.scheme === "ror"
                ) && (
                  <img
                    alt="ROR logo"
                    className="inline-id-icon mr-5"
                    src="/static/images/ror-icon.svg"
                    width="16"
                    height="16"
                  />
                )}
                {_get(initialCreatibutor, "authorityIdentifiers", []).some(
                  (identifier) => identifier.scheme === "gnd"
                ) && (
                  <img
                    alt="GND logo"
                    className="inline-id-icon mr-5"
                    src="/static/images/gnd-icon.svg"
                    width="16"
                    height="16"
                  />
                )} */}
                {displayName} {renderRole(initialCreatibutor?.role)}
              </span>
            </List.Description>
            {firstError && (
              <Label pointing="left" prompt>
                {firstError.scheme ? firstError.scheme : "Invalid identifiers"}
              </Label>
            )}
          </List.Content>
        </Ref>
      </List.Item>
    </Ref>
  );
};

CreatibutorsFieldItem.propTypes = {
  compKey: PropTypes.string.isRequired,
  identifiersError: PropTypes.array,
  index: PropTypes.number.isRequired,
  replaceCreatibutor: PropTypes.func.isRequired,
  removeCreatibutor: PropTypes.func.isRequired,
  moveCreatibutor: PropTypes.func.isRequired,
  addLabel: PropTypes.node,
  editLabel: PropTypes.node,
  initialCreatibutor: PropTypes.object.isRequired,
  displayName: PropTypes.string,
  schema: PropTypes.string.isRequired,
  autocompleteNames: PropTypes.oneOfType([PropTypes.bool, PropTypes.string]),
};

CreatibutorsFieldItem.defaultProps = {
  identifiersError: undefined,
  addLabel: undefined,
  editLabel: undefined,
  displayName: undefined,
  autocompleteNames: undefined,
};
