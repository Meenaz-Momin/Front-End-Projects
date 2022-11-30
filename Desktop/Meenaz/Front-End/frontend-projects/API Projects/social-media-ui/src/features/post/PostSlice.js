import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { extractErrorMessage } from "../../utils";
import postService from "../post/postService";

const initialState = {
  posts: null,
  post: null,
  isLoading: false,
};

// Create new post
export const createPost = createAsyncThunk(
  "post/createPost",
  async (post, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await postService.createPost(post, token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

// get all posts
export const getAllPost = createAsyncThunk(
  "post/getAllPost",
  async (_, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await postService.getAllPost(token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

// get my posts
export const getMyPost = createAsyncThunk(
  "post/getMyPost",
  async (_, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await postService.getMyPost(token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

// get one posts
export const getOnePost = createAsyncThunk(
  "post/getOnePost",
  async (postId, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await postService.getOnePost(postId, token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

//update posts
export const updatePost = createAsyncThunk(
  "post/updatePost",
  async (data, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await postService.updatePost(data, token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

// delete posts
export const deletePost = createAsyncThunk(
  "post/deletePost",
  async (postId, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await postService.deletePost(postId, token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

const postSlice = createSlice({
  name: "post",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(createPost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(createPost.fulfilled, (state, action) => {
        state.posts = action.payload;
        state.isLoading = false;
      })
      .addCase(createPost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(getAllPost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getAllPost.fulfilled, (state, action) => {
        state.posts = action.payload;
        state.isLoading = false;
      })
      .addCase(getAllPost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(getMyPost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getMyPost.fulfilled, (state, action) => {
        state.post = action.payload;
        state.isLoading = false;
      })
      .addCase(getMyPost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(getOnePost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getOnePost.fulfilled, (state, action) => {
        state.post = action.payload;
        state.isLoading = false;
      })
      .addCase(getOnePost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(updatePost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(updatePost.fulfilled, (state, action) => {
        state.posts = action.payload;
        state.post = action.payload;
        state.isLoading = false;
      })
      .addCase(updatePost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(deletePost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(deletePost.fulfilled, (state, action) => {
        state.post = action.payload;
        state.posts = state.posts.map((post) =>
          post._id === action.payload._id ? action.payload : post
        );
      })
      .addCase(deletePost.rejected, (state) => {
        state.isLoading = false;
      });
  },
});

export default postSlice.reducer;
