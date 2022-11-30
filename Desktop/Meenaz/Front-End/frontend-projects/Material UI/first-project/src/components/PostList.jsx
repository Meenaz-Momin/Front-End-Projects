import { Favorite, FavoriteBorder, MoreVert, Share } from "@mui/icons-material";
import {
  Avatar,
  Box,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  CardMedia,
  Checkbox,
  IconButton,
  Typography,
  MenuItem,
  Menu,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { deletePost, getMyPost, getAllPost } from "../features/post/postSlice";
import { useState } from "react";
import { toast } from "react-toastify";

const Post = ({ post }) => {
  const [open, setOpen] = useState({
    isOpen: false,
    id: "",
  });
  const { isOpen, id } = open;
  const navigate = useNavigate();
  const dispatch = useDispatch();
  console.log(open);
  const handlePostDelete = (e) => {
    e.preventDefault();
    if (window.confirm("are you sure, you want to delete?")) {
      dispatch(deletePost(id))
        .unwrap()
        .than(() => {
          toast.success("Post Deleted Successfully");
          navigate("/");
          dispatch(getAllPost());
          dispatch(getMyPost());
        })
        .catch(toast.error);
    }
  };
  return (
    <>
      {Array.isArray(post.data)
        ? post.data.map((postList) => {
            return (
              <Box key={postList.id}>
                <Card sx={{ margin: 5 }} elevation={10}>
                  <CardHeader
                    avatar={
                      <Avatar
                        alt="profile_pic"
                        src={`http://192.168.1.37:8888/${postList.user.prfile_pic}`}
                      />
                    }
                    action={
                      <IconButton aria-label="settings">
                        <MoreVert
                          onClick={() =>
                            setOpen({
                              isOpen: true,
                              id: `{postList.id}`,
                            })
                          }
                        />
                      </IconButton>
                    }
                    title={postList.user.name}
                  >
                    <Menu
                      id="demo-positioned-menu"
                      aria-labelledby="demo-positioned-button"
                      open={isOpen}
                      onClose={() => setOpen({ ...open, isOpen: false })}
                      anchorOrigin={{
                        vertical: "top",
                        horizontal: "right",
                      }}
                      transformOrigin={{
                        vertical: "top",
                        horizontal: "left",
                      }}
                    >
                      <MenuItem onClick={() => handlePostDelete()}>
                        Delete
                      </MenuItem>
                      {/* <MenuItem onClick={handleLogout}>View</MenuItem> */}
                    </Menu>
                  </CardHeader>
                  <CardMedia
                    component="img"
                    height="2%"
                    image={`http://192.168.1.37:8888/${postList.post_files[0]}`}
                    alt="post_image"
                  />
                  <CardContent>
                    <Typography variant="body2" color="text.secondary">
                      {postList.caption}
                    </Typography>
                  </CardContent>
                  <CardActions disableSpacing>
                    <Checkbox
                      icon={<FavoriteBorder />}
                      checkedIcon={<Favorite />}
                      color="error"
                    />
                    <IconButton aria-label="share">
                      <Share />
                    </IconButton>
                  </CardActions>
                </Card>
              </Box>
            );
          })
        : null}
    </>
  );
};

export default Post;
