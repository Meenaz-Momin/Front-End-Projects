import { LockOutlined } from "@mui/icons-material";
import {
  Stack,
  Avatar,
  Button,
  Grid,
  Paper,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { register } from "../features/auth/authSlice";
import { toast } from "react-toastify";

function Register() {
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
    name: "",
    email: "",
    password: "",
  });
  const { name, email, password } = formData;

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(register(formData))
      .unwrap()
      .then(() => {
        navigate("/");
        toast.success("Registered user successfully");
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
            Sign Up
          </Typography>
        </Grid>
        <Stack spacing={3}>
          <TextField
            label="Username"
            placeholder="Enter Name"
            variant="standard"
            value={name}
            name="name"
            onChange={handleChange}
            fullWidth
            required
          />
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
            Sign Up
          </Button>
          <Typography>
            Do you have an account? <Link to="/login">Sign In</Link>
          </Typography>
        </Stack>
      </Paper>
    </Grid>
  );
}

export default Register;
