import { Face } from "@mui/icons-material";
import {
  AppBar,
  Avatar,
  styled,
  Toolbar,
  Typography,
  Box,
  Menu,
  MenuItem,
} from "@mui/material";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../features/auth/authSlice";
import { toast } from "react-toastify";
import { deleteUser } from "../features/user/userSlice";
import { getAllPost } from "../features/post/postSlice";
import UpdateUser from "./UpdateUser";

const StyleToolbar = styled(Toolbar)({
  display: "flex",
  justifyContent: "space-between",
});

const Icons = styled(Box)(({ theme }) => ({
  display: "none",
  gap: "20px",
  alignItems: "center",
  [theme.breakpoints.up("sm")]: { display: "flex" },
}));

const UserBox = styled(Box)(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  gap: "10px",
  [theme.breakpoints.up("sm")]: { display: "none" },
}));

const Navbar = () => {
  const [open, setOpen] = useState(false);
  const [update, setUpdate] = useState(false);
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { auth } = useSelector((state) => state.auth);

  const handleProfile = () => {
    navigate("/profile");
  };

  const handleClick = () => {
    navigate("/");
  };

  const handleLogout = () => {
    dispatch(logout())
      .unwrap()
      .then(() => {
        navigate("/");
        toast.success("Logout user successfully");
      })
      .catch(toast.error);
  };

  const handleDelete = () => {
    dispatch(deleteUser())
      .unwrap()
      .then(() => {
        navigate("/");
        toast.success("User deleted successfully");
        dispatch(getAllPost()).unwrap().catch(toast.error);
      })
      .catch(toast.error);
  };

  return (
    <AppBar position="sticky">
      <StyleToolbar>
        <Typography
          variant="h6"
          sx={{ display: { xs: "none", sm: "block " } }}
          onClick={handleClick}
        >
          {auth.data.name}
        </Typography>
        <Face sx={{ display: { xs: "block", sm: "none" } }} />

        <Icons>
          <Avatar
            src={`http://192.168.1.37:8888/${auth.prfile_pic}`}
            alt="profile"
            onClick={() => setOpen(true)}
          />
        </Icons>
        <UserBox onClick={() => setOpen(true)}>
          <Avatar
            src={`http://192.168.1.37:8888/${auth.prfile_pic}`}
            alt="profile"
          />
          <Typography variant="span">{auth.data.name}</Typography>
        </UserBox>
      </StyleToolbar>

      <Menu
        id="demo-positioned-menu"
        aria-labelledby="demo-positioned-button"
        open={open}
        onClose={() => setOpen(false)}
        anchorOrigin={{
          vertical: "top",
          horizontal: "right",
        }}
        transformOrigin={{
          vertical: "top",
          horizontal: "left",
        }}
      >
        <MenuItem onClick={handleProfile}>Profile</MenuItem>
        <MenuItem onClick={() => setUpdate(true)}>Update User</MenuItem>
        {update ? (
          <UpdateUser
            name2={auth.data.name}
            email2={auth.data.email}
            description2={auth.data.description}
          />
        ) : null}
        <MenuItem onClick={handleLogout}>Logout</MenuItem>
        <MenuItem onClick={handleDelete}>Delete Account</MenuItem>
      </Menu>
    </AppBar>
  );
};

export default Navbar;
