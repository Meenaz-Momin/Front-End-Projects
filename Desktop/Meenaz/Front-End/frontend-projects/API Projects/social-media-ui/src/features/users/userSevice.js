import axios from "axios";

const API_URL = "http://192.168.1.37:8888/api/v1/users/";

const getMe = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.get(API_URL + "me", config);
  return response.data;
};

// upload profile
const profilePic = async (pic, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.post(API_URL + "profile-pic", pic, config);
  return response.data;
};

// update user
const updateUser = async (data, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.put(API_URL, data, config);
  console.log("service file ", response.data);
  return response.data;
};

// delete user
const deleteUser = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.delete(API_URL, config);
  return response.data;
};

const userService = {
  getMe,
  profilePic,
  updateUser,
  deleteUser,
};

export default userService;
