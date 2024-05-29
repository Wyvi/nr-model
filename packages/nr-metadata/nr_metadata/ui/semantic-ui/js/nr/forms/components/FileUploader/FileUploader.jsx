import React, { useState } from "react";
import PropTypes from "prop-types";
import { i18next } from "@translations/nr/i18next";
import { Message, Icon, Button } from "semantic-ui-react";
import { FileUploaderTable } from "./FileUploaderTable";
import { UploadFileButton } from "./FileUploaderButtons";
import { useDepositApiClient, useDepositFileApiClient } from "@js/oarepo_ui";
import { Trans } from "react-i18next";
import { useQuery } from "@tanstack/react-query";

export const FileUploader = ({
  messageContent,
  record,
  recordFiles,
  allowedFileTypes,
}) => {
  const [filesState, setFilesState] = useState(recordFiles?.entries || []);
  const { formik, isSubmitting, save, isSaving } = useDepositApiClient();
  const { read } = useDepositFileApiClient();
  const { values } = formik;
  // values.links.files =
  //   "https://127.0.0.1:5000/api/docs/x4cjy-2bf20/draft/filesddd";
  const draft = {
    links: {
      files: "https://127.0.0.1:5000/api/docs/x4cjy-2bf20/draft/filesddd",
    },
  };
  const { isFetching, isError, error, refetch } = useQuery(
    ["files"],
    () => read(draft),
    {
      refetchOnWindowFocus: false,
      enabled: false,
      onSuccess: (data) => {
        setFilesState(data.entries);
      },
    }
  );
  console.log(isError);
  console.log(error);

  const recordObject = record || values;

  const handleFilesUpload = () => {
    refetch();
  };
  const handleFileDeletion = (fileObject) => {
    const newFiles = filesState.filter((file) => file.key !== fileObject.key);
    setFilesState(newFiles);
  };

  return (
    <React.Fragment>
      {values.id ? (
        <React.Fragment>
          {recordObject?.files?.enabled &&
            (!isFetching ? (
              <React.Fragment>
                {isError ? (
                  <Message>
                    {i18next.t(
                      "Failed to fetch draft's files. Please try refreshing the page."
                    )}
                  </Message>
                ) : (
                  <FileUploaderTable
                    files={filesState}
                    handleFileDeletion={handleFileDeletion}
                    record={recordObject}
                    allowedFileTypes={allowedFileTypes}
                  />
                )}
                <UploadFileButton
                  record={recordObject}
                  handleFilesUpload={handleFilesUpload}
                  allowedFileTypes={allowedFileTypes}
                />
              </React.Fragment>
            ) : (
              <div className="flex justify-center align-items-center">
                <Icon name="spinner" loading size="huge" />
              </div>
            ))}
          <Message icon size="small">
            <Icon
              name="warning sign"
              size="mini"
              // style={{ fontSize: "1rem" }}
            />
            <Message.Content>{messageContent}</Message.Content>
          </Message>
        </React.Fragment>
      ) : (
        <Message>
          <Icon name="info circle" size="mini" style={{ fontSize: "1rem" }} />
          <Trans>
            If you wish to upload files, you must
            <Button
              className="ml-5 mr-5"
              primary
              onClick={() => save(true)}
              loading={isSaving}
              disabled={isSubmitting}
              size="mini"
            >
              save
            </Button>
            your draft first.
          </Trans>
        </Message>
      )}
    </React.Fragment>
  );
};

FileUploader.propTypes = {
  messageContent: PropTypes.string,
  record: PropTypes.object,
  recordFiles: PropTypes.object,
  allowedFileTypes: PropTypes.array,
};

FileUploader.defaultProps = {
  messageContent: i18next.t(
    "File addition, removal or modification are not allowed after you have published your draft."
  ),
  allowedFileTypes: ["*/*"],
};
