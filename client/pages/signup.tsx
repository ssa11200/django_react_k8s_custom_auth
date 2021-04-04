import Signup from "../components/Signup";
import Layout from "../components/Layout/Layout";
import buildClient from "../api/buildClient";
import { NextPageContext } from "next";

const SignupPage = () => {
  return (
    <Layout
      backgroundImageUrl={
        "https://images.unsplash.com/photo-1544027993-37dbfe43562a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
      }
    >
      <Signup />
    </Layout>
  );
};

SignupPage.getInitialProps = async (ctx: NextPageContext) => {
  // build preconfigured axios instance depending on whether we are running on the server or in the browser
  const axiosClient = buildClient(ctx);
  const { data } = await axiosClient.get("/api/users/currentuser/");
  const { currentUser } = data;
  //it is annoying that first the signup page is fully loaded and then redirected to dashboard page in cases of page refresh, is it ok to do it David?
  if (currentUser && typeof window === "undefined" && ctx?.res) {
    ctx.res.writeHead(302, { location: "/dashboard" });
    ctx.res.end();
  }
  return data;
};

export default SignupPage;
