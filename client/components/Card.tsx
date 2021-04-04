import styled, { css } from "styled-components";

interface ICardProps {
  isTextCentered?: boolean;
  hasBoxShadow?: boolean;
}

export const Card = styled.div<ICardProps>`
  padding: 30px;
  border-radius: 4px;
  background: white;
  ${(props) =>
    props.isTextCentered &&
    css`
      text-align: center;
    `}
  ${(props) =>
    props.hasBoxShadow &&
    css`
      box-shadow: ${props.theme.boxShadow};
    `}
`;
