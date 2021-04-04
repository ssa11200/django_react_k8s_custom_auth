import React, { FunctionComponent } from "react";
import { Message } from "semantic-ui-react";

interface IErrorMessageProps {
  message?: string;
  header?: string;
}

const ErrorMessage: FunctionComponent<IErrorMessageProps> = ({
  header,
  message,
  children,
}) => (
  <Message negative>
    {header && <Message.Header>{header}</Message.Header>}
    {message && <p>{message}</p>}
    {children}
  </Message>
);

export default ErrorMessage;
