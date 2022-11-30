import axios from "axios";

const API_URL = "http://192.168.1.37:8888/api/v1/users";

// update user
const updateUser = async (data, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.put(API_URL, data, config);
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
  updateUser,
  deleteUser,
};

export default userService;
