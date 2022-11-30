import {
  Tooltip,
  Fab,
  Modal,
  styled,
  Box,
  Typography,
  Avatar,
  TextField,
  Button,
  Stack,
} from "@mui/material";
import { Add as AddIcon } from "@mui/icons-material";
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { createPost, getMyPost } from "../features/post/postSlice";
import { toast } from "react-toastify";

const StyledModal = styled(Modal)({
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
});

const UserBox = styled(Box)({
  display: "flex",
  alignItems: "center",
  marginBottom: "20px",
  gap: "10px",
});

export const Add = () => {
  const [open, setOpen] = useState(false);
  const [file, setFile] = useState();
  const [caption, setCaption] = useState("");
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { auth } = useSelector((state) => state.auth);

  const handleCaption = (e) => {
    setCaption(e.target.value);
  };

  const handleFile = (e) => {
    const newFile = Object?.value(e.target.files).map((item) => item);
    setFile(newFile);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("post_files", file[0]);
    formData.append("caption", caption);
    dispatch(createPost(formData))
      .unwrap()
      .then(() => {
        setOpen(false);
        toast.success("Post created successfully");
        dispatch(getMyPost());
        navigate("/");
      })
      .catch(toast.error);
  };

  return (
    <>
      <Tooltip
        title="Add Post"
        sx={{
          position: "fixed",
          bottom: 20,
          left: { xs: "calc(50% - 25px)", md: 30 },
        }}
        onClick={() => setOpen(true)}
      >
        <Fab color="primary" aria-label="add">
          <AddIcon />
        </Fab>
      </Tooltip>

      <StyledModal
        open={open}
        onClose={() => setOpen(false)}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box
          height={300}
          width={500}
          p={3}
          borderRadius={5}
          bgcolor={"background.default"}
          color={"text.primary"}
        >
          <Typography variant="h6" color="gray" textAlign="center">
            Create Post
          </Typography>
          <UserBox>
            <Avatar
              src="ht53005444-7446225ad957?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
              alt="profile"
            />
            <Typography variant="span">{auth.data.name}</Typography>
          </UserBox>
          <TextField
            sx={{ width: "100%", mb: "10px" }}
            id="standard-multiline-static"
            multiline
            rows={3}
            placeholder="Write the Caption"
            variant="standard"
            value={caption}
            onChange={handleCaption}
            required
          />
          <Stack spacing={2}>
            <label>upload an image</label>
            <input
              type="file"
              accept="image/*"
              value={file}
              onChange={handleFile}
              required
            />
            <Button variant="contained" onClick={handleSubmit} fullWidth>
              Post
            </Button>
          </Stack>
        </Box>
      </StyledModal>
    </>
  );
};
