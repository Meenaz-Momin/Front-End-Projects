import axios from "axios";

const API_URL = "http://192.168.1.37:8888/api/v1/posts/";

// create post
const createPost = async (post, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.post(API_URL, post, config);
  return response.data;
};

// get all post
const getAllPost = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.get(API_URL, config);
  return response.data;
};

// get my  post
const getMyPost = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.get(API_URL + "me", config);
  return response.data;
};

// delete post
const deletePost = async (id, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.delete(API_URL + id, config);
  return response.data;
};

const postService = {
  createPost,
  getAllPost,
  getMyPost,
  deletePost,
};

export default postService;
