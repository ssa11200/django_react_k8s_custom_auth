import styled, { css } from "styled-components";

interface IPageWrapperProps {
  isCenteringDisabled?: boolean;
  backgroundImageUrl?: string;
  backgroundColor?: string;
}

export const PageWrapper = styled.div<IPageWrapperProps>`
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  width: 100vw;
  ${(props) =>
    !props.isCenteringDisabled &&
    css`
      justify-content: center;
      align-items: center;
    `}

  

  ${(props) =>
    props.backgroundImageUrl &&
    css`
      background-image: url(${props.backgroundImageUrl});
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
    `}

  background-color: ${(props) => props.backgroundColor || "white"};
  padding: 0;
`;
