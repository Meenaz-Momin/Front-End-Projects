import { Box } from "@mui/material";
import PostList from "./PostList";
import { useSelector, useDispatch } from "react-redux";
import { useEffect } from "react";
import { toast } from "react-toastify";
import { getAllPost } from "../features/post/postSlice";

export const Feed = () => {
  const dispatch = useDispatch();
  const { allPost } = useSelector((state) => state.post);

  useEffect(() => {
    dispatch(getAllPost()).unwrap().catch(toast.error);
  }, [dispatch]);

  return (
    <Box flex={4}>
      {!allPost ? (
        <>
          <h3>No Posts Yet</h3>
        </>
      ) : (
        <>
          <PostList post={allPost} />
        </>
      )}
    </Box>
  );
};
