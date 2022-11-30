import { Box, Stack } from "@mui/material";
import Navbar from "../components/Navbar";
import PostList from "../components/PostList";
import { useSelector, useDispatch } from "react-redux";
import { useEffect } from "react";
import { toast } from "react-toastify";
import { getMyPost } from "../features/post/postSlice";

function Profile() {
  const dispatch = useDispatch();
  const { myPost } = useSelector((state) => state.post);
  console.log({ myPost });
  useEffect(() => {
    dispatch(getMyPost()).unwrap().catch(toast.error);
  }, [dispatch]);
  return (
    <Box>
      <Navbar />
      {!myPost ? (
        <>
          <h4> No post Yet</h4>
        </>
      ) : (
        <>
          <Stack direction="row" spacing={2}>
            <PostList post={myPost} />
          </Stack>
        </>
      )}
    </Box>
  );
}

export default Profile;
