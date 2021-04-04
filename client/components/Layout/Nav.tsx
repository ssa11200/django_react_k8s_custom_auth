import React from "react";
import styled from "styled-components";
import { useRouter } from "next/dist/client/router";
import { useAuthContext } from "../../context/AuthContext";
import Link from "next/link";

const Spacer = styled.div`
  height: ${(props) => props.theme.navHeight};
  min-height: ${(props) => props.theme.navHeight};
`;

const Wrapper = styled.div`
  z-index: 1;
  height: ${(props) => props.theme.navHeight};
  position: fixed;
  top: 0px;
  right: 0px;
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  min-width: 300px;
  box-shadow: ${(props) => props.theme.boxShadow};
  background: white;
`;

const Brand = styled.div`
  font-size: 18px;
  margin: auto 0;
  opacity: 0.9;
  cursor: pointer;

  @media (min-width: ${(props) => props.theme.tabletBreakpoint}) {
    font-size: 24px;
  }
`;

const A = styled.a`
  cursor: pointer;
`;

interface INavProps {
  openMenu: () => void;
}

const CustomNav = ({ openMenu }: INavProps) => {
  const router = useRouter();
  const { currentUser, signout } = useAuthContext();

  return (
    <Spacer id="navbar">
      <Wrapper>
        <Brand
          onClick={() => {
            const endpoint = currentUser ? "/dashboard" : "/";
            router.push(endpoint);
          }}
        >
          Test app
        </Brand>

        {!currentUser && (
          <Link href={"/signin"}>
            <A>Log in</A>
          </Link>
        )}

        {currentUser && <A onClick={signout}>Log out</A>}
      </Wrapper>
    </Spacer>
  );
};

export default CustomNav;
