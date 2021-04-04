import React from "react";
import { Form, Input, Button } from "semantic-ui-react";
import styled from "styled-components";
import * as Yup from "yup";
import { useFormik } from "formik";
import { Card } from "./Card";
import { useRequest } from "../hooks/useRequest";
import { HTTP_METHOD } from "../types/httpMethod";
import { useRouter } from "next/router";
import { FadeIn } from "./FadeIn";
import ErrorMessage from "./ErrorMessage";

const H2 = styled.h2`
  margin-bottom: 20px;
  text-align: center;
`;

const P = styled.p`
  text-align: center;
  margin: 10px 0px 0px 0px;
`;

const A = styled.a`
  cursor: pointer;
  text-decoration: underline;
`;

const ButtonWrapper = styled.div`
  text-align: center;
`;

const validationSchema = Yup.object({
  email: Yup.string().required("Email is required"),
  password: Yup.string()
    .required("Password is required")
    .min(5, "Password should be at least 5 characters long"),
});

const Signin = () => {
  const router = useRouter();

  const onSubmit = async () => {
    await doRequest({
      email: values.email,
      password: values.password,
    });
  };

  const {
    values,
    errors,
    touched,
    handleBlur,
    handleChange,
    handleSubmit,
  } = useFormik({
    validationSchema,
    initialValues: {
      email: "",
      password: "",
    },
    onSubmit,
  });

  const { doRequest, apiErrors } = useRequest({
    url: "/api/users/signin/",
    method: HTTP_METHOD.POST,
    onSuccess: () => router.push("/dashboard"),
  });

  return (
    <FadeIn>
      <Card>
        <H2>Log In</H2>
        <Form onSubmit={handleSubmit}>
          <Form.Field>
            <Input
              placeholder="Email"
              name="email"
              value={values.email}
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Field>
          {touched.email && errors.email && (
            <ErrorMessage message={errors.email} />
          )}

          <Form.Field>
            <Input
              type="password"
              placeholder="Password"
              name="password"
              value={values.password}
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Field>
          {touched.password && errors.password && (
            <ErrorMessage message={errors.password} />
          )}
          <ButtonWrapper>
            <Button color="blue" type="submit" style={{ marginBottom: "10px" }}>
              Submit
            </Button>
          </ButtonWrapper>
          {apiErrors}
          <P>
            Don't have an account? Click{" "}
            <A
              className="text-primary"
              onClick={() => {
                router.push("/signup");
              }}
            >
              here
            </A>{" "}
            to sign up
          </P>
        </Form>
      </Card>
    </FadeIn>
  );
};

export default Signin;
