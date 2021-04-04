import Signin from "../components/Signin";
import Layout from "../components/Layout/Layout";
import { NextPageContext } from "next";
import buildClient from "../api/buildClient";

const SigninPage = () => {
  return (
    <Layout
      backgroundImageUrl={
        "https://images.unsplash.com/photo-1544027993-37dbfe43562a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
      }
    >
      <Signin />
    </Layout>
  );
};
SigninPage.getInitialProps = async (context: NextPageContext) => {
  // build preconfigured axios instance depending on whether we are running on the server or in the browser
  const axiosClient = buildClient(context);
  const { data } = await axiosClient.get("/api/users/currentuser/");
  const { currentUser } = data;
  if (currentUser && typeof window === "undefined" && context?.res) {
    context.res.writeHead(302, { location: "/dashboard" });
    context.res.end();
  }
  return data;
};

export default SigninPage;
