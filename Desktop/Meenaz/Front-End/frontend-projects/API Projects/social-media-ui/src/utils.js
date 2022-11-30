import { toast } from "react-toastify";
export function extractErrorMessage(error) {
  return toast.error(
    error.response?.data?.message || error.message || error.toString()
  );
}
