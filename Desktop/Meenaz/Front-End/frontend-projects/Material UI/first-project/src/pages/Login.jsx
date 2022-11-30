import { LockOutlined } from "@mui/icons-material";
import {
  Avatar,
  Button,
  Grid,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { login } from "../features/auth/authSlice";
import { toast } from "react-toastify";

function Login() {
  const paperStyle = {
    padding: 20,
    height: "70vh",
    width: 300,
    margin: "20px auto",
  };
  const avatarStyle = {
    backgroundColor: "#1bbd7e",
    marginBottom: "20px",
  };

  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const { email, password } = formData;

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(login(formData))
      .unwrap()
      .then(() => {
        navigate("/");
        toast.success("Login user successfully");
      })
      .catch(toast.error);
  };

  return (
    <Grid>
      <Paper elevation={10} style={paperStyle}>
        <Grid align="center">
          <Avatar style={avatarStyle}>
            <LockOutlined />
          </Avatar>
          <Typography variant="h4" mb={3}>
            Sign In
          </Typography>
        </Grid>
        <Stack spacing={3}>
          <TextField
            label="Email"
            placeholder="Enter Email"
            variant="standard"
            value={email}
            name="email"
            onChange={handleChange}
            fullWidth
            required
          />
          <TextField
            label="Password"
            placeholder="Enter Password"
            type="password"
            variant="standard"
            name="password"
            value={password}
            onChange={handleChange}
            fullWidth
            required
          />
          <Button
            variant="contained"
            type="submit"
            onClick={handleSubmit}
            fullWidth
          >
            Sign In
          </Button>
          <Typography>
            <Link to="/">Forgot Password</Link>
          </Typography>
          <Typography>
            Dont't have an account? <Link to="/register">Sign Up</Link>
          </Typography>
        </Stack>
      </Paper>
    </Grid>
  );
}

export default Login;
