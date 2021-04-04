import axios from "axios";
import { useState } from "react";
import { HTTP_METHOD } from "../types/httpMethod";
import { IApiError } from "../types/apiError";
import ErrorMessage from "../components/ErrorMessage";

const methodToAxios = (method: HTTP_METHOD) => {
  switch (method) {
    case HTTP_METHOD.GET:
      return axios.get;
    case HTTP_METHOD.POST:
      return axios.post;
    case HTTP_METHOD.PUT:
      return axios.put;
    case HTTP_METHOD.PATCH:
      return axios.patch;
    case HTTP_METHOD.DELTE:
      return axios.delete;
    default:
      return axios.get;
  }
};

export const useRequest = ({
  url,
  method,
  body,
  onSuccess,
}: {
  url: string;
  method: HTTP_METHOD;
  body?: any;
  onSuccess?: (data: any) => void;
}) => {
  const [apiErrors, setApiErrors] = useState<JSX.Element | null>(null);

  const doRequest = async (body?: any) => {
    try {
      setApiErrors(null);
      const req = methodToAxios(method);
      const response = await req(url, body);
      // callback
      onSuccess && onSuccess(response.data);
      return response.data;
    } catch (error) {
      setApiErrors(
        <ErrorMessage>
          {error.response.data.errors.map((err: IApiError, index: number) => (
            <li key={`${error.message}-${index}`}>{err.message}</li>
          ))}
        </ErrorMessage>
      );

      //throw error;
    }
  };

  return { doRequest, apiErrors };
};
