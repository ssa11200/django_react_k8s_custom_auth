import React, { FunctionComponent, useState } from "react";
import styled from "styled-components";
import Nav from "./Nav";
import { PageWrapper } from "./PageWrapper";
import Menu from "./Menu";

const AppWrapper = styled.div`
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
`;
const BottomBarWrapper = styled.div`
  @media (min-width: 768px) {
    display: none;
  }
`;
interface ILayoutProps {
  isContentCenteringDisabled?: boolean;
  backgroundImageUrl?: string;
  backgroundColor?: string;
}

const Layout: FunctionComponent<ILayoutProps> = ({
  children,
  isContentCenteringDisabled,
  backgroundImageUrl,
  backgroundColor,
}) => {
  const [isMenuVisible, setIsMenuVisible] = useState(false);
  return (
    <AppWrapper>
      <Menu
        isVisible={isMenuVisible}
        handleClose={() => setIsMenuVisible(false)}
      />
      <Nav openMenu={() => setIsMenuVisible(true)} />
      <PageWrapper
        backgroundColor={backgroundColor}
        backgroundImageUrl={backgroundImageUrl}
        isCenteringDisabled={isContentCenteringDisabled}
      >
        {children}
      </PageWrapper>
    </AppWrapper>
  );
};

export default Layout;
