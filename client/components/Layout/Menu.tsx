import React from "react";
import styled from "styled-components";
import { useAuthContext } from "../../context/AuthContext";

interface IMenuWrapperProps {
  isVisible: boolean;
}

const MenuItem = styled.li`
  color: white;
  font-size: 24px;
  list-style-type: none;
`;

const MenuWrapper = styled.div<IMenuWrapperProps>`
  z-index: 100;
  position: fixed;
  width: 100vw;
  height: 100vh;
  top: -100vh;
  right: 0;
  background: #727070;
  ${(props) =>
    props.isVisible
      ? `transform: translateY(100vh);`
      : `transform: translateY(-100vh);`}
  transition: all 0.8s cubic-bezier(0, 1, 0.8, 1);
  display: flex;
  justify-content: center;
`;

const Content = styled.div`
  max-width: 400px;
  width: 100%;
  padding: 20px;
  display: grid;
  grid-gap: 15px;
  grid-auto-rows: max-content;
`;

interface IMenuProps {
  isVisible: boolean;
  handleClose: () => void;
}

const Menu = ({ isVisible, handleClose }: IMenuProps) => {
  const { signout, currentUser } = useAuthContext();
  return (
    <MenuWrapper isVisible={isVisible}>
      <Content>
        <button onClick={handleClose}>Close</button>

        <MenuItem
          onClick={() => {
            signout();
          }}
        >
          Sign Out
        </MenuItem>
      </Content>
    </MenuWrapper>
  );
};

export default Menu;
