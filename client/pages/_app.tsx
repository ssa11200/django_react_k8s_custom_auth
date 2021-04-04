import React from "react";
import { AppProps, AppContext } from "next/app";
import { createGlobalStyle, ThemeProvider } from "styled-components";
import buildClient from "../api/buildClient";
import { AuthProvider } from "../context/AuthContext";

export interface ITheme {
  [index: string]: string;
}

export interface IThemeWrapper {
  theme: ITheme;
}

export const theme: ITheme = {
  green: "#51ac2f",
  darkGreen: "#28710E",
  darkOffWhite: "#F0F0F0",
  offWhite: "#FFFFFF",
  darkGrey: "#686868",
  lightGrey: "#e0e1e2",
  smallMobileBreakpoin: "320px",
  largeMobileBreakpoint: "376px",
  tabletBreakpoint: "767px",
  smallDesktopBreakpoint: "1024px",
  fontFamily: "Roboto",
  bottomBarHeight: "70px",
  navHeight: "62px",
  maxContentWidth: "1440px",
  boxShadow: "-1px 2px 10px 2px rgba(0, 0, 0, 0.12)",
};

const GlobalStyle = createGlobalStyle<IThemeWrapper>`
  body {
    margin: 0 auto;
    padding: 0;
    color: ${(props) => props.theme.niceBlack}; 
  }
  html {
    box-sizing: border-box;
    padding: 0;
  }
  *, *:before, *:after {
    box-sizing: inherit;
  }
`;

const MyApp = ({ Component, pageProps }: AppProps) => {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <AuthProvider currentUser={pageProps.currentUser}>
        <Component {...pageProps} />
      </AuthProvider>
    </ThemeProvider>
  );
};

MyApp.getInitialProps = async ({ Component, ctx }: AppContext) => {
  // build preconfigured axios instance depending on whether we are running on the server or in the browser
  const axiosClient = buildClient(ctx);

  // fetch current user
  const { data } = await axiosClient.get("/api/users/currentuser/");

  // defining getInitialProps on a custom app component will mean that the getInitialProps of our pages does not run automatically
  // check if the page currently being rendered (the Component) has a getInitialProps function and if so, run it as well
  let pageProps: any = { currentUser: data.currentUser };

  if (Component.getInitialProps) {
    pageProps = { ...pageProps, ...(await Component?.getInitialProps(ctx)) };
  }

  // pass down query string
  pageProps.query = ctx.query;
  return { pageProps };
};

export default MyApp;
