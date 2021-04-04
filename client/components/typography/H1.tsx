import styled from "styled-components";

export const H1 = styled.h1`
  margin: 0;
  margin-bottom: 15px;
  font-size: 24px;
  @media (min-width: ${(props) => props.theme.tabletBreakpoint}) {
    font-size: 36px;
  }
`;
