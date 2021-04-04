import { NextPage, NextPageContext } from "next";
import buildClient from "../api/buildClient";
import { useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/router";
import Layout from "../components/Layout/Layout";
import { FadeIn } from "../components/FadeIn";
import { Card } from "../components/Card";
import { H1 } from "../components/typography/H1";
import { Button } from "semantic-ui-react";

interface IIndexPageProps {
  currentUser: { id: string; email: string } | null;
}

const IndexPage: NextPage<IIndexPageProps> = ({ currentUser }) => {
  const router = useRouter();

  useEffect(() => {
    if (currentUser) {
      router.push("/dashboard");
    }
  }, []);

  return (
    <Layout
      backgroundImageUrl={
        "https://images.unsplash.com/photo-1544027993-37dbfe43562a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
      }
    >
      <FadeIn>
        <Card isTextCentered>
          <H1>Welcome</H1>

          <Link href="/signup">
            <Button color="blue" size="huge">
              Sign Up
            </Button>
          </Link>
        </Card>
      </FadeIn>
    </Layout>
  );
};

IndexPage.getInitialProps = async (context: NextPageContext) => {
  // build preconfigured axios instance depending on whether we are running on the server or in the browser
  const axiosClient = buildClient(context);
  const { data } = await axiosClient.get("/api/users/currentuser/");
  return data;
};

export default IndexPage;
