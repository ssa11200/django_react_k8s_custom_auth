import { IUser } from "../types/IUser";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export const useAuthRequirement = (currentUser: IUser | null) => {
  const router = useRouter();

  const [isAuthValid, setIsAuthValid] = useState(false);

  useEffect(() => {
    if (currentUser) {
      setIsAuthValid(true);
    } else {
      router.push("/");
    }
  }, []);

  return isAuthValid;
};
