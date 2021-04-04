import styled, { css } from "styled-components";

interface IButtonProps {
  isUpperCase?: boolean;
  isFullWidth?: boolean;
}
export const Button = styled.button<IButtonProps>`
  @media (min-width: ${(props) => props.theme.tabletBreakpoint}) {
    padding: 25px;
  }
  background-color: #101a3f;
  color: white;
  border-radius: 6px;
  padding: 15px;
  ${(props) =>
    props.isFullWidth &&
    css`
      width: 100%;
    `}
  ${(props) =>
    props.isUpperCase &&
    css`
      text-transform: uppercase;
    `}
`;
