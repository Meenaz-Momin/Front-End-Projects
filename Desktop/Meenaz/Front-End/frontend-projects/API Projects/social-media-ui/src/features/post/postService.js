import axios from "axios";

const API_URL = "http://192.168.1.37:8888/api/v1/posts/";

// create a post
const createPost = async (postData, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.post(API_URL, postData, config);
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

// get my post
const getMyPost = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.get(API_URL + "me", config);
  return response.data;
};

// get one post
const getOnePost = async (postId, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.get(API_URL + postId, config);
  return response.data;
};

// update post
const updatePost = async (data, token) => {
  const formData = new FormData();
  console.log(data?.files, "Update Post");
  formData.append("post_files", data.files);
  formData.append("caption", data.caption);
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.put(API_URL + data.id, formData, config);
  console.log("i am in service file");
  console.log(response.data);

  return response.data;
};

// delete post
const deletePost = async (postId, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await axios.delete(API_URL + postId, config);
  return response.data;
};

const postService = {
  createPost,
  getAllPost,
  getMyPost,
  getOnePost,
  deletePost,
  updatePost,
};

export default postService;
