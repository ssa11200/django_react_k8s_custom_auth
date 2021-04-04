import { NextPage, NextPageContext } from "next";
import buildClient from "../api/buildClient";
import { IUser } from "../types/IUser";
import Layout from "../components/Layout/Layout";

interface IDashboardPageProps {
  currentUser: IUser | null;
}

const DashboardPage: NextPage<IDashboardPageProps> = ({ currentUser }) => {
  return (
    <Layout backgroundColor="whitesmoke">{`${currentUser?.name} signed in`}</Layout>
  );
};

DashboardPage.getInitialProps = async (context: NextPageContext) => {
  // build preconfigured axios instance depending on whether we are running on the server or in the browser
  const axiosClient = buildClient(context);
  const { data } = await axiosClient.get("/api/users/currentuser/");
  if (
    data.currentUser === null &&
    typeof window === "undefined" &&
    context?.res
  ) {
    context.res.writeHead(302, { location: "/signin" });
    context.res.end();
  }
  return data;
};

export default DashboardPage;
