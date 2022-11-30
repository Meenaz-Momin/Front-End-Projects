import { toast } from "react-toastify";
export function extractError(error) {
  return toast.error(
    error.response?.data?.message || error.message || error.toString()
  );
}
